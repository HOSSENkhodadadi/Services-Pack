"""
URL routing for the services app.

This file maps URL patterns to view functions.
Every API endpoint for our services is defined here.

URL Pattern Format:
    path('endpoint-name/', views.function_name, name='url_name')
    
The 'name' parameter is used for reverse URL lookup in Django.
"""

from django.urls import path
from . import views

# All these URLs will be prefixed with /api/ (defined in config/urls.py)
urlpatterns = [
    # Chatbot endpoint: /api/chatbot/
    path('chatbot/', views.chatbot, name='chatbot'),
    
    # Example service endpoint: /api/example/
    path('example/', views.example_service, name='example_service'),
    
    # ========================================================================
    # TO ADD A NEW SERVICE:
    # ========================================================================
    # 1. Create a view function in views.py
    # 2. Add a new path here:
    #    path('your-service/', views.your_service_function, name='your_service'),
    # 3. The frontend can then call: http://localhost:8000/api/your-service/
    # ========================================================================
]
