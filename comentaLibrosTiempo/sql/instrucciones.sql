CREATE USER 'comentaLibrosTiempo'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'comentaLibrosTiempo'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `comentaLibrosTiempo`;
GRANT ALL PRIVILEGES ON `comentaLibrosTiempo`.* TO 'comentaLibrosTiempo'@'localhost';

CREATE TABLE roles (
    id int NOT NULL AUTO_INCREMENT,
	descripcion varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE usuarios (
    id int NOT NULL AUTO_INCREMENT,
    usuario varchar(255) UNIQUE NOT NULL,
    passwd varchar(600) NOT NULL,
    mail varchar(255),
    tmpRegistro datetime NOT NULL,
    rolId int,
    coki varchar(600) NOT NULL,
    FOREIGN KEY (rolId) REFERENCES roles(id),
    PRIMARY KEY (id)
);


CREATE TABLE `comentarios` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`titulo` varchar(255) NOT NULL,
	`autor` varchar(255) NOT NULL,
	`comentario` varchar(255) NOT NULL,
	`usuarioId` INT NOT NULL,
	`imagen` varchar(255),
	PRIMARY KEY (`id`),
    FOREIGN KEY (`usuarioId`) REFERENCES `usuarios`(`id`)
);

CREATE TABLE regOperaciones (
    id INT AUTO_INCREMENT NOT NULL,
    id_usuario INT NOT NULL,
    operacion varchar(250) NOT NULL,
    parametros varchar(600),
    tmpOperacion datetime NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

INSERT INTO roles(descripcion) VALUE ("admin");
INSERT INTO roles(descripcion) VALUE ("normal");

INSERT INTO USUARIOS(usuario, passwd, mail,rolId,tmpRegistro) VALUES ('admin','c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec','pepe@correo.net',1,now())



