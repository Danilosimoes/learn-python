CREATE TABLE IF NOT EXISTS cidades (
    Id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Estado_id INT UNSIGNED NOT NULL,
    Area DEC(10,2),
    PRIMARY KEY (Id),
    FOREIGN KEY (Estado_id) REFERENCES estados (Id)
);