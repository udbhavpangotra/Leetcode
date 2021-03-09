Select D.Name AS Department,
       E.Name AS Employee,
       sub.Salary AS Salary 
       
FROM (SELECT DepartmentId AS DId,
             MAX(Salary) AS Salary
        FROM Employee
      GROUP BY DId
    ) sub
JOIN Employee E
ON sub.DId = E.DepartmentID AND sub.Salary = E.Salary
JOIN Department D
ON sub.DId = D.Id