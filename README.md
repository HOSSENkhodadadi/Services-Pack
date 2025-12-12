# Services Pack - Educational Web Application

A beginner-friendly web application demonstrating Django backend with HTML/CSS/JavaScript frontend, following software engineering best practices.

## 📁 Project Structure

```
/backend     → Django backend (APIs, business logic)
/frontend    → HTML/CSS/JavaScript frontend (UI)
```

## 🚀 Features

- **Services Homepage**: Clean interface with service cards
- **Conversational Bot**: Fully functional chat interface with Django API integration
- **Extensible Architecture**: Easy to add new services
- **Well-Documented Code**: Comments explaining how everything works

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Backend Setup

1. **Navigate to backend folder**:
   ```bash
   cd backend
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

   The backend will be running at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend folder**:
   ```bash
   cd frontend
   ```

2. **Open in browser**:
   - Simply open `index.html` in your web browser
   - OR use a local server (recommended for development):
     - VS Code: Use "Live Server" extension
     - Python: `python -m http.server 8080`
     - Node.js: `npx http-server`

3. **Make sure Django is running** before testing the chatbot!

## 📖 How to Use

### Homepage
- Visit the homepage to see all available services
- Click on "Conversational Bot" to open the chat interface
- Other services are placeholders showing how to add more

### Chatbot
- Type a message in the input box
- Press Enter or click "Send"
- The bot will respond (currently echoes your message)
- Backend logic is ready for you to add your own AI integration

## 🔧 Adding New Services

### 1. Create Backend API Endpoint

In `backend/services/views.py`, add a new view function:

```python
@csrf_exempt
@require_http_methods(["POST"])
def your_service(request):
    try:
        data = json.loads(request.body)
        # Your service logic here
        result = "Your result"
        
        return JsonResponse({
            'result': result,
            'status': 'success'
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'status': 'error'
        }, status=500)
```

### 2. Register the URL

In `backend/services/urls.py`, add:

```python
path('your-service/', views.your_service, name='your_service'),
```

### 3. Create Frontend Page

Create `frontend/your-service.html` with:
- UI elements (forms, display areas)
- JavaScript to call your API endpoint
- Styling using the shared `styles.css`

### 4. Add Button to Homepage

In `frontend/index.html`, add a new service card:

```html
<div class="service-card">
    <div class="service-icon">🎨</div>
    <h2>Your Service</h2>
    <p>Description of your service</p>
    <button class="service-btn" onclick="openService('your-service.html')">
        Open Service
    </button>
</div>
```

## 📚 Code Organization

### Backend (`/backend`)

- `config/` - Django project settings and configuration
  - `settings.py` - All Django settings
  - `urls.py` - Main URL routing
- `services/` - Main application code
  - `views.py` - API endpoints and business logic
  - `urls.py` - Service-specific URL routing
  - `models.py` - Database models (currently empty)
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies

### Frontend (`/frontend`)

- `index.html` - Homepage with service cards
- `chatbot.html` - Conversational bot interface
- `chatbot.js` - Chatbot-specific JavaScript
- `app.js` - Shared JavaScript functions
- `styles.css` - All styles for the application

## 🎓 Learning Resources

### Key Concepts Demonstrated

1. **RESTful API Design**: Backend endpoints follow REST principles
2. **Separation of Concerns**: Frontend and backend are separate
3. **CORS Configuration**: Proper cross-origin resource sharing setup
4. **Error Handling**: Try-catch blocks and proper HTTP status codes
5. **Code Documentation**: Extensive comments explaining how things work

### Django Concepts

- Views and URL routing
- JSON responses for APIs
- CORS middleware
- Settings configuration
- App structure

### Frontend Concepts

- Fetch API for HTTP requests
- Async/await for asynchronous operations
- DOM manipulation
- Event handling
- CSS Grid and Flexbox

## 🔒 Security Notes

**This is a learning project**. For production use:

1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS` properly
4. Enable CSRF protection (remove `@csrf_exempt`)
5. Add authentication and authorization
6. Use HTTPS
7. Validate and sanitize all inputs
8. Add rate limiting

## 🐛 Troubleshooting

### "Could not connect to server" error in chatbot
- Make sure Django is running (`python manage.py runserver`)
- Check that the backend is on `http://localhost:8000`
- Look at browser console for detailed error messages

### Django import errors
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt`

### CORS errors
- Check `CORS_ALLOWED_ORIGINS` in `settings.py`
- Make sure your frontend URL is listed there

## 📝 Next Steps

1. **Implement actual chatbot logic**:
   - Integrate OpenAI API
   - Use Hugging Face transformers
   - Build rule-based system

2. **Add new services**:
   - Image generator
   - Text summarizer
   - Language translator

3. **Enhance the UI**:
   - Add dark mode
   - Improve animations
   - Make it responsive

4. **Add features**:
   - User authentication
   - Save conversation history
   - File uploads

5. **Deploy the application**:
   - Backend: Heroku, Railway, or AWS
   - Frontend: Netlify, Vercel, or GitHub Pages

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new services
- Improve documentation
- Enhance the UI/UX
- Add tests

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

## ❓ Questions?

Check the comments in the code - they're designed to help you understand:
- Where to add new features
- How to connect frontend to backend
- How to extend the project
- Common patterns and best practices

Happy coding! 🚀
