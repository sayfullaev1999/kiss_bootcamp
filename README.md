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
> #Telegram bot configuration  

> PRODUCTION_TOKEN = `YOUR PRODUCTION TOKEN TELEGRAM BOT`  

> LOCAL_TOKEN = `YOUR LOCAL TOKEN TELEGRAM BOT`  

> #Smtp configuration  

> EMAIL_HOST = `smtp.email-domain.com`  

> EMAIL_PORT = `587`  

> EMAIL_USE_TLS = `True`  

> EMAIL_HOST_USER = `yourusername@youremail.com`  

> EMAIL_HOST_PASSWORD = `your_password`  

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
* [Git](https://git-scm.com/)
* [JavaScript](https://www.javascript.com/)
* [Bootstrap](https://getbootstrap.com/)
* [HTML](https://html.com)
* [Css](https://www.w3.org/Style/CSS/Overview.en.html)

[all required packages]: requirements.txt
