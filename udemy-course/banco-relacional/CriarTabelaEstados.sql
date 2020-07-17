-- Criando tabela estado!
create Table estados (
Id INT UNSIGNED NOT NULL AUTO_INCREMENT,
Nome VARCHAR (45) NOT NULL,
Sigla VARCHAR(2) NOT NULL,
Regiao ENUM('Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul' ) NOT NULL,
Populacao DEC(5,2) NOT NULL,
PRIMARY KEY (Id),
UNIQUE KEY (Nome),
UNIQUE KEY (Sigla)
);

