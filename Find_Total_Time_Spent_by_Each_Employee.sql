-- Write your PostgreSQL query statement below
select e.event_day as day, e.emp_id , SUM(e.out_time - e.in_time) as total_time
from Employees as e
group by e.emp_id,e.event_day
