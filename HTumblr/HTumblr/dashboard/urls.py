from django.conf.urls.defaults import *
from HTumblr.dashboard.views import *
 
urlpatterns = patterns('',
 
    # Main web dashboard entrance.
    (r'^$', dashboard_main_page),
 
)