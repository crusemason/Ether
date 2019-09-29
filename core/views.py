from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .forms import RegistrationForm
from django.shortcuts import render
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'createaccount.html'




def indexView(request):
    print('mom is did it')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            CustomUser = form.save()
            # Do something with the user
            messages.success(request, 'User saved successfully.')
            success_url = reverse_lazy('login')
        else:
            messages.error(request, 'The form is invalid.')

        return render(request, 'login.html', {'form': form})

    else:
        form = RegistrationForm()
        return render(request, 'createaccount.html', {'form': form})

def login(request):
    return render(request, 'login.html')



def validate_username(request):
    username = request.GET.get('username', None)
    if(User.objects.filter(email__contains=username).exists()
            ):
            print('yessssiir')
            user = User.objects.get(email__contains=username)
            request.session['userid'] = user.id
    print(username)
    data = {
        'is_taken': User.objects.filter(email__contains=username).exists()
    }
    return JsonResponse(data)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import UserLoginForm
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def user_login(request):
    print('in dis hoe')
    context = RequestContext(request)
    authentication_form = UserLoginForm
    form = UserLoginForm
    uid = request.session['userid']
    user = User.objects.get(id=uid)
    initial = user.first_name[0]
    initial = initial.upper()
    print(initial)
    print('again'+str(user))
    if request.method == 'POST':
          username = str(user)
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("/users/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print  ("invalid login details " + username + " " + password)
              return render_to_response('login.html', {'form':form}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render_to_response('loginpw.html', {'form':form, 'user':user, 'initial':initial}, context)
