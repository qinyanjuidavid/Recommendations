from django.shortcuts import render
from Profiles.models import Profile

# Create


def mainView(request,*args,**kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print("id",profile.id)
    except:
        pass
    print(request.session.get_expiry_date())
    context = {
    }
    return render(request, "Profiles/main.html", context)
