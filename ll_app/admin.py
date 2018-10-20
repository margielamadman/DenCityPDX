from django.contrib import admin
from ll_app.models import Listing, Profile, Zipcode, ListingType
# Register your models here.

admin.site.register(Profile)


class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'listing_zipcode', 'category', 'address', 'sqft']

admin.site.register(Listing, ListingAdmin)


class ZipcodeAdmin(admin.ModelAdmin):
    list_display = ['zipcode']

admin.site.register(Zipcode)


class ListingTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'parent', 'name']

admin.site.register(ListingType, ListingTypeAdmin)


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['listing_type', 'category']
#
# admin.site.register(Category, CategoryAdmin)
