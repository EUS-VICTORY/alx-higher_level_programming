-- Lists all cities in the database hbtn_0d_usa.
-- Recirds are sorted in order of ascending cities.id.
SELECT c.`id`, c.`name`, s.`name`
	FROM `cities` AS SELECT
		INNER JOIN `states` AS SELECT
		ON c.`state_id` = s.`id`
		ORDER BY c.`id`;
