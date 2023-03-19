-- lists all Comedy shows in the database hbtn/0d_tvshows
-- lista all rows of a database corresponding to a column value
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;
