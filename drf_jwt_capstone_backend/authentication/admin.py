from django.contrib import admin
from paintball.models import Listing, Review, Member


# Register your models here.
admin.site.register(Listing)
admin.site.register(Review)
admin.site.register(Member)
