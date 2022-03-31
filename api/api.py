from fastapi import FastAPI
from api.responses import CustomJSONResponse

app = FastAPI(
    default_response_class=CustomJSONResponse,
)


@app.get('/')
async def test_view():
    return {
        'MyDICT': True,
    }


@app.get('/sec')
async def sec_view():
    return {
        'OK-200': True,
    }
