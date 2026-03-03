CREATE TABLE empl(
Eid INT PRIMARY KEY,
Ename VARCHAR(10),
Doj TEXT,
Role TEXT,
Salary TEXT
);

INSERT INTO empl(Eid,Ename,Doj,Role,Salary) VALUES
(201,"Navneet","09-12-2020","Analyst",100000),
(202,"Sobhita","10-01-2022","Advisor",90000),
(204,"Nirmal","23-07-2019","Tech Assistant",55000),
(207,"Mona","26-04-2021","UX Designer",76800),
(209,"Swati","11-03-2023","Developer",200000),
(211,"Tejas","06-09-2024","Cybersecurity Specialist",250000);

SELECT * FROM empl ;