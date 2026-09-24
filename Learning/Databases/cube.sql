-- Create a cube query using the columns year, city, stationid, and average waste collected.

SELECT 
	d.year,
	s.stationid,
	s.city,
	AVG(f.wastecollected) as AVERAGE_WASTE_COLLECTED

FROM
	facttrips f
	
	JOIN 
		dimdate d ON f.dateid = d.dateid
	JOIN
		dimstation s on f.stationid = s.stationid

GROUP BY 
	CUBE (d.year, s.city, s.stationid)

ORDER BY
	d.year,
	s.city,
	s.stationid