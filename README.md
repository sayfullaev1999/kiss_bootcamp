# KISS Bootcamp
## How to run?
### Step 1. Install pip first
```sh
sudo apt install python3-pip
```
### Step 2. Install virtual enviroment
```sh
sudo apt install python3-venv
````
### Step 3. Now create a virtual enviroment
```sh
python3 -m venv venv
```
### Step 4. Activate virtual enviroment 
```sh
source venv/bin/activate
```
### Step 5. Installing [all required packages][]
```sh
pip3 install -r requirements.txt
```
### Step 5. Create a .env file in your project directory

Add the following settings for the project there
```sh
# DJANGO Configuration
SECRET_KEY
DEBUG
IP
DOMAIN

# BOT configuration
PRODUCTION_TOKEN
LOCAL_TOKEN

# SMTP server configuration
EMAIL_HOST
EMAIL_PORT
EMAIL_USE_TLS
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD

# DB configuration
NAME_DB
USER_DB
PASSWORD_DB

# Social Media Login/Registeration
SOCIAL_AUTH_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET
SOCIAL_AUTH_GITHUB_KEY
SOCIAL_AUTH_GITHUB_SECRET
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
```
### Step 5. Create and save migration
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
### Step 5. Run server
```sh
python3 manage.py runserver
```

## Tech
* [Python3](https://python.org)
* [Django Framework](https://docs.djangoproject.com)
* [Django Rest Framework](https://docs.djangoproject.com)
* [Celery](https://git-scm.com/)
* [Redis](https://git-scm.com/)
* [Flower](https://git-scm.com/)
* [JavaScript](https://www.javascript.com/)
* [Bootstrap](https://getbootstrap.com/)
* [HTML](https://html.com)
* [Css](https://www.w3.org/Style/CSS/Overview.en.html)

[all required packages]: requirements.txt
