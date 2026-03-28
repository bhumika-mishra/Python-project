CREATE TABLE empl2(
    Eid INT,
    Ename VARCHAR(20),
    Department VARCHAR(50),
    City VARCHAR(20),
    Doj DATE,
    Salary DECIMAL(10,2)
);

INSERT INTO empl2(Eid,Ename,Department,City,Doj,Salary)VALUES
(101,"Divya","Sales","Jaipur","2022-08-09",60000),
(102,"Aashna","IT","Delhi","2021-07-11",100000),
(103,"Mahi","Admin","Nagpur","2019-08-23",90000),
(104,"Rakesh","Finance","Pune","2020-04-23",250000),
(105,"Vaibhav","Sales","Jaipur","2024-08-17",200000),
(106,"Aditya","IT","Jaipur","2025-10-21",150000),
(107,"Shubham","Admin","Delhi","2022-03-22",80000),
(108,"Mukti","Finance","Lucknow","2020-10-29",245000),
(109,"Abhinash","IT","Pune","2018-05-28",345000),
(110,"Ranveer","Admin","Lucknow","2020-07-22",88000);

SELECT * FROM empl2;

SELECT Department,Doj FROM empl2 
ORDER BY Department ASC, Doj DESC;

SELECT Department, AVG(Salary) AS avg_salary, COUNT(Eid) AS total_employees FROM empl2;

SELECT * FROM empl2
WHERE Doj > '2022-03-22';

SELECT DISTINCT Department FROM empl2;

SELECT Ename,Salary FROM empl2 
WHERE Ename LIKE 'A%';

SELECT * FROM empl2
WHERE City = 'Jaipur'; 

SELECT SUM(Salary) AS Total_salary FROM empl2;

SELECT Ename,MIN(Salary) AS Min_salary FROM empl2;

SELECT Ename,MAX(Salary) AS Max_salary FROM empl2;

SELECT Ename,Salary FROM empl2 
ORDER BY Salary DESC;

