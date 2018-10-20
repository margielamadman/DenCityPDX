"""lotlocator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from ll_app.views import IndexView, RegisterView, SearchListView, ListingUpdateView, ListingDeleteView, ListingTypeCreateView, ListingCreateView, ListingDetailView, ProfileView, ZipcodeListView, CategoryListView, ZipcodeCategoryListView, AdulistingView
from ll_api.views import ListingListCreateAPIView, ListingRetrieveUpdateAPIView, CategoryListCreateAPIView, CategoryRetrieveUpdateAPIView, SubCategoryListCreateAPIView, SubCategoryRetrieveUpdateAPIView, CategoryListingListAPIView, SubCategoryListingListAPIView, UserCreateAPIView
from django.conf.urls.static import static
from django.conf import settings
from ll_app import views as ll_appviews
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='LotLocator API')


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^$', IndexView.as_view(), name='index_view'),
    re_path(r'^#about$', ll_appviews.about, name='about_view'),
    re_path(r'^adulistings/$', AdulistingView.as_view(), name='adulisting_view'),
    # re_path(r'explore/$', Explore.as_view(), name='explore_view'),
    re_path(r'^register/$', RegisterView.as_view(), name='register_view'),
    re_path(r'^register/profile/$', ProfileView.as_view(), name='profile_view'),
    re_path(r'^search/$', SearchListView.as_view(), name='search_list_view'),
    re_path(r'^listingcreate/(?P<categorypk>\d+)$', ListingCreateView.as_view(), name='listing_create_view'),
    re_path(r'^listingupdate/(?P<pk>\d+)$', ListingUpdateView.as_view(), name='listing_update_view'),
    re_path(r'^listingdelete/(?P<pk>\d+)$', ListingDeleteView.as_view(), name='listing_delete_view'),
    re_path(r'^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name='listing_detail_view'),
    re_path(r'^category/(?P<categorypk>\d+)/$', CategoryListView.as_view(), name='category_list_view'),
    re_path(r'^zipcode/(?P<zipcode>\d+)/$', ZipcodeListView.as_view(), name='zipcode_list_view'),
    re_path(r'^zipcode/(?P<zipcodepk>\d+)/(?P<categorypk>\d+)/$', ZipcodeCategoryListView.as_view(), name='zipcode_category_list_view'),
    # Start API urls
    re_path(r'^api/api-token-auth/', views.obtain_auth_token),
    re_path(r'^api/register/$', UserCreateAPIView.as_view(), name='create_user_view'),
    re_path(r'^api/listings/$', ListingListCreateAPIView.as_view(), name='listing-list'),
    re_path(r'^api/listings/(?P<pk>\d+)/$', ListingRetrieveUpdateAPIView.as_view(), name='listing-detail'),

    re_path(r'^api/categories/$', CategoryListCreateAPIView.as_view(), name='categories-list'),
    re_path(r'^api/categories/(?P<pk>\d+)/$', CategoryRetrieveUpdateAPIView.as_view(), name='categories-detail'),

    re_path(r'^api/sub_categories/$', SubCategoryListCreateAPIView.as_view(), name='sub-categories-list'),
    re_path(r'^api/sub_categories/(?P<pk>\d+)/$', SubCategoryRetrieveUpdateAPIView.as_view(), name='sub-categories-detail'),

    re_path(r'^api/category_listings/(?P<pk>\d+)/$', CategoryListingListAPIView.as_view(), name='category-listings-list'),
    re_path(r'^api/sub_category_listings/(?P<pk>\d+)/$', SubCategoryListingListAPIView.as_view(), name='sub-category-listings-list'),
    re_path(r'^api/docs/', schema_view),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
