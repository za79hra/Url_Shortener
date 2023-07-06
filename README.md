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
- PostgreSQL
### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/za79hra/Url_Shortener/


1.Change into the project directory:
```bash
cd Url-Shortener
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

# **Configuration**
Ensure that the following environment variables are properly configured:

- REDIS_HOST: Redis database host (default: redis)
- POSTGRES_DB: PostgreSQL database name (default: postgres)
- POSTGRES_USER: PostgreSQL database username (default: postgres)
- POSTGRES_PASSWORD: PostgreSQL database password (default: mypass)

# **Usage**:

Open a web browser and go to http://localhost:8000/login to access the login page.

Enter your phone number and click on the Send OTP button to receive a one-time password via SMS.

Enter the OTP in the provided field and click on the Verify button to log in and receive your access and refresh tokens.

Use the access token in the authorization header (Authorization: Bearer <access_token>) for authenticated API requests.

To shorten a URL, make a POST request to /shorten/ with the original URL in the request body.

To view all shortened links, make a GET request to /shortened-links/.

To redirect visitors to the original URL, use the short link in the format http://localhost:8000/<short_url>.



# **API Endpoints**:

**Send One-Time Password**

- URL: /login/

- Method: POST

- Description: Sends a one-time password (OTP) to the provided phone number for   authentication.

- Request Body:
```bash
{
  "phone_number": "09123456789"
}
```


**Verify One-Time Password**

- URL: /verify/

- Method: POST

- Description: Verifies the provided OTP and returns access and refresh tokens for authentication.

- Request Body:
```bash
{
  "phone_number": "09123456789",
  "otp": "1234"
}
```

**Shorten URL**

- URL: /shorten/

- Method: POST

- Description: Shortens a given long URL and returns the shortened URL.

- Request Body:
```bash
{
  "orginal_url": "https://example.com/long-url"
}
```
**Redirect to Long URL**

URL: /<str:short_url>/
- Method: GET
- Description: Redirects to the original long URL associated with the provided short URL.


**Get All Shortened Links**

- URL: /shortened-links/
- Method: GET
- Description: Retrieves all the shortened links created by the authenticated user.


# **Note**:


Make sure to update the Redis connection details in the views.py file with your Redis configuration (host, port, etc.):
```bash
redis_connection = Redis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)
```
This README is a basic template. Feel free to add more details about the app, usage examples, and any other relevant information.


### **Docker Configuration**
To run the application using Docker, make sure you have Docker installed on your machine. Follow these steps:

1 Install Docker and Docker Compose if you haven't already.

2 Create a docker-compose.yml file with the following content:
```bash
version: '3'
services:
  app:
    build: .
    command: sh -c "gunicorn --bind 0.0.0.0:8000 Url_shortener.wsgi"
    ports:
      - 8000:8000
    volumes:
      - .:/app
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis

  redis:
    container_name: redis
    image: redis:latest
    expose:
      - 6379

  db:
    container_name: postgres
    image: postgres:latest
    expose:
      - 5432
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=mypass

volumes:
  postgres_data:
```
3 Run the following command to start the application:
```bash
docker-compose up --build
```
The application will be accessible at http://localhost:8000.


