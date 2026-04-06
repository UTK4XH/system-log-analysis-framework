-- Count error frequency
SELECT message, COUNT(*) as error_count
FROM logs
WHERE level = 'ERROR'
GROUP BY message
ORDER BY error_count DESC;

-- Get warnings
SELECT *
FROM logs
WHERE level = 'WARN';
