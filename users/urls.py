from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login" ),        # Add the login view
    # path('productos/', include('products.urls')),
]
