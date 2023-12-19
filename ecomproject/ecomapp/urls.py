
from django.urls import path
from .views import index, login_view, forgot_password_view, signup_view, product_view

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('signup/', signup_view, name='signup'),
    path('products/', product_view, name='products'),  # Update the name to 'products'
]
