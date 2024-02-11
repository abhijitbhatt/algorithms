# https://stackoverflow.com/questions/47827992/collapsing-window-intervals

# Execute script in DuckDB

DROP TABLE IF EXISTS memory.main.state;

CREATE TABLE IF NOT EXISTS memory.main.state (
   name STRING,
   start_id INT,
   end_id INT);

INSERT INTO memory.main.state VALUES ('A',1,2);
INSERT INTO memory.main.state VALUES ('A',2,3);
INSERT INTO memory.main.state VALUES ('A',3,4);
INSERT INTO memory.main.state VALUES ('B',4,5);
INSERT INTO memory.main.state VALUES ('B',5,6);
INSERT INTO memory.main.state VALUES ('A',6,7);
INSERT INTO memory.main.state VALUES ('C',7,8);
INSERT INTO memory.main.state VALUES ('C',8,9);

-- excepted output
-- A,1,4
-- B,4,6
-- A,6,7
-- C,7,9

-- This script will collapse intervals but will ignore when
-- two consecutive windows have gaps. For example first one
-- starting at 1 ending in 2 while next one starting at 4 and
-- ending in 6

SELECT
   group_id
   , name
   , MIN(start_id)
   , MAX(end_id)
FROM (SELECT
         *
         , SUM(same_as_last) OVER (ORDER BY start_id) group_id
      FROM (SELECT
               *
               -- check previous record to confirm if name has switched
               -- if yes, then mark the record with first switch with 1
               -- this will be used to generate artificial group_id
               -- used in final group-by clause
               , CASE WHEN COALESCE(LAG(name) OVER (ORDER BY start_id),name) != name THEN 1 ELSE 0 END same_as_last
            FROM memory.main.state))
GROUP BY name, group_id
ORDER BY group_id