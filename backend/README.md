# How to run the project?
## 1. create and activate a virtual environment
1. Use `python3 --version` to check python3 version, I have Python 3.10.1
2. `python3.10 -m venv venv`
3. `source venv/bin/activate`
4. `export PYTHONPATH=$PWD` 

## 2. Install FastAPI, uvicorn, SQLAlchemy, Typing, Pydantic, databases (execute this step in the first time)
1. `pip install fastapi`
2. `pip install "uvicorn[standard]"`
3. `pip install sqlalchemy`
4. `pip install typing`
5. `pip install pydantic`
6. `pip install databases`
7. Uvicorn is an ASGI (Asynchronous Server Gateway Interface) compatible server that will be used for standing up the backend API.

## 3. Run the entry point file ('main.py' in this project)
1. `python main.py`

## 4. Check route at "http://localhost:8000/"

## 5. Check route at "http://localhost:8000/users"
    - Because in the api.py, I used `@app.get("/users", tags=["users"])`

## 6. Check out the interactive API documentation at "http://localhost:8000/docs" or "http://127.0.0.1:8000/docs"

## 7. Check out the alternative API documentation at "http://127.0.0.1:8000/redoc" 

## 8. Insert new data in app.db manually in the app.db console: 
1. Insert a new data into database:
    - `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('1','Leanne Graham','Bret','Sincere@april.biz','770-736-8031','hildegard.org');`
2. Delete a data from database: 
    - `Delete from users_react_fastAPI_table where id='1';` 
    
## 9. Add some tests to the project: 
1. Install pytest: `pip install pytest`
2. Install requests: `pip install requests`
3. Run: `pytest`
4. Follow the instructions: [https://fastapi.tiangolo.com/tutorial/testing/](https://fastapi.tiangolo.com/tutorial/testing/)