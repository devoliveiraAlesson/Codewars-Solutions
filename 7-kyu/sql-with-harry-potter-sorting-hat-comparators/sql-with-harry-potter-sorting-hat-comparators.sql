with base as (
select *,
  case
    when quality1 = 'evil' and quality2 = 'cunning' then 'Slytherin'
    when quality1 =  'brave' and quality2 <> 'evil' then 'Gryffindor'
    when quality1 ='studious' or quality2 = 'intelligent' then 'Ravenclaw'
    when quality1 = 'hufflepuff' or quality2 = 'hufflepuff' then 'Hufflepuff'
    else 'NOPS'
  end as vaiOuRacha
from students
)
​
select id, name, quality1, quality2 from base
where vaiOuRacha <> 'NOPS'