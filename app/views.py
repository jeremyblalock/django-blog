from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

def login_func(request):
    success = False
    attempt = False
    if request.method == 'POST':
        attempt = True
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                success = True
            else:
                # Return a 'disabled account' error message
                pass
        else:
            # Return an 'invalid login' error message.
            pass
    return render(request, 'registration/login.html',
        {'success': success, 'user': request.user })

def logout_func(request):
    logout(request)
    return render(request, 'registration/login.html')
