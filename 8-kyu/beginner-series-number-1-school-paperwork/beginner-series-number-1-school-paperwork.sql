select
n,
m,
case
  when n >= 0 and m >= 0 then n * m
  when n < 0 or m < 0 then 0
  end as res
from paperwork