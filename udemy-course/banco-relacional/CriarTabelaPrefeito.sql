CREATE TABLE IF NOT EXISTS prefeitos (
    Id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Cidade_id INT UNSIGNED,
    PRIMARY KEY (Id),
    UNIQUE KEY (Cidade_id),
    FOREIGN KEY (Cidade_id) REFERENCES cidades (Id)
);