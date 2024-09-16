-- User data dump
CREATE TABLE users (
  id INT PRIMARY KEY,
  username VARCHAR(100),
  password VARCHAR(100),
  email VARCHAR(100),
  role VARCHAR(50)
);

INSERT INTO users (id, username, password, email, role) VALUES
(1, 'admin', 'Admin123!', 'admin@company.com', 'Administrator'),
(2, 'finance_user', 'Finance2024#', 'finance@company.com', 'Finance Manager'),
(3, 'dev_user', 'Dev@Pass2024!', 'dev@company.com', 'Developer'),
(4, 'guest', 'Welcome#2024', 'guest@company.com', 'Guest User');
