# main.py
import os
from fastapi import FastAPI
from mangum import Mangum

STAGE = os.environ.get('STAGE')
root_path = '/' if not STAGE else f'/{STAGE}'
app = FastAPI(title="Variants", root_path=root_path)
@app.get('/hello')
def hello_api(name: str = "World"):
    return {"hello": name}

@app.get(app.root_path + "/openapi.json", include_in_schema=False)
def custom_swagger_ui_html():
    return app.openapi()

# Mangum Handler, this is so important
handler = Mangum(app)
