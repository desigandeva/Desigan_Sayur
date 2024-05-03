from django.urls import path
from hello import views


urlpatterns = [
    path('home/',views.home),
    path('',views.wellcome),
    path('sayhello/',views.sayhello),
]
