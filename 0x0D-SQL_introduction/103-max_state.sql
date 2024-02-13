-- display the max temperature of each state
-- this command will display the maximum temperature of each state sorted by state name
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
