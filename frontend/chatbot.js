/*
================================================================================
CHATBOT JAVASCRIPT - Frontend Logic for Conversational Bot
================================================================================
This file handles all the chat functionality:
- Sending messages to the backend API
- Receiving and displaying bot responses
- UI updates and interactions
*/

// Configuration
const API_URL = 'http://localhost:8000/api/chatbot/';

// DOM elements - we'll reference these frequently
const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

/**
 * Send a message to the chatbot
 * This is the main function that handles user messages
 */
async function sendMessage() {
    // Get the user's message from the input field
    const userMessage = messageInput.value.trim();
    
    // Don't send empty messages
    if (!userMessage) {
        return;
    }
    
    // Display the user's message in the chat
    addMessage(userMessage, 'user');
    
    // Clear the input field
    messageInput.value = '';
    
    // Disable send button while waiting for response
    sendButton.disabled = true;
    sendButton.textContent = 'Sending...';
    
    // Show typing indicator
    const typingIndicator = showTypingIndicator();
    
    try {
        // ====================================================================
        // SEND REQUEST TO DJANGO BACKEND
        // ====================================================================
        // This is where the frontend connects to the backend API
        
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: userMessage
            })
        });
        
        // Check if the request was successful
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        // Parse the JSON response from Django
        const data = await response.json();
        
        // Remove typing indicator
        typingIndicator.remove();
        
        // Display the bot's response
        if (data.status === 'success') {
            addMessage(data.response, 'bot');
        } else {
            addMessage('Sorry, something went wrong. Please try again.', 'bot');
        }
        
    } catch (error) {
        // Handle any errors
        console.error('Error:', error);
        typingIndicator.remove();
        addMessage(
            '⚠️ Could not connect to the server. Make sure the Django backend is running on http://localhost:8000',
            'bot'
        );
    } finally {
        // Re-enable send button
        sendButton.disabled = false;
        sendButton.textContent = 'Send';
        
        // Focus back on input for next message
        messageInput.focus();
    }
}

/**
 * Add a message to the chat display
 * 
 * @param {string} text - The message text to display
 * @param {string} sender - Either 'user' or 'bot'
 */
function addMessage(text, sender) {
    // Create message container
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    
    // Add sender label
    const senderLabel = document.createElement('div');
    senderLabel.className = 'message-sender';
    senderLabel.textContent = sender === 'user' ? 'You' : 'Bot';
    
    // Add message text
    const messageText = document.createElement('div');
    messageText.textContent = text;
    
    // Assemble the message
    messageDiv.appendChild(senderLabel);
    messageDiv.appendChild(messageText);
    
    // Add to chat window
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom to show latest message
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Show typing indicator while waiting for bot response
 * Returns the indicator element so it can be removed later
 */
function showTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.className = 'message bot typing-indicator';
    indicator.innerHTML = `
        <span></span>
        <span></span>
        <span></span>
    `;
    chatMessages.appendChild(indicator);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return indicator;
}

/**
 * Handle Enter key press in input field
 * Allows sending messages by pressing Enter
 */
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

/**
 * Focus on input field when page loads
 * Makes it easier for users to start typing immediately
 */
window.addEventListener('load', () => {
    messageInput.focus();
});

/*
================================================================================
HOW TO MODIFY THIS CODE:
================================================================================

1. CHANGE THE API ENDPOINT:
   If you move the backend or change the URL structure, update:
   const API_URL = 'http://localhost:8000/api/chatbot/';

2. ADD CONVERSATION HISTORY:
   Create an array to store messages:
   
   const conversationHistory = [];
   
   In sendMessage(), before the fetch:
   conversationHistory.push({role: 'user', content: userMessage});
   
   Then send the full history to the backend:
   body: JSON.stringify({
       message: userMessage,
       history: conversationHistory
   })

3. ADD MORE FEATURES:
   
   Clear Chat Button:
   function clearChat() {
       chatMessages.innerHTML = '';
       addMessage('Chat cleared. How can I help you?', 'bot');
   }
   
   Save Conversation:
   function saveConversation() {
       const messages = Array.from(chatMessages.children);
       const text = messages.map(msg => msg.textContent).join('\n');
       // Download or save to backend
   }
   
   Voice Input:
   Use Web Speech API:
   const recognition = new webkitSpeechRecognition();
   recognition.onresult = (event) => {
       messageInput.value = event.results[0][0].transcript;
   };

4. IMPROVE ERROR HANDLING:
   Add specific error messages for different scenarios:
   - Network offline
   - Server timeout
   - Invalid API response
   - Rate limiting

5. ADD AUTHENTICATION:
   If you implement user accounts, add auth token to requests:
   headers: {
       'Content-Type': 'application/json',
       'Authorization': `Bearer ${authToken}`
   }

================================================================================
CONNECTING TO DIFFERENT AI SERVICES:
================================================================================

The backend (Django) handles the actual AI integration.
This frontend just sends/receives messages.

To integrate different AI services, you only need to modify
the Django backend (backend/services/views.py).

Examples of what you can connect to:
- OpenAI GPT (ChatGPT)
- Google PaLM API
- Anthropic Claude
- Hugging Face models
- Custom trained models
- Rule-based systems

The frontend code stays the same regardless of which AI you use!

================================================================================
*/
