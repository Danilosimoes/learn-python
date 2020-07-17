select * from
    cidades c
inner join
    prefeitos p
on
    c.`Id` = p.`Cidade_id`;


select * from
    cidades c
left join
    prefeitos p
on
    c.`Id` = p.`Cidade_id`;


select * from
    cidades c
right join
    prefeitos p
on
    c.`Id` = p.`Cidade_id`;


-- select * from
--    cidades c
-- full join
--    prefeitos p
-- on
--    c.`Id` = p.`Cidade_id`;


select * from
    cidades c
left join
    prefeitos p
on
    c.`Id` = p.`Cidade_id`
union
select * from
    cidades c
right join
    prefeitos p
on
    c.`Id` = p.`Cidade_id`;





