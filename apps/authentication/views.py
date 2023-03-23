from django.contrib.auth.views import LoginView



class Login(LoginView):
    """
    
    """
    template_name = 'authentication/login/login.html'
    redirect_authenticated_user = True