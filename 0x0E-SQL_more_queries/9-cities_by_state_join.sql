-- comment
SELECT c.id, c.name, s.name FROM cities c JOIN states s ON s.id = c.state_id;
