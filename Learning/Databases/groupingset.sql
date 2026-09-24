-- Create a grouping sets query using the columns stationid, trucktype, total waste collected
-- This process requires a join (especifically a left-join)
SELECT 
    f.stationid, 
    t.trucktype, 
    SUM(f.wastecollected) AS total_waste
FROM 
    facttrips f
JOIN 
    dimtruck t ON f.truckid = t.truckid
GROUP BY 
    GROUPING SETS (
        (f.stationid, t.trucktype), -- Detalle por estación y camión
        (f.stationid),              -- Subtotal por estación
        (t.trucktype),              -- Subtotal por tipo de camión
        ()                          -- Gran total de toda la recolección
    )
	HAVING
		GROUPING(f.stationid)=0     -- This ensure null values are not included
		AND GROUPING(t.trucktype)=0 -- This ensure null values are not included
ORDER BY 
    f.stationid, 					-- Add NULL LAST to include nullable data
    t.trucktype;					-- Add NULL LAST to include nullable data
