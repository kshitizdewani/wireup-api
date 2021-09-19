from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    permission_classes = []
    def get(self,request):
        return Response(data={'name':'Anurag','city':'bilaspur'})
    
    def post(self, request):
        print(request.data)
        return Response(status=status.HTTP_201_CREATED)
    
