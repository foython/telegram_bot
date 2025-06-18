from django.contrib import admin
from django.urls import path, include
from .views import login_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LogoutView, UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('', include(router.urls)), 
    path('logout/', LogoutView.as_view(), name='logout'),    
]