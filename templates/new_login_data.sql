CREATE DATABASE internship_db2;
USE internship_db2;

CREATE TABLE user_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    domain TEXT,
    skills TEXT,
    location VARCHAR(50),
    mode VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM user_history;

USE internship_db2;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE user_history ADD email VARCHAR(100);
SELECT user, host FROM mysql.user;

SELECT * FROM users;

