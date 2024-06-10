CREATE TABLE IF NOT EXISTS sample_table (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

INSERT INTO sample_table (name) VALUES ('Chan'), ('Necmi'), ('Tuba');
