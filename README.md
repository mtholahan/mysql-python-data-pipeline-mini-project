# MySQL Python Data Pipeline Mini Project


## 📖 Abstract
This project develops a basic data pipeline for an event ticketing system, integrating CSV-based vendor feeds with a relational database. The system simulates how major ticket platforms manage direct ticket sales alongside third-party reseller submissions.

The workflow includes:

* Designing and creating a sales table in MySQL with fields for ticket, customer, event, and purchase details.

* Using Python’s MySQL connector to establish database connections and ingest new sales records from daily CSV submissions.

* Implementing a loader function to iterate through CSV rows and insert them into the database table.

* Running SQL queries to generate statistical insights, such as identifying the most popular events in the past month based on ticket volume.

* Formatting query results into human-readable output, e.g., "The North American International Auto Show" as a top-selling event.

Deliverables include Python code, the sales table definition, ingestion logic, and example query results. Through this project, I gained practice in Python-MySQL integration, database schema creation, batch CSV ingestion, and SQL-based analytics, building foundational ETL pipeline skills.



## 🛠 Requirements
- Python 3.8+
- MySQL Server running locally or remote
- mysql-connector-python package
- Provided ticket_sales.csv dataset
- GitHub repo for code + logs submission



## 🧰 Setup
- Install mysql-connector-python (pip install mysql-connector-python)
- Create a MySQL database (e.g., ticketdb)
- Define and create sales table per schema in rubric
- Place provided CSV (ticket_sales.csv) in project folder



## 📊 Dataset
- ticket_sales.csv (third-party reseller records)
- Schema includes:
  ticket_id, trans_date, event_id, event_name, event_date, event_type,
  event_city, customer_id, price, num_tickets



## ⏱️ Run Steps
- Connect to MySQL using get_db_connection()
- Load CSV into sales table with load_third_party()
- Commit and close connection
- Query popular tickets in past month using query_popular_tickets()
- Print results to stdout in user-friendly format



## 📈 Outputs
- sales table populated with ticket_sales.csv records
- Console output listing top-selling events (past month)



## 📸 Evidence

![mysql_schema.png](./evidence/mysql_schema.png)  
Screenshot of MySQL schema after import

![pipeline_run.png](./evidence/pipeline_run.png)  
Screenshot of ETL pipeline executing




## 📎 Deliverables

- [`- Python ETL script`](./deliverables/- Python ETL script)

- [`- requirements.txt`](./deliverables/- requirements.txt)

- [`- MySQL schema definition (SQL export) in /deliverables/`](./deliverables/- MySQL schema definition (SQL export) in /deliverables/)

- [`- README with setup instructions`](./deliverables/- README with setup instructions)




## 🛠️ Architecture
- Data pipeline architecture:
  - Source: CSV (third-party ticket sales)
  - Ingestion: Python (mysql-connector)
  - Storage: MySQL sales table
  - Analytics: SQL queries for popular events



## 🔍 Monitoring
- Manual validation via MySQL queries (SELECT TOP records)
- Review of command-line output logs



## ♻️ Cleanup
- Drop sales table if no longer needed
- Delete ticket_sales.csv from project folder
- Remove Python venv (optional)



*Generated automatically via Python + Jinja2 + SQL Server table `tblMiniProjectProgress` on 09-15-2025 18:04:14*