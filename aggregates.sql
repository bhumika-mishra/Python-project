CREATE TABLE Employee1(
Eid INTEGER,
Ename VARCHAR(20),
Department VARCHAR(20),
Salary DECIMAL
);

INSERT INTO Employee1(Eid,Ename,Department,Salary)VALUES
(101,"Rakesh","Finance",300000),
(102,"Aashna","IT",90000),
(103,"Divya","Marketing",50000),
(104,"Abhishek","Finance",250000),
(105,"Mahi","IT",100000),
(101,"Rakesh","Marketing",35000);

SELECT SUM(Salary) AS Total_salary FROM Employee1;

SELECT AVG(Salary) AS Avg_salary FROM Employee1;

SELECT DISTINCT Department FROM Employee1;

SELECT MIN(Salary) AS Min_salary,
MAX(Salary) AS Max_salary FROM Employee1;