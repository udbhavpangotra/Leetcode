# Write your MySQL query statement below


select MAX(Salary) SecondHighestSalary from Employee where Salary < (Select Max(Salary) from Employee) ;