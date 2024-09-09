CREATE TABLE `Estado`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(255) NOT NULL
);

CREATE TABLE `Municipio`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(255) NOT NULL,
    `estado_id` INT UNSIGNED NOT NULL
);

CREATE TABLE `Crime`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `descricao` VARCHAR(255) NOT NULL,
    `sigla` VARCHAR(255) NOT NULL
);

CREATE TABLE `Patrimonio`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `descricao` VARCHAR(255) NOT NULL
);

CREATE TABLE `Crime_Municipio`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `mes` ENUM(
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'
    ) NULL,
    `ano` INT NOT NULL,
    `quantidade` INT NOT NULL,
    `municipio_id` INT UNSIGNED NOT NULL,
    `crime_id` INT UNSIGNED NOT NULL,
    `patrimonio_id` INT UNSIGNED NULL
);

ALTER TABLE
    `Crime_Municipio` ADD CONSTRAINT `crime_municipio_crime_id_foreign` FOREIGN KEY(`crime_id`) REFERENCES `Crime`(`id`);

ALTER TABLE
    `Municipio` ADD CONSTRAINT `municipio_estado_id_foreign` FOREIGN KEY(`estado_id`) REFERENCES `Estado`(`id`);

ALTER TABLE
    `Crime_Municipio` ADD CONSTRAINT `crime_municipio_patrimonio_id_foreign` FOREIGN KEY(`patrimonio_id`) REFERENCES `Patrimonio`(`id`);

ALTER TABLE
    `Crime_Municipio` ADD CONSTRAINT `crime_municipio_municipio_id_foreign` FOREIGN KEY(`municipio_id`) REFERENCES `Municipio`(`id`);
    
    
    