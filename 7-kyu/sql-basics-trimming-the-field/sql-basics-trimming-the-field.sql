select
  id,
  name,
  regexp_replace(characteristics, ',.+', '') as characteristic
​
from monsters
order by id