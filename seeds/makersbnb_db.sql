DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS images;
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

-- Property images table
CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    property_id INT NOT NULL,
    image BYTEA NOT NULL
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
ALTER TABLE images ADD FOREIGN KEY (property_id) REFERENCES properties (id);
ALTER TABLE bookings ADD FOREIGN KEY (property_id) REFERENCES properties (id);
ALTER TABLE bookings ADD FOREIGN KEY (user_id) REFERENCES users (id);


-- Test data

INSERT INTO users (name, email, password) VALUES ('Marco Polo','marco@gmail.com',crypt('mypssword', gen_salt('bf')));

INSERT INTO properties (name,description, price, available_from, available_to, owner_id) VALUES ('Studio in London','Great studio to rent in the heart of London',60.0,'2024-07-01','2024-12-31',1);

INSERT INTO bookings (property_id,user_id,requested_from, requested_to, total_price, created_at) VALUES (1,1,'2024-07-05','2024-07-11',360.0,'2024-07-01')


-- Insert new users with humorous names
INSERT INTO users (name, email, password) 
VALUES ('John Doe', 'john.doe@gmail.com', crypt('pa$$w0rd', gen_salt('bf')));

INSERT INTO users (name, email, password) 
VALUES ('Jane Dough', 'jane.dough@gmail.com', crypt('bakingL0ver', gen_salt('bf')));

INSERT INTO users (name, email, password) 
VALUES ('Sam Sung', 'sam.sung@gmail.com', crypt('samsung123', gen_salt('bf')));

INSERT INTO users (name, email, password) 
VALUES ('Will Power', 'will.power@gmail.com', crypt('willpower!', gen_salt('bf')));

-- Insert properties with humorous descriptions
INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Igloo in Antarctica', 'Chill out in this exclusive igloo, guaranteed to be the coolest spot on Earth!', 100.0, '2024-12-01', '2025-03-01', 2);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Treehouse in the Amazon', 'Live like Tarzan in this treehouse, swing from vine to vine!', 75.0, '2024-08-01', '2025-01-01', 3);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Haunted Mansion', 'Spend a night with friendly ghosts! Comes with complimentary screams and eerie noises.', 200.0, '2024-10-01', '2024-11-01', 1);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Underwater Suite', 'Stay with the fishes! Scuba gear not included.', 150.0, '2024-06-01', '2024-09-01', 3);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Studio in London', 'Great studio to rent in the heart of London', 60.0, '2024-07-01', '2024-12-31', 1);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Cave in the Mountains', 'Experience the Stone Age! Flintstones fans will love it.', 50.0, '2024-05-01', '2024-09-01', 4);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Space Capsule', 'Sleep among the stars! Zero gravity bed included.', 300.0, '2024-07-01', '2024-12-31', 5);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Pirate Ship', 'Arrr! Stay aboard the Jolly Roger and find hidden treasures.', 80.0, '2024-06-01', '2024-11-01', 1);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Medieval Castle', 'Live like a king or queen! Drawbridge and moat included.', 250.0, '2024-03-01', '2024-08-01', 3);

INSERT INTO properties (name, description, price, available_from, available_to, owner_id) 
VALUES ('Beach Hut', 'Sun, sea, and sand just outside your door.', 90.0, '2024-05-01', '2024-09-01', 2);

-- Insert humorous bookings
INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (1, 1, '2024-12-10', '2024-12-20', 1000.0, '2024-12-01');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (2, 2, '2024-09-01', '2024-09-10', 750.0, '2024-08-25');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (3, 1, '2024-10-13', '2024-10-14', 200.0, '2024-10-01');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (4, 2, '2024-06-15', '2024-06-20', 750.0, '2024-06-01');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (1, 1, '2024-07-05', '2024-07-11', 360.0, '2024-07-01');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (5, 3, '2024-07-10', '2024-07-15', 750.0, '2024-07-01');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (6, 4, '2024-06-20', '2024-06-25', 250.0, '2024-06-10');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (7, 5, '2024-08-01', '2024-08-10', 3000.0, '2024-07-20');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (8, 1, '2024-09-05', '2024-09-12', 560.0, '2024-09-01');

INSERT INTO bookings (property_id, user_id, requested_from, requested_to, total_price, created_at) 
VALUES (9, 2, '2024-07-20', '2024-07-25', 1250.0, '2024-07-15');
