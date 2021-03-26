# Write your MySQL query statement below

with t as (select Email,count(Id) counter from Person group by Email)
select Email from t where counter > 1;