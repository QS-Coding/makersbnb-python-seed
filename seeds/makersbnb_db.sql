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

-- User Insert 
INSERT INTO users (name, email, password) VALUES ('Marco Polo','marco@gmail.com',crypt('mypssword', gen_salt('bf')));
INSERT INTO users (name, email, password) VALUES ('Martha Hudson','martha.hudson@example.com',crypt('IamSHerl0ck3d', gen_salt('bf')));
INSERT INTO users (name, email, password) VALUES ('Homer Simpson','homer.simpson@example.com',crypt('d0h12345', gen_salt('bf')));
INSERT INTO users (name, email, password) VALUES ('Sirius Black','sirius.black@example.com',crypt('padf00t123', gen_salt('bf')));
INSERT INTO users (name, email, password) VALUES ('Bruce Wayne','bruce.wayne@example.com',crypt('batc4ve123', gen_salt('bf')));
INSERT INTO users (name, email, password) VALUES ('Bilbo Baggins','bilbo.baggins@example.com',crypt('ringbearer123', gen_salt('bf')));

-- Property Insert
INSERT INTO properties (name,description, price, available_from, available_to, owner_id) VALUES ('Studio in London','Great studio to rent in the heart of London',60.0,'2024-07-01','2024-12-31',1);
INSERT INTO properties (name, description, price, available_from, available_to, owner_id) VALUES ('Studio in London','Great studio to rent in the heart of London',60.0,'2024-07-01','2024-12-31',1);
INSERT INTO properties (name, description, price, available_from, available_to, owner_id) VALUES ('Spacious Apartment','Lovely spacious apartment with great views',80.0,'2024-08-01','2024-11-30',2);
INSERT INTO properties (name, description, price, available_from, available_to, owner_id) VALUES ('Modern Flat','Newly renovated modern flat in city center',100.0,'2024-09-01','2024-10-31',3);
INSERT INTO properties (name, description, price, available_from, available_to, owner_id) VALUES ('Cozy Cottage','A cozy cottage in the countryside',40.0,'2024-07-15','2024-12-15',4);
INSERT INTO properties (name, description, price, available_from, available_to, owner_id) VALUES ('Beach House','Beautiful beach house with ocean views',120.0,'2024-07-01','2024-08-31',5);

-- Booking Insert
INSERT INTO bookings (property_id,user_id,requested_from, requested_to, total_price, created_at) VALUES (1,1,'2024-07-05','2024-07-11',360.0,'2024-07-01')
INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) VALUES (1, 1, '2024-07-05', '2024-07-11', 360.0, '2024-07-01');
INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) VALUES (2, 2, '2024-08-10', '2024-08-20', 800.0, '2024-08-01');
INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) VALUES (3, 3, '2024-09-05', '2024-09-15', 1000.0, '2024-09-01');
INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) VALUES (4, 4, '2024-07-20', '2024-07-30', 400.0, '2024-07-15');
INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) VALUES (5, 5, '2024-07-10', '2024-07-20', 1200.0, '2024-07-01');


