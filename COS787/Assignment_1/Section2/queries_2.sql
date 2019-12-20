-- 2.2
SELECT SUM(ST_Length(way)) AS lengthm, SUM(ST_Length(way)/1000) AS lengthkm	
FROM mossel_bay_line
WHERE mossel_bay_line.highway = 'tertiary' 
OR mossel_bay_line.highway = 'secondary' 
OR mossel_bay_line.highway = 'road' 
OR mossel_bay_line.highway = 'residential' 
OR mossel_bay_line.highway = 'primary'
OR mossel_bay_line.highway = 'motorway' 
OR mossel_bay_line.highway = 'living_street'
OR mossel_bay_line.highway = 'trunk'
-- 2.3
SELECT WAY, ST_NRings(way) As Nrings, ST_NumInteriorRings(way) As ninterrings
FROM mossel_bay_polygon
WHERE boundary = 'administrative'
AND ST_NRings(way) > 1
-- 2.4
SELECT SUM(a.way_area) as building_area, b.all_area as total_area, SUM(a.way_area)/b.all_area*100 as percentage 
FROM mossel_bay_polygon a, (
    SELECT SUM(way_area) as all_area
    FROM mossel_bay_polygon
) b
WHERE a.building IS NOT null
GROUP BY b.all_area
-- 2.5
SELECT way_area, name
FROM mossel_bay_polygon
WHERE tags -> 'natural' = 'beach' 
OR tags -> 'leisure' = 'beach'
OR tags -> 'natural' = 'coastline'
ORDER BY way_area DESC
-- 2.6
SELECT Distinct(b.way)
FROM (
    SELECT b.way, b.geom
    FROM mossel_bay_point a, mossel_bay_polygon b
    WHERE a.name = 'Mossel Bay Golf Estate'
    AND b.leisure = 'golf_course'
    AND ST_CONTAINS(b.way, a.way)
) a, road b
WHERE ST_INTERSECTS(a.way, b.way)
-- 2.7
SELECT *
FROM public.poi p, public.groute g
WHERE ST_Intersects(p.way, g.buffer);
-- 2.8
SELECT tags->'osm_user', COUNT(tags->'osm_user') AS num
FROM mossel_bay_polygon
WHERE tags -> 'building' IS NOT null
Group BY tags->'osm_user'
ORDER BY num DESC
-- 2.9
SELECT SUBSTRING(tags->'osm_timestamp' from 0 for 11) AS osm_timestamp, COUNT(tags->'osm_timestamp') AS num_lines_edited
FROM mossel_bay_line
WHERE tags -> 'osm_timestamp' LIKE '2018-%'
AND (tags -> 'osm_version')::INT > 1
GROUP BY osm_timestamp
ORDER BY num_lines_edited DESC
