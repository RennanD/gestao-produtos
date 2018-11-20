from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout


def dash(request):
	return render (request,'dash.html')
	
def logout_view(request):
	logout(request)
	return redirect('dash')