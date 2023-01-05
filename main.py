from fastapi import FastAPI
from routers import langs, versions, datablocks, dictionar, lists
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from starlette.responses import FileResponse 


   

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(langs.router, tags=["langs"])
app.include_router(versions.router, tags=["versions"])
app.include_router(datablocks.router, tags=["datablocks"])
app.include_router(dictionar.router, tags=["dictionaries"])
app.include_router(lists.router, tags=["lists"])




class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 404:
            response = await super().get_response('.', scope)
        return response

#app.mount('/', SPAStaticFiles(directory='build/', html=True), name='spa')

#app.mount("/", StaticFiles(directory="build", html=True), name="static")


# uvicorn main:app --reload
#if __name__ == "__main__": 
#    uvicorn.run(app, host="0.0.0.0", workers=1, port=8000)