-- list shows rate by rating )))
SELECT
sh.title AS title,
SUM(r.rate) AS rating
FROM tv_shows AS sh
JOIN tv_show_ratings AS r
ON sh.id = r.show_id
GROUP BY title
ORDER BY rating DESC;
