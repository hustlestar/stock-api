CREATE TABLE IF NOT EXISTS `stock_history` (
`SH_TICKER` varchar(5) NOT NULL,
`SH_DATE` date NOT NULL,
`OPEN` double NOT NULL,
`HI` double NOT NULL,
`LO` double NOT NULL,
`CLOSE` double NOT NULL,
`VOL` int(11) NOT NULL,
PRIMARY KEY (`SH_TICKER`,`SH_DATE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `user` (
`id` int NOT NULL AUTO_INCREMENT,
`username` varchar(20) NOT NULL,
`email` varchar(60) NOT NULL,
`password` varchar(60) NOT NULL,
`type` enum('admin','moder','user','banned') DEFAULT 'user',
`registered` datetime DEFAULT CURRENT_TIMESTAMP,
`sex` enum('male','female'),
`image_file` varchar(60) NOT NULL DEFAULT 'images/users/anon.jpg',
PRIMARY KEY (`id`),
UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;