 
​
  SELECT
  REGEXP_REPLACE(text, '[aeiouAEIOU]', ' ', 'g') as results
  from random_string