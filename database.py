import sqlite3

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('subscription.db')
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    try:
        sql_create_subscription_table = """ CREATE TABLE IF NOT EXISTS subscription (
                                            id integer PRIMARY KEY,
                                            email text NOT NULL
                                        ); """

        if conn is not None:
            c = conn.cursor()
            c.execute(sql_create_subscription_table)
        else:
            print("Error! cannot create the database connection.")
    except Error as e:
        print(e)

def add_subscription(conn, email):
    sql = ''' INSERT INTO subscription(email)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (email,))
    conn.commit()
    return cur.lastrowid

def main():
    database = create_connection()
    if database is not None:
        create_table(database)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
