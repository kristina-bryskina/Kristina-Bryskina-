
SELECT login FROM users ORDER BY registration_date DESC limit 1;  


SELECT DISTINCT(strftime('%Y',DATETIME(birth_date))) FROM users;


SELECT SUM(amount) AS 'total_items' FROM history;



SELECT 
	AVG( CAST(strftime('%Y', DATETIME("now")) as integer) -
	CAST(strftime('%Y', DATETIME(birth_date)) as integer))
	 AS 'average_age'
	 FROM users
	 WHERE DATETIME(registration_date, '+2 months')>DATETIME("now");