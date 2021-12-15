from simpleInterest import simple_interest
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def get_input(request:Request):
    packet = await request.json()
    principal = packet['principal']
    rate = packet['rate']
    period = packet['period']

    interest= simple_interest(principal,rate,period)

    return jsonify(packet,interest)
    
# fast-api doesn't need driver function here