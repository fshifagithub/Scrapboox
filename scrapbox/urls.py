"""
URL configuration for scrapbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from scrap import views
from django.conf import settings
from django.conf.urls.static import static# urls.py
from django.urls import path





urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.RegistrationView.as_view(),name="register"),
    path("signin",views.LoginView.as_view(),name="signin"),
    path("logout",views.SignOutView.as_view(),name="signout"),
    path("create",views.ScrapCreateView.as_view(),name="item-create"),
    path("itemview/<int:pk>/change",views.ScrapUpdateView.as_view(),name="itemupdate"),
    path('listall',views.ScrapboxListView.as_view(),name="list-all"),
    path("itemview/<int:pk>/details",views.ItemView.as_view(),name="itemview"),
    path("scrap/<int:pk>/remove",views.ScrapDeleteView.as_view(),name="scrap-remove"),
    path("scrapbox/<int:pk>/addtocart",views.AddToWishlist.as_view(),name="addtocart"),
    path("scrapbox/cartlist",views.CartListView.as_view(),name="cartlist-view"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


