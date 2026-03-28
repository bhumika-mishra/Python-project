CREATE TABLE NewsArticle1(
    title VARCHAR(255),
    category VARCHAR(50),
    date DATE,
    relevance INT
);

INSERT INTO NewsArticle1(title, category, date, relevance) VALUES
('New Hacker Group Targets Banks', 'Hackers', '2026-03-25', 9),
('Cybersecurity Firm Stops Major Attack', 'Hackers', '2026-03-27', 7),
('Hackers Exploit AI Tools', 'Hackers', '2026-03-28', 10),
('Government Issues Warning on Data Breach', 'Data Breach', '2026-03-20', 6),
('Tech Company Releases Security Patch', 'Technology', '2026-03-26', 8);

SELECT title,date, relevance
FROM  NewsArticle1 WHERE category = 'Hackers' AND date > '2026-03-24'  
ORDER BY  relevance DESC, date DESC  ;                              
