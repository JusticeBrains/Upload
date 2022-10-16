from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

admin.site.site_header = "Meeting Upload"
admin.site.site_title = "Meeting Upload Portal"
admin.site.index_title = "Welcome To Meeting Upload Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('academic/', include('academicmeetings.urls', namespace='academic_meetings')),
    path('', include('pages.urls',namespace='pages')),

    # path('accounts/', include('users.urls', namespace='users')),

    # browser reload
    path("__reload__/", include("django_browser_reload.urls")),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
