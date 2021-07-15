from django.shortcuts import render
from Profiles.models import Profile

# Create
def main_view(request):
    context={

    }
    return(request,"Profiles/main.html",context)