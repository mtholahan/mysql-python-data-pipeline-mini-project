import mysql.connector
import csv
from datetime import datetime

FILE_PATH = r"C:\Projects\mysql-python-data-pipeline-mini-project\third_party_sales_1.csv"

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
        user='mholahan',
        password='Certified5-Distract5',
        host='localhost',
        port='3306',
        database='event_ticket_system')
    except Exception as error:
        print("Error while connecting to database for ticket sales.", error)
    return connection

def clear_table(connection):
    cursor = connection.cursor()
    cursor.execute("""TRUNCATE TABLE ticketsales;""")
    connection.commit()
    cursor.close()

def load_third_party(connection, file_path_csv):
    cursor = connection.cursor()
    try:
        with open(file_path_csv, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                # Fix trans_date (index 1) and event_date (index 4)
                row[1] = datetime.strptime(row[1], '%m/%d/%Y').date().isoformat()
                row[4] = datetime.strptime(row[4], '%m/%d/%Y').date().isoformat()

                cursor.execute("""
                    INSERT INTO ticketsales 
                    (ticket_id, trans_date, event_id, event_name, event_date,
                    event_type, event_city, customer_id, price, num_tickets)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, row)
        connection.commit()
    except Exception as e:
        print("Error while loading thrid-party data:", e)
        connection.rollback()
    finally:
        cursor.close()

def query_popular_tickets(connection):
    # Get the most popular ticket in the past month
    sql_statement = """
    WITH CTE
    AS
    (
        SELECT 
            t.event_id, t.event_name, SUM(t.num_tickets) as TicketSales
        FROM ticketsales t
        WHERE
            YEAR(t.trans_date) >= YEAR(t.trans_date - INTERVAL 1 MONTH) 
        AND 
            MONTH(t.trans_date) >= MONTH(t.trans_date - INTERVAL 1 MONTH)
        GROUP BY t.event_id, t.event_name
        
    )

    SELECT CTE.event_name, CTE.TicketSales
    FROM CTE
    ORDER BY CTE.TicketSales DESC
    LIMIT 5;
    """
    cursor = connection.cursor()
    try:
        cursor.execute(sql_statement)
        records = cursor.fetchall()
        return records   
    except Exception as e:
        print("Error while querying popular tickets:", e)
        return []
    finally:
        cursor.close()


# === Main ===
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        clear_table(conn)
        load_third_party(conn, FILE_PATH)
        popular = query_popular_tickets(conn)
        print("May we recommend the past months' top-selling events:")
        for row in popular:
            print(f"- {row[0]} ({row[1]} tickets sold)") # type: ignore
        conn.close