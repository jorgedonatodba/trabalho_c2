select m.NUMERO_CONTA,M.DATA, M.DESCRICAO, M.VALOR, M.SALDO_ANTERIOR, M.SALDO_ATUAL
  from MOVIMENTACOES m
 order by m.NUMERO_CONTA,M.DATA 