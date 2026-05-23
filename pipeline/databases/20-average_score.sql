-- Compute avg score procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    -- declare var for calculated avg
    DECLARE calculated_avg FLOAT;

    -- Compute the avg from the corrections t
    -- and shove it into the var
    SELECT AVG(score) INTO calculated_avg
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Store/update tha back to usrs t
    UPDATE users
    SET average_score = calculated_avg
    WHERE users.id = user_id;

END $$

DELIMITER ;
