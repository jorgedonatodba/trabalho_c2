/*INSERE DADOS NA TABELA DE PEDIDOS E ITENS*/
DECLARE
  VCPF NUMBER :=0;
  VCOD_CONTA NUMBER :=0;
  VNUM_CONTA NUMBER :=0;
  VCOD_MOV NUMBER :=0;
  VDESC VARCHAR2(20);
  VTIPOMOV VARCHAR2(1);
  VTIPOCONT VARCHAR2(10);
  VSALDO  NUMBER :=0;
  VVALOR  NUMBER :=0;
  VLIMITE  NUMBER :=0;
  VID NUMBER :=0;
  VDATAMOV DATE := SYSDATE - 2000;
  VSALDOANT NUMBER :=0;
  VSALDOATU NUMBER :=0;
  VCONTASALDO NUMBER :=0;
BEGIN

FOR Lcntr IN 1..10
LOOP

  VCOD_CONTA := seq_contas_id.NEXTVAL;

 SELECT ID
    INTO VID
    FROM CLIENTES
  WHERE ID = (select round(dbms_random.value(1,8)) from dual);


  SELECT round(dbms_random.value(1,1000),2) 
    INTO VSALDO
  from dual;
  
  SELECT round(dbms_random.value(1,1000),2) 
    INTO VLIMITE
  from dual;

select CASE round(dbms_random.value(1,3))
  WHEN 1 THEN 'corrente'
  WHEN 2 THEN 'poupanca'
  WHEN 3 THEN 'credito'
END
INTO VTIPOCONT
 from dual;

  VNUM_CONTA := VNUM_CONTA + 1;

  INSERT INTO CONTAS VALUES(VCOD_CONTA,  /*CODIGO_CONTA*/
                            VNUM_CONTA,  /*NUMERO_CONTA*/
                             VTIPOCONT,  /*TIPO_CONTA*/
                             VSALDO,     /*SALDO*/
                             VLIMITE,    /*LIMITE*/
                             VID         /*CODIGO_CLIENTE*/
                             );
  COMMIT;
END LOOP;

FOR Lcntr IN 1..1000
LOOP

  VCOD_MOV := seq_movimentacoes_id.NEXTVAL;
  
  VDATAMOV := VDATAMOV + 1/24;

  SELECT NUMERO,SALDO,LIMITE
    INTO VCOD_CONTA,VCONTASALDO,VLIMITE
    FROM CONTAS
  WHERE NUMERO = (select round(dbms_random.value(1,10)) from dual);

  select CASE round(dbms_random.value(1,2))
    WHEN 1 THEN 'C'
    WHEN 2 THEN 'D'
  END
  INTO VTIPOMOV
  from dual;

  select CASE VTIPOMOV
    WHEN 'C' THEN 'CREDITO EM CONTA'
    WHEN 'D' THEN 'DÉBITO EM CONTA'
  END
  INTO VDESC
  from dual;

  SELECT round(dbms_random.value(1,1000),2) 
    INTO VVALOR
  from dual;

  IF VTIPOMOV = 'D' THEN
    VSALDOANT := VCONTASALDO;
    VSALDOATU := VCONTASALDO - VVALOR;
    VVALOR := VVALOR*-1;
  ELSIF VTIPOMOV = 'C' THEN
    VSALDOANT := VCONTASALDO;
    VSALDOATU := VCONTASALDO + VVALOR;
  END IF;

  IF (VLIMITE*-1) <= VSALDOATU THEN

    UPDATE CONTAS
    SET saldo = VSALDOATU
    WHERE numero=VCOD_CONTA;

    INSERT INTO MOVIMENTACOES VALUES(VCOD_MOV,   /*CODIGO_MOVIMENTACAO*/
                                    VDATAMOV,    /*VALOR*/
                                    VDESC,  /*CODIGO_CONTA*/
                                    VVALOR,
                                    VSALDOANT,
                                    VSALDOATU,
                                    VCOD_CONTA     /*TIPO_MOV*/
                                    );
    COMMIT;
END IF;
  END LOOP;
END;