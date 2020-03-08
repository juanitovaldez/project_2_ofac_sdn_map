-- SQLite
SELECT * FROM sqlite_master
order by name;

-- Delete From SDN;
-- Delete From "add";
-- Delete From alt;
-- Delete From sdn_comments;

DROP VIEW IF EXISTS geo_codeable_adresses;
Create VIEW geo_codeable_adresses AS
SELECT 'add'.add_num as add_num,
       'add'.ent_num AS ent_num,
       'add'.adress AS "query", 
       'add'.csppc AS region,
       'add'.country AS country
FROM 'add' WHERE "query" NOT LIKE "%-0- %" OR 
                 region NOT LIKE "%-0- %"  OR
                 country NOT LIKE  "%-0- %";


SELECT * from geo_codeable_adresses;




-- DROP VIEW IF EXISTS geo_code;

-- CREATE VIEW geo_code AS	
--     SELECT add.add_num,
--            add.ent_num,
--            add.adress,
--            add.csppc,
--            add.country,
