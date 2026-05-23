-- Divide Safely
DELIMITER $$

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
    -- Check if the denominator is 0
    IF b = 0 THEN
        RETURN 0;
    ELSE
        -- If it's safe, return result
        RETURN a / b;
    END IF;
END $$

DELIMITER ;