from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout


from colleges.models import UserList, CollegeList

def index(request):
    return render(request, 'colleges/index.html')
	
def validate(request):		
    uname = request.POST.get('user_name')
    passwd = request.POST.get('password')
    user = authenticate(username=uname, password=passwd)
    if user is not None:
        # the password verified for the user
        if user.is_active:
			login(request, user)
			#return HttpResponse("Logged in")
			return HttpResponseRedirect('colleges/districts/')
			#logout(request)
        else:
		    logout(request)
		    return render(request, 'colleges/index.html', {
                'error_message': "The password is valid, but the account has been disabled!",
            })            
    else:
	    #logout(request)
		return render(request, 'colleges/index.html', {
            'error_message': "Invalid Login Credentials!",
        })
		
def districts(request):	
    if not request.user.is_authenticated():
	    return HttpResponse("You are not logged in")
    else:
        district_list = CollegeList.objects.values('district').distinct()
        context = {'district_list': district_list}
        return render(request, 'colleges/districts.html', context)
	
def colleges(request, district):
    return HttpResponse("You're looking at colleges in %s." % district)

def details(request, college_id):	
    college = get_object_or_404(CollegeList, pk=college_id)
    return render(request, 'colleges/details.html', {'college_id': college_id})