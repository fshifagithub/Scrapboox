from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from scrap.forms import UserForm,LoginForm,VehicleForm,ScrapboxForm,AddToCartForm
from django.contrib.auth import authenticate,login,logout
from scrap.models import scraps,UserProfile,Order,WishList
from django.contrib import messages

from django.urls import reverse

# Create your views here
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
           return render(request,"register.html",{"form":form})
        


# loginview
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
           unname=form.cleaned_data.get("username")
           pwd=form.cleaned_data.get("password")
           user_object=authenticate(request,username=unname,password=pwd)
           if user_object:
               login(request,user_object)
               messages.success(request,"logged in  successfully....")
               return redirect("list-all")
        print("invalid")
        messages.error(request,"error in login....")
        return render(request,"login.html",{"form":form})

class ScrapUpdateView(View):
    def get(self,request,*args,**kwargs):
     id=kwargs.get("pk")
     obj=scraps.objects.get(id=id)
     form=ScrapboxForm(instance=obj)
     return render(request,"scrap_update.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=scraps.objects.get(id=id)
        form=ScrapboxForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"updated successfuly")
            return redirect("list-all")
        else:
            messages.error(request,"failed...")
            return render(request,"scrap_update.html",{"form":form})
            


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



# scrapcreate
class ScrapCreateView(View):
    def get(self,request,*args,**kwargs):
        form=ScrapboxForm()
        return render(request,"scrap_create.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=ScrapboxForm(request.POST,files=request.FILES)
        if form.is_valid():
                form.instance.user=request.user
                form.save()
                messages.success(request,"....new data created successfully....")
                return redirect('list-all')
        else:
                messages.error(request,"....error on create new data....")
                return render(request,"scrap_create.html",{"form":form})

#list view
class ScrapboxListView(View):
    def get(self,request,*args,**kwargs):
        qs=scraps.objects.all()
        return render(request,"scrap_list.html",{"data":qs})

# itemview
class ItemView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=scraps.objects.get(id=id)
        return render(request,"scrapboxitem_view.html",{"data":qs})



class ScrapDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        scraps.objects.get(id=id).delete()
        return redirect("list-all")
    
class AddToWishlist(View):
    def post(self,request,*args,**kwargs):
        scrap_id=kwargs.get("pk")
        print(scrap_id)
        scrapbox_object=get_object_or_404(scraps,id=scrap_id)
        print(scrapbox_object)
        action=request.POST.get("action")
        print("...",action)
        cart,created=WishList.objects.get_or_create(user=request.user)
        if action == "addtocart":
            cart.scrap.add(scrapbox_object)
            messages.success("Added successfuly...")
        return redirect("list-all")
    
class CartListView(View):
    def get(self,request,*args,**kwargs):
        user_wishlist=WishList.objects.filter(user=request.user).first()
        return render(request,"cartlist.html",{"user_wishlist":user_wishlist})

    



    
    
