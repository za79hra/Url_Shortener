from django.urls import path
from .views import (

    SendOneTimePassword,
    VerifyOneTimePassword,
    CreateShortedLink,
    GetAllShortedLinks,
    RedirectToLongLink,
)
from rest_framework_simplejwt.views import TokenRefreshView


app_name = 'short'
urlpatterns = [
    path('login/', SendOneTimePassword.as_view(), name='client_login'),
    path('verify/', VerifyOneTimePassword.as_view(), name='verify_login'),
    path('refresh/', TokenRefreshView.as_view()),
    
    path('shorten/', CreateShortedLink.as_view(), name='short_link'),
    path('shortened-links/', GetAllShortedLinks.as_view(), name='get_short_link'),
    path('<str:short_url>/', RedirectToLongLink.as_view(), name='redirect-to-long-link'), 
  
]
