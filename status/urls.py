from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    # path('yesterday/',views.yesterday_data,name='yesterday'),
    path('about/',views.about,name='about'),
]