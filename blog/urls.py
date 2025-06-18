from django.contrib import admin
from django.urls import path, include
from .views import BlogView




# router = DefaultRouter()
# router.register('user', UserViewSet)

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    # path('', include(router.urls)), 
    # path('logout/', LogoutView.as_view(), name='logout'),    
]