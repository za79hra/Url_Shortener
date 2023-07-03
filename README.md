# URL Shortener App

The URL Shortener App is a Django-based web application that allows users to shorten long URLs and redirect visitors to the original links. The app provides user authentication using JWT tokens and utilizes Redis for caching one-time passwords (OTP).

## Features

- User authentication with JWT tokens
- Generating and validating one-time passwords (OTP) for phone number verification
- Shortening long URLs and creating unique short links
- Tracking the number of times each shortened link is viewed
- Redirection from the short link to the original URL

## Installation and Setup

### Prerequisites

- Python (version 3.6 or higher)
- Django (version 3.0 or higher)
- Redis (version 3.0 or higher)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/url-shortener-app.git


1.Change into the project directory:
```bash
cd url-shortener-app
```
2.Install the required dependencies:
```bash
pip install -r requirements.txt
```
3.Configure the database settings in the settings.py file.

4.Apply the database migrations:
```bash
python manage.py migrate
```
5.Start the Django development server:
```bash
python manage.py runserver
```
6. The app should now be running on http://localhost:8000.


**Usage**:



Open a web browser and go to http://localhost:8000/login to access the login page.

Enter your phone number and click on the Send OTP button to receive a one-time password via SMS.

Enter the OTP in the provided field and click on the Verify button to log in and receive your access and refresh tokens.

Use the access token in the authorization header (Authorization: Bearer <access_token>) for authenticated API requests.

To shorten a URL, make a POST request to /shorten/ with the original URL in the request body.

To view all shortened links, make a GET request to /shortened-links/.

To redirect visitors to the original URL, use the short link in the format http://localhost:8000/<short_url>.



API Endpoints:




-POST /login/: Send a one-time password (OTP) to the provided phone number for authentication.
-POST /verify/: Verify the OTP and retrieve access and refresh tokens.
-POST /refresh/: Refresh the access token using the refresh token.
-POST /shorten/: Shorten a long URL and create a unique short link.
-GET /shortened-links/: Get a list of all shortened links.
-GET /<short_url>/: Redirect visitors to the original URL associated with the short link.


Note:


Make sure to update the Redis connection details in the views.py file with your Redis configuration (host, port, etc.):
```bash
redis_connection = Redis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)
```
This README is a basic template. Feel free to add more details about the app, usage examples, and any other relevant information.


Contributing:

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License:



The URL Shortener App is open-source software licensed under the MIT License.
```bash

Feel free to customize the content based on your specific project details and requirements.
```
