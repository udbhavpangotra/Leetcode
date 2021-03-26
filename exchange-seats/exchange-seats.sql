# select id,

#     case when id%2 = 1 then inull(lead(student,1) over(order by id),student)
#         else lag(student,1) over(order by id) end as student 
# from seat


SELECT id,
    CASE WHEN id%2 = 1 THEN IFNULL(LEAD(student,1) OVER (ORDER BY id),student)
        ELSE LAG(student,1) OVER (ORDER BY id) END AS student
FROM seat