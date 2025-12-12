"""
URL Configuration for the Services Pack project.

This file routes incoming HTTP requests to the appropriate views.

How URLs work in Django:
1. A request comes in (e.g., /api/chatbot/)
2. Django checks urlpatterns in order
3. When it finds a match, it calls the associated view function
4. The view processes the request and returns a response

To add a new service:
1. Create a new view in services/views.py
2. Import it here
3. Add a new path() to urlpatterns below
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    # Root URL - serve the frontend homepage
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # Chatbot page
    path('chatbot.html', TemplateView.as_view(template_name='chatbot.html'), name='chatbot_page'),
    
    # Django admin interface - useful for managing data
    # Access at: http://localhost:8000/admin/
    path('admin/', admin.site.urls),
    
    # All our service API endpoints are under /api/
    # This includes the chatbot and any future services
    path('api/', include('services.urls')),
    
    # Serve static files (CSS, JS) from frontend folder
    re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR.parent / 'frontend'}),
]
