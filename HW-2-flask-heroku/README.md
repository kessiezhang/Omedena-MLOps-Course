## Access Heroku API
https://bmi-calculator-heroku.herokuapp.com/

## Test
Input: height(inches), weight(pounds)
Output: BMI

## Result on LocalHost & Postman

**1. Local** <br>
<img width="619" alt="1  Test on Localhost" src="https://user-images.githubusercontent.com/44122973/147841845-8732d3fc-6fd7-4ed3-8ab0-2e56b8420a10.png">

**2. Postman**

<img width="633" alt="2  Test on Postman" src="https://user-images.githubusercontent.com/44122973/147841856-2426b1e5-097a-46d5-b054-6d7b137b4b0f.png">

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
$git commit -am "commit BMI_calculator app"
$heroku git:remote -a bmi-calculator-heroku
$git push heroku master
```
