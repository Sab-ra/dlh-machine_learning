-- country fans
SELECT
o.origin AS origin,
SUM(b.fans) AS nb_fans
FROM metal_bands AS o
JOIN metal_bands AS b
ON o.band_name = b.band_name
GROUP BY origin
ORDER BY nb_fans DESC;
