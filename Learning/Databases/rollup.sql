SELECT 
    d.year, 
    s.city, 
    s.stationid, 
    SUM(f.wastecollected) AS total_waste
FROM 
    facttrips f
-- Multiple JOINS REQUIRED to map columns from different tables
JOIN 
    dimdate d ON f.dateid = d.dateid
JOIN
	dimstation s ON f.stationid = s.stationid
GROUP BY 
    ROLLUP (d.year, s.city, s.stationid)
ORDER BY 
    d.year, 
    s.city, 
    s.stationid;
