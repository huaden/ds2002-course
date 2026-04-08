USE xyb9vz_db;

INSERT INTO owls (name, owl_species, owl_age, height) VALUES
('lab10_bam',     'Red Owl',      14, 5.2),
('lab10_ade',     'Blue Owl',     12, 5.6),
('lab10_bayo',   'Yellow Owl',     13, 6.0);

INSERT INTO trees (owl_id, yearsWithOwl, tree_species, tree_age) VALUES
(12,     5, 'OAK', 815),
(13,     1, 'OAK', 439);