-- Rate ganres
SELECT
gn.name AS name,
SUM(r.rate) AS rating
FROM tv_genres AS gn
JOIN tv_show_genres AS sg
ON gn.id = sg.genre_id
JOIN tv_show_ratings AS r
ON sg.show_id = r.show_id
GROUP BY name
ORDER BY rating DESC;
