from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users, address
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# the above line creates everything from database.py and models.py file

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return RedirectResponse(url="todos", status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(address.router)
