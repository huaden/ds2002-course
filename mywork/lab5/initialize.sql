USE xyb9vz_db;

DROP TABLE IF EXISTS trees;
DROP TABLE IF EXISTS owls;



CREATE TABLE owls (
    owl_id      INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    owl_species VARCHAR(100) NOT NULL,
    owl_age     INT,
    height      FLOAT
);

CREATE TABLE trees (
    tree_id         INT PRIMARY KEY AUTO_INCREMENT,
    owl_id          INT NOT NULL,
    yearsWithOwl    INT NOT NULL,
    tree_species    VARCHAR(100) NOT NULL,
    tree_age        INT,
    FOREIGN KEY (owl_id) REFERENCES owls(owl_id)
);


INSERT INTO owls (name, owl_species, owl_age, height) VALUES
('Bob',     'Red Owl',      8, 3.2),
('Joe',     'Blue Owl',     9, 4.3),
('Peter',   'Blue Owl',     13, 4.0),
('Billy',   'Purple Owl',   10, 4.4),
('Montana', 'Yellow Owl',   9, 5.9),
('Milan',   'Red Owl',      7, 5.8),
('Meteor',  'Purple Owl',   7, 3.2),
('Rhowl',   'Red Owl',      9, 5.7),
('Alex',    'Blue Owl',     5, 3.6),
('Data',    'Yellow Owl',   7, 4.2),
('Science', 'Yellow Owl',   14, 4.6);

INSERT INTO trees (owl_id, yearsWithOwl, tree_species, tree_age) VALUES
(1,     5, 'OAK', 815),
(2,     1, 'OAK', 439),
(3,     4, 'FIR', 329),
(4,     3, 'OAK', 589),
(5,     4, 'FIR', 813),
(6,     6, 'OAK', 758),
(7,     3, 'OAK', 821),
(8,     2, 'OAK', 772),
(9,     5, 'OAK', 237),
(10,    3, 'FIR', 868),
(11,    5, 'OAK', 719);