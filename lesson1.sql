CREATE TABLE supplier(
SNO INT PRIMARY KEY ,
Sname VARCAHR(10),
Status INT,
City VARCHAR(10)
);

INSERT INTO supplier (SNO,Sname,Status,City) VALUES
(101,"Riya",5,"Cuttack"),
(102,"Adwiti",7,"Surat"),
(103,"Akash",10,"Jaipur"),
(104,"Sonali",15,"Pune"),
(105,"Abhishek",12,"Mohali");

SELECT * FROM supplier;



CREATE TABLE salesman(
SID INT PRIMARY KEY ,
Sname VARCAHR(10),
City VARCHAR(10),
Commission INT
);

INSERT INTO salesman (SID,Sname,City,Commission) VALUES
(111,"Abinash","Cuttack",10),
(112,"Mani","Surat",12),
(113,"Ganesh","Jaipur",20),
(114,"Sneha","Pune",5),
(115,"Ravi","Mohali",8);

SELECT * FROM salesman;



CREATE TABLE orders(
Order_no INT PRIMARY KEY ,
Purchs_amt INT,
Ord_date TEXT,
cust_id TEXT,
Slm_id TEXT
);

INSERT INTO orders(Order_no,Purchs_amt,Ord_date,cust_id,Slm_id) VALUES
(2001,20000,"09-12-2025",12345,23434),
(2002,6000,"11-11-2024",12347,23479),
(2003,30000,"23-09-2023",12365,23086),
(2004,56700,"01-03-2026",12395,23656),
(2005,22300,"12-08-2024",12055,23126);

SELECT * FROM orders ;

