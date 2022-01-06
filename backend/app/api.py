# bring all the modular components together
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas
from . import crud
from .database import SessionLocal, engine

# to create models in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Why we use CORSMiddleware here?
# In order to make cross-origin requests
# e.g., requests that originate from a different protocol, IP address, domain name, or port
#       you need to enable Cross Origin Resource Sharing (CORS)
# FastAPI's built-in CORSMiddleware handles this for us
# It allows cross-origin requests from our frontend domain and port which will run at localhost:3000
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def read_root() -> dict:
    return "Welcome to my minimal React application!"

# fake data to test if the front-end can show correct data
# users = [
#     {
#         "id": 1,
#         "name": "Leanne Graham",
#         "username": "Bret",
#         "email": "Sincere@april.biz",
#         "phone": "770-736-8031",
#         "website": "hildegard.org",
#     },
#     {
#         "id": 2,
#         "name": "Ervin Howell",
#         "username": "Antonette",
#         "email": "Shanna@melissa.tv",
#         "phone": "010-692-6593",
#         "website": "anastasia.net",
#     },
#     {
#         "id": 3,
#         "name": "Clementine Bauch",
#         "username": "Samantha",
#         "email": "Nathan@yesenia.net",
#         "phone": "463-123-4447",
#         "website": "kale.biz",
#     },
#     {
#         "id": 4,
#         "name": "Patricia Lebsack",
#         "username": "Karianne",
#         "email": "Julianne.OConner@kory.org",
#         "phone": "493-170-9623",
#         "website": "demarco.info",
#     },
#     {
#         "id": 5,
#         "name": "Chelsey Dietrich",
#         "username": "Kamren",
#         "email": "Lucio_Hettinger@annie.ca",
#         "phone": "254-954-1289",
#         "website": "ramiro.info",
#     },
#     {
#         "id": 6,
#         "name": "Mrs. Dennis Schulist",
#         "username": "Leopoldo_Corkery",
#         "email": "Karley_Dach@jasper.info",
#         "phone": "477-935-8478",
#         "website": "ola.org",
#     },
#     {
#         "id": 7,
#         "name": "Kurtis Weissnat",
#         "username": "Elwyn.Skiles",
#         "email": "Telly.Hoeger@billy.biz",
#         "phone": "210-067-6132",
#         "website": "elvis.io",
#     },
#     {
#         "id": 8,
#         "name": "Nicholas Runolfsdottir V",
#         "username": "Maxime_Nienow",
#         "email": "Sherwood@rosamond.me",
#         "phone": "586-493-6943",
#         "website": "jacynthe.com",
#     },
#     {
#         "id": 9,
#         "name": "Glenna Reichert",
#         "username": "Delphine",
#         "email": "Chaim_McDermott@dana.io",
#         "phone": "775-976-6794",
#         "website": "conrad.com",
#     },
#     {
#         "id": 10,
#         "name": "Clementina DuBuque",
#         "username": "Moriah.Stanton",
#         "email": "Rey.Padberg@karina.biz",
#         "phone": "024-648-3804",
#         "website": "ambrose.net",
#     }
# ]

# use fake data to test
# need to update "data.users" in minimalReactTable.js, when fetch the data
# @app.get("/users", tags=["users"])
# async def get_users() -> dict:
#     return { "users": users }

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


