# Write your MySQL query statement below


with t as (select Id, Salary, dense_rank() over(order by Salary desc) dense_rank_salary from Employee) 
select max(Salary) SecondHighestSalary from t where dense_rank_salary =2