 
select
​
o.user_id,
u.name
​
from orders o
left join users u on u.id = o.user_id
​
​