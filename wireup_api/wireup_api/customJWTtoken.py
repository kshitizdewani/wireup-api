from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        token['email'] = user.email
        
        # if user.groups.filter(name='tutor').exists():
        #     token['role'] = 'tutor'
        # elif user.groups.filter(name='student').exists():
        #     token['role'] = 'student'
            
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
