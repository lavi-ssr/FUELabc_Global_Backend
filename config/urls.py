from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "api/v1/auth/",
        include("apps.users.urls"),
    ),

    path(
        "api/v1/",
        include("apps.vehicles.urls"),
    ),

    # =========================
    # AEM APIs
    # =========================
    path(
        "api/v1/aem/",
        include("apps.aem.urls"),
    ),

    path("api/v1/tripanalytics/", 
         include("apps.tripanalytics.urls")
         ), 

]