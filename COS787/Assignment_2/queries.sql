-- 3.2
select f.biome
from "fire_eco_types" f, "za_burntarea" b
where st_contains(f.geom, b.geom)
-- 3.3
select f.biome
from "fire_eco_types" f, "za_burntarea" b
where st_contains(f.geom, b.geom)
order by b.yyyymm, b.burnday
limit 1
-- 3.4
select clip.rast, clip.geom, clip.name
into rain_prov
from ( 
	select st_clip(r.rast, p.geom) as rast, p.province as name, p.geom as geom
	from "Provinces" p, rain r
) clip

SELECT (
    SELECT ST_SummaryStats(a.rast)
).mean as avg_rain, a.name
FROM rain_prov a
order by avg_rain desc
-- 3.5
22.566 Western 
-- 3.6
SELECT st_area (b.geom)
FROM (
    SELECT (
        SELECT ST_SummaryStats(a.rast)
    ).mean as avg_rain, a.name, a.geom
    FROM rain_prov a
    ORDER BY avg_rain DESC
    LIMIT 1
) b
-- 3.7
SELECT c.province, c.biome
FROM (
    SELECT DISTINCT (
        SELECT ST_SummaryStats(a.rast)
    ).mean as avg_rain, a.province, a.geom
    FROM rain_prov a
    ORDER BY avg_rain DESC
    LIMIT 1
) b, province_land_cover c
WHERE b.province = c.province
-- 3.8
select polysqkm
from fire_eco_types f
where province = 'Gauteng'
order by polysqkm desc
limit 1
-- 3.9a
NDWI = (NIR-SWIR)/(NIR+SWIR)
-- 3.9b