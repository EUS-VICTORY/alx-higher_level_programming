-- Displays the average temperature (in Fahrenheit)
-- by city ordered by descending temperature.
SELECT `city`, AVG(`Value`) AS `avg_tmp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;