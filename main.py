from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {'data': {'message': 'Hello, World!'}}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {'data': {'item_id': item_id, 'query': q}}
