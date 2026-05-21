-- Select cities by temperature and order
SELECT city, AVG(value) AS temperature
FROM temperatures
GROUP BY city
ORDER BY temperature DESC;
