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
`INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('1','Leanne Graham','Bret','Sincere@april.biz','770-736-8031','hildegard.org');`
 
 `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('2','Ervin Howell','Antonette','Shanna@melissa.tv','010-692-6593','anastasia.net');`
 
` INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('3','Clementine Bauch','Samantha','Nathan@yesenia.net','463-123-4447','kale.biz');`
 
 `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('4','Patricia Lebsack','Karianne','Julianne.OConner@kory.org','493-170-9623','demarco.info');`

 `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('5','Chelsey Dietrich','Kamren','Lucio_Hettinger@annie.ca','254-954-1289','ramiro.info');`

 `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('6','Mrs. Dennis Schulist','Leopoldo_Corkery','Karley_Dach@jasper.info','477-935-8478','ola.org');`
 
 `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('7','Kurtis Weissnat','Elwyn.Skiles','Telly.Hoeger@billy.biz','210-067-6132','elvis.io');`
 
 `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('8','Nicholas Runolfsdottir V','Maxime_Nienow','Sherwood@rosamond.me','586-493-6943','jacynthe.com');`
 
 `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('9','Glenna Reichert','Delphine','Chaim_McDermott@dana.io','775-976-6794','conrad.com');`
 
 `INSERT INTO users_react_fastAPI_table (id, name, username, email, phone, website)
 VALUES ('10','Clementina DuBuque','Moriah.Stanton','Rey.Padberg@karina.biz','024-648-3804','ambrose.net');`