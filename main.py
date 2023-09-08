from fastapi import FastAPI
from eletronicos import eletronicos_list

app = FastAPI()



@app.get('/')
async def root():
    return {'message':'hello'}

@app.get('/get-items')
async def get_items():
    data = eletronicos_list
    if data:
        return {'status':'success','data':data}

@app.get('/get-product/{product}')
async def get_product(product:str):
    for item in eletronicos_list:
        if item["nome"] == product:
            return {'status':'success','data':[item]}
    return {'status':'success','message':'Item não encontrado'}

@app.get('/get-price/{product}')
async def get_price(product:str):
    for item in eletronicos_list:
        if item["nome"] == product:         
            return {'status':'success','data':[item['preco']]}
    return {'status':'success','message':'Preco não encontrado'}