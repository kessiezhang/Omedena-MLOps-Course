from app.BMI_calculator import bmi_calculator
from flask import Flask, jsonify, request

app = Flask('__name__')
@app.route('/', methods=['GET','POST'])
def get_input():
    """
    A function to get request using flask and return BMI
    """
    packet = request.get_json(force=True)
    weight = packet['weight']
    height = packet['height']
    bmi = bmi_calculator(weight, height)
    return jsonify(packet,bmi)
