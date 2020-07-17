update estados
set nome = 'Maranhão'
where `Sigla` = 'MA';


select nome from estados where `Sigla` = 'MA';


update estados
set `Nome` = 'Paraná',
     `Populacao` = 11.32
where `Sigla` = 'PR';

select nome,
       sigla,
       populacao
from estados
where `Sigla` = 'PR';