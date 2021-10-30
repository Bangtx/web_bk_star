from fastapi import *

api = FastAPI()

@api.get('/')
def hello():
    return '<h1>hello</h1>'