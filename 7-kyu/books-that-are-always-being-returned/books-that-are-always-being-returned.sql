select distinct
  l.book_id,
  b.title
from loans l
left join books b on b.book_id = l.book_id
where l.book_id not in (select book_id from loans where return_date is null)
​
order by l.book_id desc