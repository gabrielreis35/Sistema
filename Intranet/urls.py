import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.urls import path, include

import clients

urlpatterns = [
    path('', include('main.urls', namespace='main:Home_Main')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('produtos.urls', namespace='products')),
    path('colaborator/', include('colaborator.urls', namespace='colaborators')),
    path('departments/', include('departments.urls', namespace='departments')),
    path("workOrder/", include('workOrder.urls', namespace="workOrder")),
    path("clients/", include('clients.urls', namespace="clients")),
    path("settings/", include('settings.urls', namespace="settings")),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)