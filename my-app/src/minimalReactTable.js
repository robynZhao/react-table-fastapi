import React, { useMemo, useState, useEffect } from 'react';
import './MinimalReactTable.css';
import Table from './table';

const MinimalReactTable =() => {
  // specify the column information with column attributes
  const columns = useMemo(() => [
      {
          Header: "React FastAPI Table",
          columns: [
              {
                  Header: "User Information",
                  columns: [
                      {
                          Header: 'User_Id',
                          accessor: 'id'
                      },
                      {
                          Header: 'User_Name',
                          accessor: 'username'
                      },
                      {
                          Header: 'Full_Name',
                          accessor: 'name'
                      }
                  ]
              },
              {
                  Header: "Contact Information",
                  columns: [
                      {
                          Header: 'User_Email',
                          accessor: 'email'
                      },
                      {
                          Header: 'User_Phone',
                          accessor: 'phone'
                      },
                      {
                          Header: 'User_Website',
                          accessor: 'website'
                      }
                  ]
              }
          ]
      }

    ], []
  );

  // console.log(columns);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // get data from "http://localhost:8000/users" which is created in api.py
  const fetchData = () => {
    return fetch("http://localhost:8000/users")
        .then((response) => {
          if (response.ok) {
            return response.json();
          }
          throw response;
        })
        .then((data) => setData(data))
        .catch((error) => {
          console.log(error);
          setError(error);
        })
        .finally(() => {
          setLoading(false);
        })
  };
  useEffect(() => {fetchData()}, []);
  if (loading) return "Loading";
  if (error) return "Error!";
  console.log(data);

  return (
      <div>
        <Table columns={columns} data={data} />
      </div>
  );
}

export default MinimalReactTable;
