from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .serializers import (
     SendOneTimePasswordSerializer,
       VerifyOneTimePasswordSerializer,
         LinkShortenerSerializer,   
)

# from .tasks import send_sms
from .models import LinkShortenerModel
from .permissions import IsOwnerOrReadOnly


from random import randint
from redis import Redis 
import shortuuid


from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404


redis_connection = Redis(host='redis', port=6379, db=0, charset='utf-8', decode_responses=True)


class SendOneTimePassword(APIView):

    def post(self, request, *args, **kwargs):

        serializer = SendOneTimePasswordSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data.get('phone_number')
        otp = str(randint(1000, 9999))
        
        if redis_connection.get(phone_number):
            return Response({'message': 'you have just received the code!'}, status=status.HTTP_400_BAD_REQUEST)
        
        redis_connection.set(phone_number, otp, ex=120)

        # send_sms.apply_async(args=[phone_number, otp])
        
        return Response({'otp': otp}, status=status.HTTP_200_OK)


  

class VerifyOneTimePassword(APIView):

    def post(self, request, *args, **kwargs):
        serializer = VerifyOneTimePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get('phone_number')
        otp = serializer.validated_data.get('otp')
    
        saved_otp = redis_connection.get(phone_number)
      
        if otp == saved_otp:
            user, created = User.objects.get_or_create(username=phone_number)

            refresh_token = RefreshToken().for_user(user)
            access_token = refresh_token.access_token

            data = {
                'access_token': str(access_token),
                'refresh_token': str(refresh_token)

                }
            
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    



class CreateShortedLink(APIView):
    

    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def post(self, request):
        serializer = LinkShortenerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        long_url = serializer.validated_data['orginal_url']
        short_url = shortuuid.uuid()[:6]
        shortened_url = LinkShortenerModel.objects.create(orginal_url=long_url, short_url=short_url, owner=request.user)
        
        return Response(LinkShortenerSerializer(shortened_url).data, status=status.HTTP_201_CREATED)


class RedirectToLongLink(APIView):

    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get(self, request, short_url):
        try:
            link = get_object_or_404(LinkShortenerModel, short_url=short_url , owner=request.user)
            absolute_url = link.get_absolute_url()
            link.url_viewed += 1
            link.save()
            return redirect(absolute_url)
        except:
            raise Http404('sorry')
            

class GetAllShortedLinks(APIView):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get(self, request):
        shortened_urls = LinkShortenerModel.objects.all()
        serializer = LinkShortenerSerializer(instance=shortened_urls, many=True)
        return Response(serializer.data)



    
