## Access Heroku API
http://solar-app-kz.herokuapp.com

## Test
Input: "month", "day", "Daily_Temp", "Daily_Precip", "Daily_Humidity", "Daily_Pressure", "Daily_WindDir",
"Daily_WindSpeed", "Daily_DNI", "Daily_DHI"
Output: Average Solar Irradiance

## Result on LocalHost & Postman

**1. Local: http://127.0.0.1:8000** <br>
<img width="670" alt="1  Postman Local Test" src="https://user-images.githubusercontent.com/44122973/149857320-9b8bf4a1-c4a5-487a-b7c0-3e8b1b56423d.png">

**2. Postman**
<img width="586" alt="2  Deployed on Heroku" src="https://user-images.githubusercontent.com/44122973/149857341-06a150b2-0897-4f39-abb8-dbd1559a67be.png">


## Step by Step Command Line
```terminal
$python -m venv venv
$pip install flask
$pip install gunicorn
$pip install heroku
$touch Procfile
$pip freeze >requirements.txt
$python __init__.py

$heroku login -i
$git init
$git add .
$git commit -am "commit solar app"
$heroku git:remote -a solar-app-kz-heroku
$git push heroku master
```
