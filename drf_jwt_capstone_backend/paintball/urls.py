from django.urls import path
from paintball import views
# from django.conf.urls import url


urlpatterns = [
    path('listings/getall/', views.get_all_listings),
    path('listings/post/', views.post_listing),
    path('listings/put/<int:user_id>/', views.put_listing),
    path('listings/get/', views.get_current_users_listings),
    path('listings/get/<int:user_id>/', views.get_users_listings_by_id),
    path('listings/delete/<int:user_id>/', views.delete_listing),
    path('reviews/post/', views.post_review),
    path('reviews/getall/<int:listers_id>/', views.get_all_listers_reviews),
    path('reviews/getall/', views.get_all_reviews),
    path('members/post/', views.post_member),
    path('members/get/<int:listers_id>/', views.get_members),
    path('create-checkout-session/', views.post_checkout),
]
