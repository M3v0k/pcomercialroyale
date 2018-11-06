from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'm2m.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'', include('royale.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
