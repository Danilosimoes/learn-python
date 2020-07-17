select * from estados;

select nome, sigla from estados;

select
    Sigla,
    Nome as 'Nome do Estado'
from estados
where `Regiao` = 'Sul';

select nome,
       regiao,
       populacao
from estados
where `Populacao` >= 10
order by `Populacao` desc;