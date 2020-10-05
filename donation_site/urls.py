from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as core_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),
    path('donate/', core_views.donate, name='donate'),
    path('success/<str:args>', core_views.successPage, name='success'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
