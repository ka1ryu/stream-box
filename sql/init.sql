CREATE DATABASE IF NOT EXISTS sugoi_site CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'sugoi_site'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON sugoi_site.* TO 'sugoi_site'@'%';

FLUSH PRIVILEGES;