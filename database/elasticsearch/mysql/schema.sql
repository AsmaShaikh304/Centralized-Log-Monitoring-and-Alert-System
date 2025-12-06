CREATE DATABASE clmas_db;

USE clmas_db;

CREATE TABLE logs (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    timestamp VARCHAR(50),
    level VARCHAR(20),
    message TEXT,
    source VARCHAR(50)
);

CREATE TABLE alerts (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    rule_name VARCHAR(100),
    message TEXT,
    timestamp VARCHAR(50)
);
