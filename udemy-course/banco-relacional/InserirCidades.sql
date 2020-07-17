INSERT INTO cidades (Nome, Area, Estado_id)
VALUES('Campinas', 795, 26);


INSERT INTO cidades (Nome, Area, Estado_id)
VALUES ('Niterói', 133.9, 19);


INSERT INTO cidades (Nome, Area, Estado_id)
VALUES (
        'Caruaru',
         920.6,
         (select Id from estados where Sigla = 'PE')
)


INSERT INTO cidades
     (Nome, Area, Estado_id)
VALUES (
        'Juazeiro do Norte',
        248.2,
        (select Id from estados where Sigla = 'CE')
)


SELECT * FROM cidades;
