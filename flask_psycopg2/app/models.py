import psycopg2
# connection parameters
host = 'localhost'
port = '5432'
database = "flask_db"
user = "postgres"
password = "postgres"

conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    database = database,
    password=password,
)

# we open a cursor to perform databse operations
cur = conn.cursor()

# execute a command
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books('
            'id serial PRIMARY KEY,'
            'title varchar (150) NOT NULL,'
            'author varchar (50) NOT NULL,'
            'pages_num integer NOT NULL,'
            'review text,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

# insert data into the table
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A tale of Two cities',
             'Charles Dickens',
             489,
             'A great classic')
            )

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic')
            )
#commit the transaction
conn.commit()

#close the connection
cur.close()
conn.close()
