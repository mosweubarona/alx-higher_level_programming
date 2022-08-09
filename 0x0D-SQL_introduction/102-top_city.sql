-- Using temperature data set from ex.18
-- Display top 3 cities by temperature during July and August
SELECT 'city', AVG('value') 'avg_temp' FROM 'temperatures'
WHERE 'month' = 7 OR 'month' = 8
GROUP BY 'city'
ORDER BY 'avg_temp' DESC
LIMIT 3;
