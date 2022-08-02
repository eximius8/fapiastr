from fastapi import FastAPI
from routers import langs, versions, datablocks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(langs.router)
app.include_router(versions.router)
app.include_router(datablocks.router)




class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 404:
            response = await super().get_response('.', scope)
        return response

app.mount('/', SPAStaticFiles(directory='astraia-db-front/build/', html=True), name='whatever')


# uvicorn main:app --reload
if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", workers=1, port=8000)