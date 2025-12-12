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
from django.urls import path, include

urlpatterns = [
    # Django admin interface - useful for managing data
    # Access at: http://localhost:8000/admin/
    path('admin/', admin.site.urls),
    
    # All our service API endpoints are under /api/
    # This includes the chatbot and any future services
    path('api/', include('services.urls')),
]
