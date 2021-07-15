from django.shortcuts import render
from Profiles.models import Profile
from django.contrib.auth  import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create


def SignupView(request):
    profile_id=request.session.get('ref_profile')
    print("Profile id",profile_id)
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            if profile_id is not None:
                recommended_by_profile=Profile.objects.get(id=profile_id)
                instance=form.save()
                registered_user=User.objects.get(id=instance.id)
                registered_profile=Profile.objects.get(user=requested_user)
                registered_profile.recommended_by=recommended_by_profile
                registered_profile.save()
            else:
                form.save()
    context = {
        'form':form
    }
    return render(request, "Profiles/signup.html", context)


def mainView(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print("id", profile.id)
    except:
        pass
    print(request.session.get_expiry_date())
    context = {
    }
    return render(request, "Profiles/main.html", context)
