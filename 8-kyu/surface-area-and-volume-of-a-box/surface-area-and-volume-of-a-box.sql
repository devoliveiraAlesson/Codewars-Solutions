-- # write your SQL statement here: 
-- you are given a table 'box' with columns: width (int), height (int), depth (int)
-- return a query with columns: width, height, depth, area (int), volume (int)
-- sort results by area ascending, then volume ascending, then width ascending, then height ascending
​
select
  [width],
  [height],
  [depth],
  (([height] * [width]) + (height * depth) + (depth * width))  * 2 as "area",
  [width] * [height] * [depth] as "volume"
from box
where [depth] > 0 and
      [width] > 0 and
      [height] > 0
order by area asc, volume asc, width asc, height asc