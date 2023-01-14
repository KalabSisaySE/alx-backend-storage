-- ranks country origins of bands
SELECT SUM(fans) AS nb_fans, origin
FROM `metal_bands`
GROUP BY origin
ORDER BY nb_fans desc
