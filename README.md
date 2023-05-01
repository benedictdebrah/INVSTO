## Project objective
#### This project aims to analyze data and create an investing/trading strategy for the data. The data is uploaded to a PostgreSQL database using Python.
<br>

#### 1. To upload the data to the database, the following steps were taken:

- Created a PostgreSQL database on my local machine
- Installed the necessary packages, including psycopg2 and pandas
- Created a Python script to connect to the database and create a table with the appropriate columns and data types
- Read the data from an Excel file using pandas
- Inserted the data into the table using a for loop and SQL queries
- The Python script database.py contains the code for the above steps. (Before running the script, make sure to - modify the database connection parameters and file path to match the local setup ).
- Where this <b>pg_dump -h localhost -p 5432 -U postgres INVSTO > invsto_backup.sql</b> was used to get a backup for my database 


#### 2. Analysis of the dataset