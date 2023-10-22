from fastapi import FastAPI
import uvicorn
from controllers import  auth_controller

app = FastAPI()

app.include_router(auth_controller.router)


if __name__ == '__main__': #ee helvetti
    uvicorn.run('main:app', port=8002, reload=False)
