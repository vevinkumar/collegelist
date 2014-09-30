from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.views import generic

from colleges.models import UserList, CollegeList

def index(request):	
    #logout(request)
    if request.user.is_authenticated():	
        return HttpResponseRedirect('districts/')
    uname = request.POST.get('user_name')
    passwd = request.POST.get('password') 
    if uname is None:
        return render(request, 'colleges/index.html')	
    else:
        user = authenticate(username=uname, password=passwd)
    if user is not None:
        # the password verified for the user
        if user.is_active:
			login(request, user)
			#return HttpResponse("Logged in")
			return HttpResponseRedirect('districts/')
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

def logmeout(request):
    logout(request)
    return render(request, 'colleges/index.html')
		
def districts(request):	
    if not request.user.is_authenticated():
	    return HttpResponse("You are not logged in")
    else:
        district_list = CollegeList.objects.values('district').distinct()
        context = {'district_list': district_list}
        return render(request, 'colleges/districts.html', context)
	
def colleges(request, district):
    college_list = CollegeList.objects.filter(district=district).order_by('college_name')
    return render(request, 'colleges/colleges.html', {'college_list': college_list})
    #return HttpResponse("You're looking at colleges in %s." % district)

def details(request, college_id):
    college = CollegeList.objects.filter(college_id=college_id)
    return render(request, 'colleges/details.html', {'college': college})