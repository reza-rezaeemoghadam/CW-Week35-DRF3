from rest_framework.urls import path

from .views import (RegisterAPIView, LoginAPIView,
                    ContactListAPIView, AddContactAPIView, DeleteContactAPIView, UpdateContactAPIView) 

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="user_register"),
    path('login/', LoginAPIView.as_view(), name="user_login"),
    path('contact/list', ContactListAPIView.as_view(), name="contact_list"),
    path('contact/add', AddContactAPIView.as_view(), name="contact_add"),
    path('contact/delete', DeleteContactAPIView.as_view(), name="contact_delete"),
    path('contact/update', UpdateContactAPIView.as_view(), name="contact_update"),
]
