USE xyb9vz_db;


SELECT o.name, o.owl_species, o.owl_age, t.tree_species, t.yearsWithOwl, t.tree_age
FROM owls o
JOIN trees t ON o.owl_id = t.owl_id
WHERE t.yearsWithOwl >= 4
ORDER BY t.yearsWithOwl DESC;