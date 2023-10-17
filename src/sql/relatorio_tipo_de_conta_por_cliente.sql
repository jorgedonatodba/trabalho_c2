  select cl.NOME, ct.TIPO,COUNT(1)
  from CLIENTES cl, CONTAS ct
  where cl.ID=ct.ID_CLIENTE
  GROUP BY cl.nome,ct.tipo