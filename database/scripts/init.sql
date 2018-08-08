CREATE TABLE IF NOT EXISTS `stock_history` (
`TICKER` varchar(5) NOT NULL,
`PRICE_DATE` date NOT NULL,
`OPEN` double NOT NULL,
`HIGH` double NOT NULL,
`LOW` double NOT NULL,
`CLOSE` double NOT NULL,
`VOL` int(11) NOT NULL,
PRIMARY KEY (`TICKER`,`PRICE_DATE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `user` (
`id` int NOT NULL AUTO_INCREMENT,
`username` varchar(20) NOT NULL,
`email` varchar(60) NOT NULL,
`password` varchar(60) NOT NULL,
`type` enum('admin','moder','user','banned') DEFAULT 'user',
`registered` datetime DEFAULT CURRENT_TIMESTAMP,
`sex` enum('male','female'),
`image_file` varchar(60) NOT NULL DEFAULT 'pics/users/anon.jpg',
PRIMARY KEY (`id`),
UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;