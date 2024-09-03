import json
import psycopg2

# Path to the JSON file
json_file_path = '5yrs_Transaction.json'

# Load the JSON data
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Define connection parameters
conn_params = {
    'dbname': 'exec_condo_db',
    'user': 'postgres',
    'password': '*********',
    'host': '127.0.0.1',
    'port': '5432'
}

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**conn_params)
    print("Connection successful!")
except psycopg2.Error as e:
    print("Error occurred while connecting to the database:", e)
    raise SystemExit(e)

cursor = conn.cursor()

# Create tables
create_transactions_table_sql = """
CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    street VARCHAR(255),
    x NUMERIC,
    y NUMERIC,
    project VARCHAR(255),
    market_segment VARCHAR(255)
);
"""

create_transaction_details_table_sql = """
CREATE TABLE IF NOT EXISTS transaction_details (
    id SERIAL PRIMARY KEY,
    transaction_id INTEGER REFERENCES transactions(id),
    area NUMERIC,
    floor_range VARCHAR(50),
    no_of_units INTEGER,
    contract_date VARCHAR(50),
    type_of_sale VARCHAR(50),
    price NUMERIC,
    property_type VARCHAR(255),
    district VARCHAR(50),
    type_of_area VARCHAR(50),
    tenure VARCHAR(50)
);
"""

# Execute table creation
try:
    cursor.execute(create_transactions_table_sql)
    cursor.execute(create_transaction_details_table_sql)
    conn.commit()
    print("Tables created successfully!")
except psycopg2.Error as e:
    print("Error occurred while creating tables:", e)

# Insert data into tables
insert_transaction_sql = """
INSERT INTO transactions (street, x, y, project, market_segment)
VALUES (%s, %s, %s, %s, %s) RETURNING id
"""

insert_transaction_details_sql = """
INSERT INTO transaction_details (transaction_id, area, floor_range, no_of_units, contract_date, type_of_sale, price, property_type, district, type_of_area, tenure)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

try:
    for record in data['Result']:
        # Insert into transactions table
        transaction_values = (
            record.get('street', None),
            record.get('x', None),
            record.get('y', None),
            record.get('project', None),
            record.get('marketSegment', None)
        )
        cursor.execute(insert_transaction_sql, transaction_values)
        transaction_id = cursor.fetchone()[0]  # Get the id of the inserted record

        # Insert into transaction_details table
        for transaction in record.get('transaction', []):
            transaction_details_values = (
                transaction_id,
                transaction.get('area', None),
                transaction.get('floorRange', None),
                transaction.get('noOfUnits', None),
                transaction.get('contractDate', None),
                transaction.get('typeOfSale', None),
                transaction.get('price', None),
                transaction.get('propertyType', None),
                transaction.get('district', None),
                transaction.get('typeOfArea', None),
                transaction.get('tenure', None)
            )
            cursor.execute(insert_transaction_details_sql, transaction_details_values)

    conn.commit()
    print("Data inserted successfully!")
except psycopg2.Error as e:
    print("Error occurred while inserting data:", e)
finally:
    cursor.close()
    conn.close()
