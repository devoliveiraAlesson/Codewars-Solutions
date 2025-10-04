 
select
  id,
  name,
  position("," in characteristics) as comma
from monters