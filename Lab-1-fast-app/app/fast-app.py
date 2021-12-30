from simpleInterest import simple_interest
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def get_input(request:Request):
    getInput=await request.json()
    principal = getInput['principal']
    rate = getInput['rate']
    period = getInput['period']

    interest= simple_interest(principal,rate,period)

    return interest
    
# main driver app
if __name__ == '__main__':
    app.run()