from django.urls import path
from paintball import views

urlpatterns = [
    path('listings/getall', views.get_all_listings),
    path('listings/post', views.post_listing),
    path('listings/put/<user_id>/', views.put_listing),
    path('listings/get', views.get_users_listings),
    path('listings/delete', views.delete_listing),
    path('reviews/post', views.post_review),
    path('reviews/getall/<int:listers_id>', views.get_all_listers_reviews),
    path('reviews/getall/', views.get_all_reviews),

]
