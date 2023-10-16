--DROP VIEWS
DROP VIEW  view_saldo_contas;
DROP VIEW  view_movimentacoes;
DROP VIEW  view_detalhes_clientes;

-- Deletando a tabela de movimentacoes, se existir
drop table movimentacoes CASCADE CONSTRAINTS purge;

-- Deletando a tabela de contas, se existir
drop table contas CASCADE CONSTRAINTS purge;

-- Deletando a tabela de clientes, se existir
drop table clientes CASCADE CONSTRAINTS purge;

-- Deletando a sequencia de clientes,  seq_clientes_id, se existir
DROP sequence seq_clientes_id;

-- Criando a sequência para a tabela de clientes
CREATE SEQUENCE seq_clientes_id;

-- Criando a tabela de clientes
CREATE TABLE clientes (
  id NUMBER NOT NULL,
  nome VARCHAR2(50) NOT NULL,
  cpf VARCHAR2(11) UNIQUE NOT NULL,
  endereco VARCHAR2(100) NOT NULL,
  telefone VARCHAR2(15) NOT NULL,
  CONSTRAINT clientes_PK PRIMARY KEY (id)
);

-- Deletando a sequencia de contas, seq_contas_numero, se existir
DROP SEQUENCE seq_contas_id;

-- Criando a sequência para a tabela de contas
CREATE SEQUENCE seq_contas_id;

-- Criando a tabela de contas
CREATE TABLE contas (
  id NUMBER NOT NULL,
  numero NUMBER NOT NULL,
  tipo VARCHAR2(10) CHECK (tipo IN ('corrente', 'poupanca', 'credito')),
  saldo NUMBER(10,2) NOT NULL,
  limite NUMBER(10,2) NOT NULL,
  id_cliente NUMBER NOT NULL,
  CONSTRAINT contas_PK PRIMARY KEY (numero),
  CONSTRAINT contas_fk FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

-- Deletando a sequencia de movimentacoes, seq_movimentacoes_id, se existir
DROP SEQUENCE  seq_movimentacoes_id;

-- Criando a sequência para a tabela de movimentacoes
CREATE SEQUENCE seq_movimentacoes_id;

-- Criando a tabela de movimentacoes
CREATE TABLE movimentacoes (
  id NUMBER NOT NULL,
  data DATE NOT NULL,
  descricao VARCHAR2(50) NOT NULL,
  valor NUMBER(10,2) NOT NULL,
  saldo_anterior NUMBER(10,2) NOT NULL,
  saldo_atual NUMBER(10,2) NOT NULL,
  numero_conta INT NOT NULL,
  CONSTRAINT movimentacoes_PK PRIMARY KEY (id),
  CONSTRAINT movimentacoes_fk FOREIGN KEY (numero_conta) REFERENCES contas(numero)
);

-- Criando a view de saldo das contas
CREATE VIEW view_saldo_contas AS
SELECT numero, tipo, saldo
FROM contas;

-- Criando a view de movimentacoes
CREATE VIEW view_movimentacoes AS
SELECT data, descricao, valor
FROM movimentacoes;

-- Criando a view de detalhes do cliente
CREATE VIEW view_detalhes_clientes AS
SELECT nome, cpf, endereco
FROM clientes;


-- Criando índice na tabela de contas
CREATE INDEX idx_contas_id_cliente ON contas (id_cliente);

-- Criando índice na tabela de movimentacoes
CREATE INDEX idx_movimentacoes_cont_num ON movimentacoes (numero_conta);
