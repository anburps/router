
from django.urls import path,include


# urlpatterns = [
   
# ]
from rest_framework.routers import DefaultRouter

from app import views
router=DefaultRouter()
router.register("",views.BlogModelViewSet)

urlpatterns = [

    path('',include(router.urls)),
    path('generate_token/',views.GenerateToken.as_view(),name="generatetoken"),
    path('logout/', views.Logout.as_view(), name='logout'),


]