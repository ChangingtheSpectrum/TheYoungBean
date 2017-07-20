from django.conf.urls import url
from django.contrib import admin
import sitepages.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', sitepages.views.home, name='home'),
    url(r'^about-us/', sitepages.views.about_us, name='about-us'),
    url(r'^our-menu/', sitepages.views.our_menu, name='our-menu'),
]
