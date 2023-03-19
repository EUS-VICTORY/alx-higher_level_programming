-- Uses the hbtn-0d_tvshows database to lists all genres of the sgow Dexter
-- Uses a database to lists all rows in a table corresponding to all rows in another
SELECT name
FROM tv_genres
LEFT JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
LEFT JOIN tv_shows ON tv_shows_genres.show_id = tv_shows.genre_id
WHERE tv_shows.title = 'Dester'
GROUP BY name
ORDER BY name ASC;