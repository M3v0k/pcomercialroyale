from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'm2m.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'', include('royale.urls')),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]

if settings.DEBUG:
    from django.conf.urls.static import static
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
