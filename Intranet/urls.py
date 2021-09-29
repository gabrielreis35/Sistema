import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('main/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('produtos.urls')),
    path('colaborator/', include('colaborator.urls')),
    path('departments/', include('departments.urls'))
]

if settings.DEBUG:
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),