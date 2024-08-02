from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('account.urls')),
    path('project/', include('project.urls')),
    path('project/<uuid:project_id>/', include('todolist.urls')),
    path('project/<uuid:project_id>/<uuid:todolist_id>/', include('task.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
