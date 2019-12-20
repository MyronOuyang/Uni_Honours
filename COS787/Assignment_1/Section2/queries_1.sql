-- create tables
CREATE TABLE administrative_area(
    id SERIAL PRIMARY KEY,
    name varchar,
    way geometry,
    area float
);
CREATE TABLE golf_course(
    id SERIAL PRIMARY KEY,
    name varchar,
    area float,
    way geometry
);
CREATE TABLE road(
    id SERIAL PRIMARY KEY,
    name varchar,
    highway varchar,
    oneway varchar,
    surface varchar,
    ref varchar,
    service varchar,
    way geometry,
    golf_course_id INTEGER REFERENCES golf_course(id)
);
CREATE TABLE coastline(
    id SERIAL PRIMARY KEY,
    name varchar,
    way geometry,
    length float
);
CREATE TABLE beach(
    id SERIAL PRIMARY KEY,
    name varchar,
    coastline_id INTEGER REFERENCES coastline(id),
    way geometry
);
CREATE TABLE building(
    id SERIAL PRIMARY KEY,
    name varchar,
    admin_id INTEGER REFERENCES administrative_area(id),
    building_way geometry,
    admin_way geometry
);
CREATE TABLE point_of_interest(
    id SERIAL PRIMARY KEY,
    name varchar,
    way geometry,
    building_id INTEGER REFERENCES building(id),
    coastline_id INTEGER REFERENCES coastline(id)
);
CREATE TABLE groute(
    id SERIAL PRIMARY KEY,
    buffer geometry,
    way geometry
);
-- mossel bay
Select objectid as municipality_id, province, district_n, district, geom, st_area(geom)
into Mossel_Bay
from new_line;
-- administrative area
INSERT into administrative_Area (name, way, area)
select name, way, st_area(way)
FROM mossel_bay_polygon
WHERE boundary = 'administrative';
-- building   
Insert into building (admin_id, building_way, admin_way, name)
SELECT aa.id, mbp.way, aa.way, mbp.name 
FROM mossel_bay_polygon mbp, Administrative_Area aa
WHERE mbp.building is not null and ST_Contains(aa.way, mbp.way);
-- coastline   
insert into coastline (name, way, length)
SELECT name, way ,  st_length(way)
from mossel_bay_line
where osm_id = -79797
-- beach   
insert into beach (name, coastline_id, way)
SELECT mbp.name, cl.id, mbp.way as beach_way
FROM mossel_bay_polygon mbp, coastline cl
WHERE mbp.tags -> 'natural' = 'beach' 
OR mbp.tags -> 'leisure' = 'beach'
OR mbp.tags -> 'natural' = 'coastline'  and st_intersects(mbp.way, st_buffer(cl.way, 20));
-- golf_course   
insert into golf_course (name, area, way)
SELECT name, st_area(way), way
FROM mossel_bay_polygon 
WHERE leisure = 'golf_course'
-- road
insert into road (name, highway, oneway, surface, ref, service, way, golf_course_id)
select mbp.name, mbp.highway, mbp.oneway, mbp.surface, mbp.ref, mbp.service, mbp.way, golf_course.id
FROM mossel_bay_line mbp, golf_course
WHERE (mbp.highway = 'tertiary' 
OR mbp.highway = 'secondary' 
OR mbp.highway = 'road' 
OR mbp.highway = 'residential' 
OR mbp.highway = 'primary'
OR mbp.highway = 'motorway' 
OR mbp.highway = 'living_street'
OR mbp.highway = 'trunk')
OR st_intersects(mbp.way, golf_course.way)
-- poi
SELECT *
INTO poi
FROM public.mossel_bay_point p
WHERE p.tourism != '' OR p.natural != '' OR p.religion != '' OR p.shop != '';
--buffer table for 750m 
Insert into groute (buffer, way)
SELECT ST_Buffer(way, 750), way
FROM public.mossel_bay_line
WHERE public.mossel_bay_line.osm_id = -79797;
Insert into point_of_interest (way, name, coastline_id, building_id)

select Distinct(p.way), p.name, g.id, b.id
FROM poi p, public.groute g, building b
WHERE ST_Intersects(p.way, g.buffer) or st_contains(b.building_way, p.way)
