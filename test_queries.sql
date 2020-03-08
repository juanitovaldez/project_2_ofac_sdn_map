-- SQLite
SELECT * FROM sqlite_master
order by name;

--SELECT * From "SDN" WHERE SDN_Type = "vessel";

SELECT SDN.ent_num, SDN_Name, SDN.SDN_Type, SDN.Program,
       g_id.lat, g_id.lng
FROM "SDN" JOIN geocoded_id as g_id 
ON SDN.ent_num=g_id.ent_num;

Select * from SDN WHERE ent_num = "26664"; 