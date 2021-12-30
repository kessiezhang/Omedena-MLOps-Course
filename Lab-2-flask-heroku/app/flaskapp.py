from app.simpleInterest import simple_interest
from flask import Flask, jsonify, request

# instantiate flask object
# need to import this in __init__.py file
app = Flask('__name__')

@app.route('/', methods=['GET','POST'])
def get_input():
    """
    A function to get request using flask, 
    evluate and return result
    """
    packet = request.get_json(force=True)
    principal = packet['principal']
    rate = packet['rate']
    period = packet['period']
    
    interest = simple_interest(principal,rate,period)

    return jsonify(packet, interest)
