from rest_framework.parsers import JSONParser
from api.serializers import PaymentIntentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from dashboard.models import User
from dashboard.models import Payment_Intent
from api.fusion import fusion_generator

# Create your views here.

# {
#     "amount": 300.5,
#     "order_id": "HHBNH567HVHJB",
#     "return_url": "https://shade.com/return/user"
# }

class PaymentIntentApiView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data["user"] = request.user.pk
        data["status"] = "initiated"
        serializer = PaymentIntentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            intent = Payment_Intent.objects.get(pk=serializer.data["id"])
            fusion_link = fusion_generator(intent.pk)
            intent.redirect_url = fusion_link
            intent.save()

            res = {
                "amount": serializer.data["amount"],
                "redirect_url": intent.redirect_url,
                "status": serializer.data["status"]
            }

            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EntriesApiView(APIView):
    
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         entries = Entry.objects.filter(owner=request.user)
#         serializer = EntrySerializer(entries, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EntrySerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EntryApiView(APIView):

#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_object(self, id):
        
#         try:
#             return Entry.objects.get(pk=id)
#         except Entry.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#         entryObj = self.get_object(id)
#         serializer = EntrySerializer(entryObj)
#         return Response(serializer.data)

#     def put(self, request, id):
#         entryObj = self.get_object(id)
#         serializer = EntrySerializer(entryObj ,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         entryObj = self.get_object(id)
#         entryObj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)