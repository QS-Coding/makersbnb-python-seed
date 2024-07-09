DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS users;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Users table.

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password TEXT NOT NULL
);

-- Properties table

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    available_from DATE NOT NULL,
    available_to DATE NOT NULL,
    owner_id INT NOT NULL
);

-- Bookings table
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    property_id INT NOT NULL,
    user_id INT NOT NULL,
    requested_from DATE NOT NULL,
    requested_to DATE NOT NULL,
    is_confirmed BOOLEAN NOT NULL DEFAULT FALSE,
    total_price FLOAT NOT NULL,
    created_at DATE NOT NULL
);

ALTER TABLE properties ADD FOREIGN KEY (owner_id) REFERENCES users (id);
ALTER TABLE bookings ADD FOREIGN KEY (property_id) REFERENCES properties (id);
ALTER TABLE bookings ADD FOREIGN KEY (user_id) REFERENCES users (id);


-- Test data

INSERT INTO users (name, email, password) VALUES ('Marco Polo','marco@gmail.com',crypt('mypssword', gen_salt('bf')));

INSERT INTO properties (name,description, price, available_from, available_to, owner_id) VALUES ('Studio in London','Great studio to rent in the heart of London',60.0,'2024-07-01','2024-12-31',1);

INSERT INTO bookings (property_id,user_id,requested_from, requested_to, total_price, created_at) VALUES (1,1,'2024-07-05','2024-07-11',360.0,'2024-07-01')
