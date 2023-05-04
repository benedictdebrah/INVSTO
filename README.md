## Project objective
#### This project aims to analyze data and create an investing/trading strategy for the data. The data is uploaded to a PostgreSQL database using Python.
<br>

#### 1. Uploading the data to the database, the following steps were taken:

- Created a PostgreSQL database on my local machine
- Installed the necessary packages, including psycopg2 and pandas
- Created a Python script to connect to the database and create a table with the appropriate columns and data types
- Read the data from an Excel file using pandas
- Inserted the data into the table using a for loop and SQL queries
- The Python script database.py contains the code for the above steps. (Before running the script, make sure to - modify the database connection parameters and file path to match the local setup ).
- Where this <b>pg_dump -h localhost -p 5432 -U postgres INVSTO > invsto_backup.sql</b> was used to get a backup for my database 


#### 2. Strategy and Backtesting
- Created a function for 8window and 21 window moving averages
- Function to check if the inputs are in the right datatype if not, the function makes the corrections
- Function to plot winning signals and loosing signals
- Created a streamlit app for frontend

#### How to use this app.
- Required columns format  'datetime','close','high','low','open','volume','instrument'
- For the datatypes there is a function that check datatypes validity (if not it makes the right changes provided the columns are in the right format.
- Compatible with excel files
- #### visit the link <a href='https://benedictdebrah-invsto-app-c0k8zb.streamlit.app/'>Demo</a>
