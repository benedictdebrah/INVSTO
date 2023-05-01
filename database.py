import psycopg2
import pandas as pd

# set the database connection parameters
db_params = {
    'host': '-------',
    'port': '-----',
    'database': '-----',
    'user': '-----',
    'password': '----'
}

#connecting to my database
conn = psycopg2.connect(**db_params)

# create a cursor object
cursor = conn.cursor()

# defining the table name , column names and data types
table_name = 'hindalco'


columns = {
    'datetime': 'timestamp',
    'close': 'float',
    'high': 'float',
    'low': 'float',
    'open': 'float',
    'volume': 'int',
    'instrument': 'varchar'
}

# apply the data type replacements to the columns dictionary
replacements = {
    'datetime64': 'timestamp',
    'float64': 'float',
    'int64': 'int',
    'object': 'varchar'
}

for column_name in columns:
    data_type = columns[column_name]
    columns[column_name] = replacements.get(data_type, 'varchar')

# create the table in the database
create_table_sql = """
CREATE TABLE IF NOT EXISTS {} (
    {}
)
""".format(table_name, ',\n    '.join(['{} {}'.format(k, v) for k, v in columns.items()]))

try:
    cursor.execute(create_table_sql)
    print("Table created successfully.")
except Exception as e:
    print("Error creating table:", e)

# read the Excel file into a DataFrame
file_path = r'data\HINDALCO_1D.xlsx'
df = pd.read_excel(file_path)

# insert the data into the table
for i, row in df.iterrows():
    insert_sql = """
    INSERT INTO {} ({})
    VALUES ({})
    """.format(table_name, ', '.join(columns.keys()), ', '.join(['%s' for c in columns]))
    try:
        cursor.execute(insert_sql, tuple(row))
        print("Record inserted successfully.")
    except KeyError as e:
        print("Error inserting record:", e)

# commit the changes and close the connection
conn.commit()
conn.close()
