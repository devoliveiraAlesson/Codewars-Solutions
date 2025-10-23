​
select
  film_id,
  title,
  special_features
  
from film
​
where array['Behind the Scenes','Deleted Scenes'] && special_features
      and not special_features @> array['Behind the Scenes','Deleted Scenes']
      and not array['Commentaries'] && special_features
​
order by title asc, film_id asc