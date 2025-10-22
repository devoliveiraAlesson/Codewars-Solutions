select 
  n,
  case
    when n > 0 then (n*(n+1)*(n+2)) /6
    else 0
    end as res
​
​
​
from sumtriangular