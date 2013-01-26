from django.shortcuts import render
from django.contrib.auth.decorators import login_required
 
@login_required
def dashboard_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise,
    take them to the login page.
    """
    return render(request, 'dashboard/Templates/index.html')