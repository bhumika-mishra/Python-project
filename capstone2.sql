CREATE TABLE Custmr1(
Custmr_id INTEGER,
Custmr_name VARCHAR(20),
Product_name TEXT,
Country TEXT
);

INSERT INTO Custmr1(Custmr_id,Custmr_name,Product_name,Country)VALUES
(111,"Jeffrey","Printer","Romania"),
(112,"Aabha","Dishwasher","India"),
(113,"Karl","Refrigerator","Sweden"),
(114,"Nora","Printer","Azerbaijan"),
(115,"Erik","Computer","Australia"),
(116,"Aditya","Hard Drive","India"),
(117,"Georgina","Printer","Romania"),
(118,"Vilma","Dishwasher","Sweden");

SELECT Custmr_name FROM Custmr1 
WHERE Custmr_name LIKE 'A%';

SELECT Custmr_name FROM Custmr1 
WHERE Custmr_name LIKE '%or%';

SELECT DISTINCT Product_name FROM Custmr1;

SELECT Custmr_name,Country FROM Custmr1
WHERE Country = 'Romania';

SELECT Product_name,Country FROM Custmr1
WHERE Country = 'India';