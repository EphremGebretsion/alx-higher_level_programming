-- display the average temperature of cities
-- this command dispalays the average temperature of cities sorted by temprature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
