-- SQLite
--select * from sqlite_master;

-- select * from "add"
-- where adress is not "-0- " and csppc is not "-0- " and country is  "Russia";


-- select * from "add"
-- where adress is "-0- " and csppc is not "-0- " and country is  "-0- ";

SELECT 'SDN'.ent_num AS ent_num,
       'SDN'.SDN_name AS SDN_Name,
       'SDN'.SDN_Type AS SDN_Type,
       'SDN'.Program AS Program,
       'add'.add_num as add_num,
       'add'.adress AS 'query', 
       'add'.csppc AS region,
       'add'.country AS country
FROM SDN JOIN 'add' ON 'SDN'.ent_num = 'add'.ent_num
WHERE 'query' NOT LIKE "%-0- %" AND
       region NOT LIKE "%-0- %"  AND
       country NOT LIKE  "%-0- %" AND
       country IS "United Kingdom" OR
       country IS "Russia";



