/*
================================================================================
MAIN APPLICATION JAVASCRIPT
================================================================================
This file contains shared JavaScript functions used across multiple pages.
*/

/**
 * Navigate to a service page
 * Called when a service button is clicked on the homepage
 * 
 * @param {string} page - The filename of the page to open (e.g., 'chatbot.html')
 */
function openService(page) {
    window.location.href = page;
}

/**
 * Show "coming soon" alert for placeholder services
 * This is used for services that aren't implemented yet
 * 
 * @param {string} serviceName - Name of the service
 */
function showComingSoon(serviceName) {
    alert(`${serviceName} is coming soon!\n\nTo implement this service:\n1. Create the frontend page in /frontend\n2. Add backend logic in /backend/services/views.py\n3. Register the API endpoint in /backend/services/urls.py\n4. Update the button to link to your new page`);
}

/**
 * Go back to homepage
 * Used by the back button on service pages
 */
function goHome() {
    window.location.href = 'index.html';
}

/*
================================================================================
HOW TO ADD COMMON FUNCTIONS:
================================================================================

If you have JavaScript code that's used across multiple service pages,
add it here as a function.

Examples:
- API error handling
- User authentication
- Common UI components
- Utility functions (date formatting, validation, etc.)

Then include this file in your HTML pages with:
<script src="app.js"></script>
================================================================================
*/
