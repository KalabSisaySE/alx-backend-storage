-- creates a trigger that resets the attribute valid_email only when email has been changed

DELIMITER @@
CREATE TRIGGER `users_UPD`
BEFORE UPDATE
ON `users` FOR EACH ROW
-- check if email is changed and reset the value of valid_email
BEGIN
IF NEW.email <> OLD.email
THEN SET NEW.valid_email = 0;
END IF;
END;
@@

DELIMITER ;