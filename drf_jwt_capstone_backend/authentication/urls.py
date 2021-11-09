from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from authentication import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('getall/', views.get_all_users),
    path('getalllisted/', views.get_all_users_listed),
    path('get/<int:user_id>/', views.get_user_by_id),
    path('put/<int:user_id>/', views.put_user),
]
