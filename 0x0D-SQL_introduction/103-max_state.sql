-- Displays the max temperature of each state, ordered by state na
SELECT `state`, MAX( `value`) As `max-temp`
FROM `temperatures`
GROUP BY `state`
GROUP BY `state`;