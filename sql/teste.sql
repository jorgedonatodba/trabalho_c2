CREATE TABLE FORNECEDORES (
                CNPJ VARCHAR2(14) NOT NULL,
                RAZAO_SOCIAL VARCHAR2(255) NOT NULL,
                NOME_FANTASIA VARCHAR2(255) NOT NULL,
                CONSTRAINT FORNECEDORES_PK PRIMARY KEY (CNPJ)
);

/*
alter session set CONTAINER=FREEPDB1;
drop user ivie cascade;
create user ivie identified by ivie;
grant dba to ivie;
*/

select CASE round(dbms_random.value(1,2))
    WHEN 1 THEN 'C'
    CASE round(dbms_random.value(1,2))
        WHEN 1 THEN 'C'
        WHEN 2 THEN 'D'
    END
    WHEN 2 THEN 'D'
    CASE round(dbms_random.value(1,2))
        WHEN 1 THEN 'C'
        WHEN 2 THEN 'D'
    END
END
from dual;



select CASE round(dbms_random.value(1,2))
    WHEN 1 THEN 'C'
    WHEN 2 THEN 'D'
END
from dual;


select * from c##ivie.clientes;


  select id,  numero,  tipo,  saldo,  limite,  id_cliente from contas 


