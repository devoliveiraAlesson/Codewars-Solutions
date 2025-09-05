select
  number,
  case
    when (number % 2) in (1, -1) then "Odd"
    else "Even"
  end as is_even
from numbers