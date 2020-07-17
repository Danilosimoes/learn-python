CREATE TABLE IF NOT EXISTS empresas (
    Id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    cnpj INT UNSIGNED,
    PRIMARY KEY (Id),
    UNIQUE KEY (cnpj)
);


-- cidades_empresas

CREATE TABLE IF NOT EXISTS empresas_unidades(
    Empresa_id INT UNSIGNED NOT NULL,
    Cidade_id INT UNSIGNED NOT NULL,
    Sede TINYINT(1) NOT NULL,
    PRIMARY KEY(Empresa_id, Cidade_id)
);