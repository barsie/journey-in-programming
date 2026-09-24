-- Create a materialized view named max_waste_stats using the columns city, stationid, 
-- trucktype, and max waste collected.

CREATE MATERIALIZED VIEW max_waste_stats AS
SELECT 
    s.city, 
    s.stationid, 
    t.trucktype, 
    MAX(f.wastecollected) AS max_waste_collected
FROM 
    facttrips f
JOIN 
    dimstation s ON f.stationid = s.stationid
JOIN 
    dimtruck t ON f.truckid = t.truckid
GROUP BY 
    s.city, 
    s.stationid, 
    t.trucktype
WITH DATA;
