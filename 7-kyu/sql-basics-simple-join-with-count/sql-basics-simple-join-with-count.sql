 
select
  p.name,
  count(t.*) as toy_count
from people p
left join toys t on t.people_id = p.id
group by p.name
​