README: Django Chat API with Token Authentication
Project Overview
This project is a simple REST API built using Django and Django Rest Framework (DRF) for handling user authentication and chat functionalities. The key features include user registration, login with JWT token generation, AI-generated dummy responses to user messages, and token-based rate limiting. Users are required to have a certain number of tokens in their account to interact with the chat API. Each message sent deducts tokens from the user's account.

Features
User Registration: Users can register with a username and password.
Login and JWT Tokens: After registration, users can log in to receive JWT tokens for authentication in future requests.
AI-Generated Chat Responses: Users can send messages and receive dummy AI responses.
Token Deduction for Chats: Every message sent by the user deducts 100 tokens from their account. Users must have sufficient tokens to send a message.
Token Balance API: An API endpoint to check the remaining token balance of the user.
Installation Instructions
Prerequisites
Python 3.10+
pip (Python package manager)
SQLite (default Django database)
Steps to Set Up
Clone the Repository:

bash
Copy code
git clone https://github.com/your-repo/django-chat-api.git
cd django-chat-api
Set Up a Virtual Environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Run Database Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser (Admin for Django Admin Panel):

bash
Copy code
python manage.py createsuperuser
Run the Server:

bash
Copy code
python manage.py runserver
The API will be available at: http://127.0.0.1:8000/.

Requirements File
If you need to generate a requirements.txt file, use the command:

bash
Copy code
pip freeze > requirements.txt
API Endpoints
1. User Registration
Endpoint: /register/
Method: POST
Description: Registers a new user with a username and password. It automatically assigns 4000 tokens to the user.

Request Example:

json
Copy code
{
  "username": "john_doe",
  "password": "password123"
}
Response Example:

json
Copy code
{
  "message": "You've been registered"
}
2. User Login
Endpoint: /login/
Method: POST
Description: Logs in a registered user and returns JWT access and refresh tokens.

Request Example:

json
Copy code
{
  "username": "john_doe",
  "password": "password123"
}
Response Example:

json
Copy code
{
  "user": "john_doe",
  "access_token": "your_jwt_access_token",
  "refresh_token": "your_jwt_refresh_token"
}
3. Chat Endpoint
Endpoint: /chatView/
Method: POST
Description: Accepts user messages and returns dummy AI responses. Requires authentication. Each request deducts 100 tokens from the user.

Request Headers:

http
Copy code
Authorization: Token <your_jwt_access_token>
Request Example:

json
Copy code
{
  "message": "Hello, how are you?"
}
Response Example:

json
Copy code
{
  "user": 1,
  "message": "Hello, how are you?",
  "response": "Dummy response based on your message",
  "timestamp": "2025-01-01T12:00:00Z"
}
4. Check Token Balance
Endpoint: /token_balance/
Method: GET
Description: Returns the current token balance of the authenticated user.

Request Headers:

http
Copy code
Authorization: Token <your_jwt_access_token>
Response Example:

json
Copy code
{
  "tokens": 3900
}
5. Token Refresh
Endpoint: /token/refresh/
Method: POST
Description: Refreshes the JWT access token using the refresh token.

Request Example:

json
Copy code
{
  "refresh": "your_jwt_refresh_token"
}
Response Example:

json
Copy code
{
  "access_token": "your_new_jwt_access_token"
}
Usage Guidelines
User Registration: Users need to register via the /register/ endpoint before accessing any other part of the API.
Authentication: After logging in via the /login/ endpoint, include the access_token in the Authorization header for all authenticated requests. Use the format Authorization: Token <your_access_token>.
Token Deduction: Every time a user interacts with the chat API (/chatView/), 100 tokens are deducted from their account. Make sure the user has sufficient tokens before sending a request.
Admin Panel
To access the Django admin panel, visit http://127.0.0.1:8000/admin/ and log in using the superuser account you created during setup. From there, you can manage users and view chat history.

Technologies Used
Django: A high-level Python web framework.
Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs in Django.
SQLite: The default Django database for local development.
Security
JWT (JSON Web Tokens): For authentication and maintaining user sessions.
Token Deduction: Users are only allowed to interact with the chat API if they have sufficient tokens. The token deduction system ensures controlled access to the API.
Conclusion
This Django REST API provides a basic structure for user management, token-based authentication, and token-regulated access to chat services. It's extendable, so you can replace the dummy AI response with actual AI-generated content or integrate more complex token management systems.

Feel free to expand the functionality, enhance security, or connect to a more robust database if necessary!
