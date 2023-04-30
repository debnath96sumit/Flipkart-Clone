from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('mycart/', views.mycart, name='mycart'),
    path('search/', views.search, name='search'),
    path('details/<int:id>', views.details, name='details'),
]

