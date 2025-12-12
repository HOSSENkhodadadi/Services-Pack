"""
Views for the Services Pack application.

Views are Python functions that:
1. Receive HTTP requests
2. Process the request (business logic goes here)
3. Return HTTP responses (usually JSON for APIs)

This file contains all the backend logic for our services.
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import FileResponse, Http404
from django.conf import settings
from groq import Groq
import os

import json


# ============================================================================
# HEALTH CHECK ENDPOINT
# ============================================================================

@require_http_methods(["GET"])
def health_check(request):
    """
    Simple endpoint to verify Django backend is running.
    Test at: http://localhost:8000/api/health/
    
    Returns:
        JSON with status message
    """
    return JsonResponse({
        'status': 'ok',
        'message': 'Django backend is running!'
    })


# ============================================================================
# CHATBOT SERVICE
# ============================================================================
import boto3
import json
# import os
# os.environ['AWS_BEARER_TOKEN_BEDROCK'] = "${bedrock-api-key-YmVkcm9jay5hbWF6b25hd3MuY29tLz9BY3Rpb249Q2FsbFdpdGhCZWFyZXJUb2tlbiZYLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFTSUEzTTQ2VVhJMlpPRUlHRU9MJTJGMjAyNTEyMTElMkZldS1ub3J0aC0xJTJGYmVkcm9jayUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjExVDIzNDA0M1omWC1BbXotRXhwaXJlcz00MzIwMCZYLUFtei1TZWN1cml0eS1Ub2tlbj1JUW9KYjNKcFoybHVYMlZqRUM4YUNtVjFMVzV2Y25Sb0xURWlSekJGQWlCeHdTUFpPQ0VpcUJwVWIzeGNMUTFqcm80JTJGJTJGNkd4VHdtU08zRHAlMkZLU3NZZ0loQU1XSXZrcjhnYmJvUzVPNmwwaE80M1NuNnFlbzlQRGVNUzFGZ2VGVTFFV0hLcTREQ1BuJTJGJTJGJTJGJTJGJTJGJTJGJTJGJTJGJTJGJTJGd0VRQUJvTU56Z3pOakkzTXpZNU1ERXpJZ3lUSUNpbmdGOWhqd0ZHYkRvcWdnTmpjenYzT1FJcDNEN2UzUFhrVXVMNDM1b3dWNyUyQjNmdW5tNTBOTkZ3djBRUXNBVUZ3M3RTaThRV1M3WUpneUpnZ295Y0c5cUhVMFBGdCUyQkJVcDBMbW1tcEo4dDk3WXNISUVadjMlMkZRRWs2M29UTnpQZ3YzaXFQbEtyY21aaExqN29BNE1DRW5LNlFBZUpuc04ycmFmQXVjNG1oTW9DR1pPZmhQR1glMkIySER6dVhOJTJGaWhraDRyS1NiSjFsMGEzUktSZlEwcW1qVFBBRFBOaHhhZDdKQzFOYUNJeUpqbUpNY3VoRVJ4cFVTeXhwbnN0Zmp5VCUyRmlrSGVwQjI3OWZXdXZacWtOZUlLOUJ3TGhPUmRiaWVvYUJDUm8lMkJoUTZ6JTJCd2olMkZ1MEZnSXp6SkFNbXZXdzNiMDRVNDZVM2Q5JTJGN0V0bU9NOTZseU5tWEhvMXNZYWVMOSUyQmNadiUyQlRERWclMkJJVVpsdVVjYjdTa0szdyUyQmsxZ2FLOEZtVFdZbzhlR2w1QUJCUmNYZjk1M0s0WlhnSTZaRktBY3JiNzVHTkNjdnhRcTJHTzQ3d2FUU3BDOENxTzhRbGFvYUVocFE2SjdNTmpHZ2JBREZjUGJLdmZnZEQ5anltWDhqWUd4T3hLY1pSakMxWlZtQnp0JTJGJTJCV2c2bVoxaURleGUlMkJ3bWVwN0RpVThQdUpyUnQ1TG9MekNMOU96SkJqcmVBbTNRcm9LeGRxMmFrejd5dUV1dUNaZmJLRXRDMyUyRnJvYmRJMVlNbjI3UVRncENaWURaYlJUYVNuYjg4ZjVuY2NkYnBUZHp2dHF1WGIlMkZsOEF0QnUlMkY3ZlJzbjBsWTh2dzJoUzFIemNkb3BIZDJNNDg0T2lFcmM5RksycDB2STQ5Z0F2V0VRVmZiUU5nQUJ3RllnUVJPcHlLcVFmaVdSM3cyQVR0dmJFbEtpdVRCcDRiNFRqUGk4SUVRdjFNY2Z1NEl5S2lVQjVHOVpObHdHYTVxdWh5QWM3M3JCTDBoYno2bVUwdmthSTB2VEIlMkJBY3NydnJOQld5TklaMGtJVUZ3eDk5bWlNUFgweWMyTXAzZ1lTMldKeXpMVyUyRk50TUp1SlFGdHpTUmk5Wm84ZEtlN0hwdE4xUVklMkJ0amNaVDh2dERvV2ZWbFV0YWxHTWJYcjBjJTJGeVR3ODZIMkxrJTJCb3Y4Z29yWnZ2cUR3V0FKN1F6QldyelhPRkJvcmVSM1lDZ0FndVF5dTclMkYxM1JBSWplYU9PR3MlMkJ4djlUTCUyRiUyRldFb3FPTmphVE9BT3pDWTFJV1dPd0pOOVozNDVsRFhoajFoOUZBaVNoSzl2QnhqQW9hVTlwMGdtMVBPRFkmWC1BbXotU2lnbmF0dXJlPTVjZTk5MWFhMzgyOWY2NjFiNzE4YmE1NTVlZTI1YTJiNmZkYTNlMTQzNTg4ZTQ1ZjZhN2JkZjg0MmU2ZGQ1NzEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JlZlcnNpb249MQ==}"
# bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')
@csrf_exempt  # Disables CSRF for simplicity in learning - use with caution in production
@require_http_methods(["POST"])  # Only accept POST requests
def chatbot(request):
    """
    API endpoint for the conversational bot.
    
    This function receives messages from the frontend and returns bot responses.
    
    Expected Request Format (JSON):
    {
        "message": "Hello, bot!"
    }
    
    Response Format (JSON):
    {
        "response": "Bot's reply here",
        "status": "success"
    }
    
    HOW TO ADD YOUR CHATBOT LOGIC:
    ================================
    Currently, this is a simple echo bot for demonstration.
    
    To integrate your own chatbot:
    1. Replace the simple logic below with your chatbot code
    2. You might use:
       - OpenAI API (import openai)
       - Transformers library (from transformers import pipeline)
       - Your own trained model
       - Rule-based logic
       - Any other AI service
    
    Example with OpenAI:
        import openai
        openai.api_key = 'your-key'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_response = response.choices[0].message.content
    
    Example with simple rules:
        if "hello" in user_message.lower():
            bot_response = "Hi there! How can I help you?"
        elif "weather" in user_message.lower():
            bot_response = "I can't check the weather, but it's always sunny in code!"
        else:
            bot_response = "Interesting question! Tell me more."
    """

    client = Groq(
    api_key=os.environ.get("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"),
)
    try:
        # Parse the JSON data from the request
        data = json.loads(request.body)
        user_message = data.get('message', '')
    #     prompt = f"Answer to the following question from the user: {user_message}."
    #     kwargs = {
    # "modelId": "amazon.titan-text-lite-v1",
    # "contentType": "application/json",
    # "accept": "*/*",
    # "body": json.dumps(
    #     {
    #         "inputText": prompt
    #     }
    # )
    #     }
        # response = bedrock_runtime.invoke_model(**kwargs)
        # print(response)
        # response_body = json.loads(response.get('body').read())
        # response_text = response_body['results'][0]['outputText']
        
        # ====================================================================
        # YOUR CHATBOT LOGIC GOES HERE
        # ====================================================================
        # Current implementation: Simple echo bot for demonstration
        # Replace this with your actual chatbot logic!
        completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {
            "role": "user",
            "content": user_message
        }
        ],
        temperature=1,
        # max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None
        )
        response_text = ""
        for chunk in completion:
            # print(chunk.choices[0].delta.content or "", end="")
            response_text += chunk.choices[0].delta.content or ""
        
        bot_response = f" {response_text}"
        
        # You could also add:
        # - Conversation history tracking
        # - User session management
        # - Database storage of conversations
        # - Multi-turn context handling
        # ====================================================================
        
        # Return the response as JSON
        return JsonResponse({
            'response': bot_response,
            'status': 'success'
        })
        
    except json.JSONDecodeError:
        # Handle invalid JSON
        return JsonResponse({
            'response': 'Invalid request format',
            'status': 'error'
        }, status=400)
    
    except Exception as e:
        # Handle any other errors
        return JsonResponse({
            'response': f'An error occurred: {str(e)}',
            'status': 'error'
        }, status=500)


# ============================================================================
# HOW TO ADD NEW SERVICES
# ============================================================================
"""
To add a new service (e.g., "Image Generator", "Text Summarizer"):

1. CREATE A NEW VIEW FUNCTION:
   Copy the structure above and modify it for your service.
   
   @csrf_exempt
   @require_http_methods(["POST"])
   def image_generator(request):
       try:
           data = json.loads(request.body)
           prompt = data.get('prompt', '')
           
           # YOUR SERVICE LOGIC HERE
           result = "Generated image URL here"
           
           return JsonResponse({
               'result': result,
               'status': 'success'
           })
       except Exception as e:
           return JsonResponse({
               'response': str(e),
               'status': 'error'
           }, status=500)

2. REGISTER THE URL:
   Go to services/urls.py and add:
   path('image-generator/', views.image_generator, name='image_generator'),

3. CREATE FRONTEND PAGE:
   Create a new HTML file in /frontend/ for the UI
   Add JavaScript to call your new API endpoint

4. ADD BUTTON TO HOMEPAGE:
   Update frontend/index.html to include a button for your new service
"""


# ============================================================================
# EXAMPLE: Additional service placeholder
# ============================================================================

@csrf_exempt
@require_http_methods(["POST"])
def example_service(request):
    """
    Template for a new service.
    This is currently a placeholder - implement your logic here!
    """
    try:
        data = json.loads(request.body)
        
        # Add your service logic here
        result = "Service not implemented yet"
        
        return JsonResponse({
            'result': result,
            'status': 'success'
        })
        
    except Exception as e:
        return JsonResponse({
            'response': str(e),
            'status': 'error'
        }, status=500)
