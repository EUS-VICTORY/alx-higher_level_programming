-- creates and fills a table `second_table` with attributes id, name, and scorei.
Create TABLE IF NOT EXIST `second_table` (`id` INT, `name` VACHAR(256), `scores` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex");
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob, 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, " George", 8);



()