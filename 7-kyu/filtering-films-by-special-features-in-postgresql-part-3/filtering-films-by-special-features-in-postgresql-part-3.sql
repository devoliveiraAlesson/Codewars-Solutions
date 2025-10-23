 
with filmes as (
select
  film_id,
  title,
  
  case
    when 'Commentaries' = any(special_features) then NUll
    when 'Deleted Scenes' = any(special_features) and 'Behind the Scenes'= any(special_features) then NUll
    when 'Deleted Scenes' = any(special_features) or 'Behind the Scenes'= any(special_features) then special_features
    else NUll end
    as special_features
​
from film
)
​
select * from filmes
where special_features = Null