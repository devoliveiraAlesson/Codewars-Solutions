with tabelinha as (
select
user_id,
count(distinct product_id) as qtd
from orders
group by user_id
having count(distinct product_id) = (select count(distinct id) from products)
​
)
​
select
tabelinha.user_id as user_id,
u.name as name
​
from tabelinha
left join users u on u.id = tabelinha.user_id
order by user_id desc
​
​
​