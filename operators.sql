CREATE TABLE Customer1(
Custmr_id INTEGER,
Custmr_name VARCHAR(20),
City TEXT,
Grade INTEGER
);

INSERT INTO Customer1(Custmr_id,Custmr_name,City,Grade)VALUES
(111,"Jeffrey","New York",100),
(112,"Calvin","New York",100),
(113,"Daniel","Vancouver",110),
(114,"George","New York",120),
(115,"Eliza","New York",100),
(116,"Danny","New York",110),
(117,"Bella","New York",140),
(118,"Diahnne","Bangkok",100);

SELECT * FROM Customer1 
WHERE City = "New York" OR Grade > 100 ;

SELECT * FROM Customer1 
WHERE City = "New York" AND Grade > 100 ;
