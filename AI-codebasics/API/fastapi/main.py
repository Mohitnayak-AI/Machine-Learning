from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/hello/{name}')
def hello(name):
    return f"hello {name}"

@app.get('/hello')
def hello():
    return "hello Mohit"

food_items = {
    'indian' : ['samosa','Dosa'],
    'american' : ['Hot Dogs','Apple pie'],
    'italian' : ['Ravioli','pizza']
}

# @app.get("/get_items/{cuisine}")
# def get_items(cuisine):
#     items = food_items.get(cuisine)
#     if not items:
#         return f"{cuisine} is not in the item list"
#     return food_items.get(cuisine)

class AvailableCuisines(str,Enum):
    indian = "indian"
    american = "american"
    italian = "italian"
    
@app.get("/get_items/{cuisine}")
def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code:int):
    return {'discount_amount': coupon_code.get(code)}

@app.get('/')
def hello():
    return "hello"