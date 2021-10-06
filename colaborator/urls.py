from django.urls import path
from .views import ColaboratorView, ColaboratorRegister

app_name = 'colaborators'

urlpatterns = [
    path('', ColaboratorView.as_view(template_name = 'colaborator/User.html'), name = 'Home_Colaborator'),
    path('signup/', ColaboratorRegister.as_view(template_name = 'colaborator/Signup.html'), name = 'Signup_Colaborator'),
]
