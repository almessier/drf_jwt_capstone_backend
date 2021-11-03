from django.contrib import admin
from paintball.models import Listing
from paintball.models import Review
from paintball.models import Member


# Register your models here.
admin.site.register(Listing)
admin.site.register(Review)
admin.site.register(Member)
