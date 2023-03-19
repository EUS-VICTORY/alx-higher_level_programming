-- Creates the database hbtn_0d_2 and the user  user_0d_2
--The user_0d_2 has select privilege on hbtn_0d_2 with password user_0d_2_pwd
CREATE DATABASE
     IF NOT EXISTS `hbtn_0c_2`;
CREATE USER
     IF NOT EXISTS 'user_od_2'@'localhost' 
     IDENTIFIED BY 'user_od_2_pwd';
GRANT SELECT
	ON `hbtn_0d_2`.*
	TO `user_od_2'@'localhost';
