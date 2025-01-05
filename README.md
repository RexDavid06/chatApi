Chat API with JWT Authentication
This is a simple Django-based API for a chat application that uses JWT (JSON Web Tokens) for authentication. Users can register, log in, check their token balance, and chat with a basic AI response system. The API ensures that only authenticated users can interact with the chat system.

Features
User Registration: Users can register with a username and password.
Login: Users can log in using their credentials to receive a JWT access token and refresh token.
Chat: Authenticated users can send messages to the chat API, which returns a dummy AI response. Each message costs tokens, and the user’s token balance is updated accordingly.
Token Balance: Users can check their token balance after logging in.
Technologies Used
Django (Backend)
Django REST Framework (API framework)
Django REST Framework SimpleJWT (JWT Authentication)
SQLite (Database for development)
Installation
To run this project locally, follow the steps below:

1. Clone the Repository
git clone https://github.com/your-repository/chat-api.git
cd chat-api
2. Create a Virtual Environment (Recommended)
3. Install Dependencies
Install the required Python libraries:
pip install -r requirements.txt
4. Apply Migrations
Make sure your database is set up:
python manage.py migrate
5. Create a Superuser (Optional)
If you want to access the Django admin interface, create a superuser:
python manage.py createsuperuser
6. Run the Server
Start the development server:
python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

Endpoints
1. Register User
POST /register/

Request body:
json
Copy code
{
  "username": "user123",
  "password": "password123"
}
Response:
json
Copy code
{
  "message": "You've been registered"
}
2. Login User
POST /login/

Request body:
json
Copy code
{
  "username": "user123",
  "password": "password123"
}
Response:
json
Copy code
{
  "user": "user123",
  "access_token": "access_token_string",
  "refresh_token": "refresh_token_string"
}
3. Get Token Balance
GET /token_balance/

Headers:
Authorization: Bearer <access_token>
Response:
json
Copy code
{
  "tokens": 100
}
4. Chat
POST /chatView/

Headers:
Authorization: Bearer <access_token>
Request body:
json
Copy code
{
  "message": "Hello, AI!"
}
Response:
json
Copy code
{
  "user": "user123",
  "message": "Hello, AI!",
  "response": "Dummy Response"
}
Authentication
JWT Authentication
When a user logs in, they receive two tokens:
Access Token: This is used to authenticate the user for a limited period of time (default 5 minutes).
Refresh Token: This is used to get a new access token when the original access token expires.
You can use the access_token in the Authorization header to make authenticated requests:

text
Copy code
Authorization: Bearer <access_token>
If your access token expires, use the refresh_token to get a new access token by calling the /token/refresh/ endpoint.

Token Expiry & Refresh
Once the access token expires, the user can request a new one using the refresh token: POST /token/refresh/

Request body:
json
Copy code
{
  "refresh": "refresh_token_string"
}
Response:
json
Copy code
{
  "access_token": "new_access_token_string"
}
Requirements
Python 3.10 or higher
Django 5.1.2
Django REST Framework
Django REST Framework SimpleJWT
