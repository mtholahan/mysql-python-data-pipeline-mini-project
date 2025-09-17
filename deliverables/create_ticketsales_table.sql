/*
* Date 14-Jul-2025
* Author: Mark Holahan
* Purpose: MySQL Python Data Pipeline Mini Project
* RDBMS: MySQL
*/

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

SELECT * FROM ticketsales ORDER BY trans_date DESC;

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

SELECT t.event_id, t.event_name, t.trans_date
FROM ticketsales t
WHERE
	YEAR(t.trans_date) >= YEAR(t.trans_date - INTERVAL 1 MONTH) 
    AND 
    MONTH(t.trans_date) >= MONTH(t.trans_date - INTERVAL 1 MONTH)
GROUP BY t.event_id
ORDER BY t.event_id, t.trans_date DESC
LIMIT 5;


SELECT *
FROM your_table
WHERE YEAR(date_field) = YEAR(NOW() - INTERVAL 1 MONTH)
  AND MONTH(date_field) = MONTH(NOW() - INTERVAL 1 MONTH);