-- Write your PostgreSQL query statement below
Select p.product_id 
from Products as p
where low_fats='Y' and recyclable='Y'