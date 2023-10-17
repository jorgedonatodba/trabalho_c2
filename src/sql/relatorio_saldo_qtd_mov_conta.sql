 with qtd_mov as
  (select mv.NUMERO_CONTA, count(1) as qtd
  from MOVIMENTACOES mv
  group by mv.numero_conta)   
  select cl.NOME, ct.NUMERO "Numero da Conta", m.QTD as MOVIMENTACOES, ct.SALDO "SALDO ATUAL"
  FROM CLIENTES cl, CONTAS ct, qtd_mov m
  where CL.ID=ct.ID_CLIENTE
  and ct.ID=m.NUMERO_CONTA