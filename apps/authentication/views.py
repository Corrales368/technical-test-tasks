from django.contrib.auth.views import LoginView



class Login(LoginView):
    """
    Login view that receives username and password.
    All logic is implemented by the inherited class Django LoginView
    """
    template_name = 'authentication/login/login.html'
    redirect_authenticated_user = True