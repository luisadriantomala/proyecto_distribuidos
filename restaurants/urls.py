from django.conf.urls import url 
from restaurants import views 
 
urlpatterns = [ 
    url(r'^api/restaurants$', views.restaurants_list)
]