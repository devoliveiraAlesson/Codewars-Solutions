select n,
​
(floor(n * 0.5) * ceil(n * 0.5))::integer as res
​
​
from perpendicular