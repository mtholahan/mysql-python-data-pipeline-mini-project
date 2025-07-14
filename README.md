# 🎟️ Event Ticket System – Data Pipeline Mini-Project

This project simulates a real-world ticketing system that processes third-party ticket sales via CSV. The goal is to practice using Python and SQL to build a simple but complete data pipeline using MySQL.

## 📁 Project Structure

```
.
├── create_ticketsales_table.sql    # Create table DDL
├── event_ticket_system.py          # Main script with all 3 pipeline steps
├── README.md
├── run_log.txt                     # Saved CLI output from a successful run
├── third_party_sales_1.csv         # Input CSV file with sales data


## 🚀 How to Run This Project

### 🔧 1. Prerequisites

- Python 3.x
- MySQL Server (running locally)
- MySQL user with access to a schema called `event_ticket_system`
- `mysql-connector-python` package:

```bash
pip install mysql-connector-python
```

### 🛠️ 2. Set Up the MySQL Table (see third_party_sales_1.csv)

Connect to MySQL and run:

```sql
USE event_ticket_system;

CREATE TABLE IF NOT EXISTS ticketsales (
    ticket_id int,
    trans_date date,
    event_id int,
    event_name varchar(50),
    event_date date,
    event_type varchar(10),
    event_city varchar(20),
    customer_id int,
    price decimal,
    num_tickets int
);
```

### 🐍 3. Run the Python Pipeline

Make sure to update your MySQL credentials in `get_db_connection()` inside the script.

```bash
python event_ticket_system.py
```

## ⚙️ What the Script Does

1. **Connects to the MySQL database** using the provided credentials.
2. **Reads a third-party CSV file** and parses the `trans_date` and `event_date` values into proper `DATE` objects.
3. **Inserts all records** into the `ticketsales` table.
4. **Queries and prints the top 5 most popular events** by total ticket sales.

## ✅ Sample Output

```
Most Popular Events:
- Rock Concert (120 tickets sold)
- Auto Show (80 tickets sold)
- Jazz Festival (75 tickets sold)
...
```

## 📝 How to Verify It Worked

- Run the Python script and confirm there are no errors.
- Inspect the database: `SELECT * FROM ticketsales;`
- Ensure dates were parsed correctly, and all rows were loaded.
- Validate that popular event names are printed as expected.

## 📎 Notes

- You can easily swap in another CSV file by changing the filename in `load_third_party()` call at the bottom of the script.
- A successful run log is included in `run_log.txt` per submission requirements.

## 📌 Author

Mark Holahan  
Boot Camp: Springboard Data Engineering  
Instructor: Akhil