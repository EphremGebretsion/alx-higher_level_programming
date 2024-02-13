-- lists the number of records with the same score
-- this command print scores with there number of occurance
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
