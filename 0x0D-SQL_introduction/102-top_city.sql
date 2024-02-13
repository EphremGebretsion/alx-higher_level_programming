-- display the top 3 of cities temperature during July and August
-- this command will deisplay the top 3 cities with highest temperature during July to Augest
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 or month = 8
	GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
