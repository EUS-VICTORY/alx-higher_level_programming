-- Creates the table hbtn_0d_usa with table states.
CREATE DATABASE IF NOT EXISTS `hbtn_0c_usa`;
CREATE DATABASE IF NOT EXISTS `hbtn_0c_usa`.`states` (
	PRIMARY KEY(`id`),
	`id` INT          NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL
	);
