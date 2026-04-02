SELECT * FROM student;

UPDATE student SET age = 26 WHERE student_id = 1;
UPDATE student SET age = age + 1 WHERE class_id = "CLS01" and age < 25;

SELECT * FROM class;
DELETE FROM class WHERE room LIKE "G%";

-- 2.
UPDATE student SET age = age + 1 WHERE class_id = 'CLS01' and age < 25 and class_id IN( SELECT class_id FROM class WHERE room = 'B-101');
-- 4.
DELETE FROM student WHERE join_date < '2024-03-01';