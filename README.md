# How to run this program?
1. In first Terminal (to run front-end): 
    1. Direct to folder "my-app"
    2. Run `npm start`
    3. Open [http://localhost:3000](http://localhost:3000) to view it in your browser
        - Before run back-end, you will get "Error!" message in the browser
2. In second Terminal (to run back-end):
    1. Direct to folder "backend"
    2. Run: 
        1. `source venv/bin/activate`
        2. `export PYTHONPATH=$PWD` 
        3. `python main.py` 
    3. Refresh [http://localhost:3000](http://localhost:3000) 
    4. To view it in your browser
        - Open [http://localhost:8000](http://localhost:8000) to see the main page
        - Open [http://localhost:8000/users](http://localhost:8000/users) to see the database in JSON
    5. To view the interactive API documentation: 
        - Open [http://localhost:8000/docs](http://localhost:8000/docs) or [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    6. To the alternative API documentation: 
        - Open [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 

# Some updates will be added to this project in the future:  
1. Add more tests in this project 
    - Unit tests, integration tests and system tests for front-end
    - API tests for backend
2. Update this project to a CRUD project (create, read, update, delete)
    - This project can only read data right now
    - I need to add some buttons that allow users can add/update/delete data
3. Design and update the table.css
    - This project is using the copy of css-style for the table from [https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy](https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy), right now 
4. Build some security stuff into this project

# Some sources that are used in this project: 
1. Front-end, REACT: 
    - [https://reactjs.org/](https://reactjs.org/) 
    - [https://reactjs.org/docs/faq-ajax.html](https://reactjs.org/docs/faq-ajax.html)
    - REACT-TABLE: [https://react-table.tanstack.com/](https://react-table.tanstack.com/) 
2. Back-end, Python: [https://www.python.org/](https://www.python.org/)
3. API, FastAPI: 
    - [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
    - [https://fastapi.tiangolo.com/tutorial/sql-databases/](https://fastapi.tiangolo.com/tutorial/sql-databases/) 
