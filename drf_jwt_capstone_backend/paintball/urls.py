from django.urls import path
from paintball import views

urlpatterns = [
    path('listings/getall', views.get_all_listings),
    path('listings/post', views.post_listing),
]
