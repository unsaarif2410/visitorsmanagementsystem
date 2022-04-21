"""visitorsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views.indexpage,name="homepage"),
    path('signup/',views.Userreg_view, name="sign"),
    path('login/',views.loginpage, name="login"),
    
    path('logout/',views.logout, name="logout"),
    path('view/',views.view,name="user"),
    path('visitorentry/',views.Visitorentry_view, name="visitor"),
    path('deptentry/',views.DeptEntry_view, name="deptentry"),
    path('viewdept/',views.view_dept,name="dept"),
    path('deletedept/<int:id>',views.delete_dept),
    path('editdept/<int:id>',views.edit_dept),
    path('updatedept/<int:id>',views.update_dept),
    path('delete/<int:id>',views.delete),
    path('viewvisitor/',views.view_visitor,name="visit"),
    path('edit/<int:id>',views.edit),
    path('deletevisitor/<int:id>',views.delete_visitor),
    path('editvisitor/<int:id>',views.edit_visitor),
    path('update/<int:id>',views.update),
    path('updatevisitor/<int:id>',views.update_visitor),
    path('CheckOutvisitor/<int:id>',views.CheckOut_visitor_entry),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]
