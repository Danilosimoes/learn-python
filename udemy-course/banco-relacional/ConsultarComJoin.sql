select * from estados e, cidades c
where e.Id = c.Estado_id;


select
    e.nome as Estado,
    c.nome as Cidade,
    regiao as Região
from estados e, cidades c
where e.Id = c.Estado_id;



select
    c.nome as Cidade,
    e.nome as Estado,
    regiao as Região
from estados e
inner join cidades c on e.Id = c.estado_id;



