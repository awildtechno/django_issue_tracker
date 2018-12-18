from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from apps.users.models import User
from apps.issues.models import Issue


@login_required
def all_issues(request):
    return render(request, 'issues/all_issues.html')


@login_required
def my_issues(request):
    return render(request, 'issues/my_issues.html')


@login_required
def priority_issues(request):
    return render(request, 'issues/priority_issues.html')


@login_required
def issue(request, issueno):
    try:
        issue = Issue.objects.get(id=issueno)
    except ObjectDoesNotExist:
        return redirect('/issues/all')

    return render(request, 'issues/issue.html', {'issue': issue})
