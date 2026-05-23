-- Creates stored procedure AddBonus
DELIMITER $$

CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    -- Create var for the proj ID
    DECLARE p_id INT;

    -- Try to fine the exist pr ID
    SELECT id INTO p_id
    FROM projects
    WHERE name = project_name;

    -- If it not exist (p_id = NULL) --> create it
    IF p_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        -- Grab new ID
        SET p_id = LAST_INSERT_ID();
    END IF;
