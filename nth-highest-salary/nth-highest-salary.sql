CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      with t as(Select ID, Salary,
      dense_rank() OVER (order by Salary desc) as sal_rank
      from Employee) select max(Salary) from t where sal_rank = n     
  );
END