select e.nome Empresa, c.nome Cidade
from empresas e, empresas_unidades eu, cidades c
where e.Id = eu.Empresa_id
and  c.`Id` = eu.Cidade_id
and sede;