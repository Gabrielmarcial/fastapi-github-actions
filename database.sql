
-- DROP SEQUENCE public.eletronicos_id_seq;

CREATE SEQUENCE public.eletronicos_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;-- public.eletronicos definition

-- Drop table

-- DROP TABLE public.eletronicos;

CREATE TABLE public.eletronicos (
	id serial4 NOT NULL,
	nome varchar(255) NULL,
	marca varchar(255) NULL,
	modelo varchar(255) NULL,
	preco numeric(10, 2) NULL,
	CONSTRAINT eletronicos_pkey PRIMARY KEY (id)
);

INSERT INTO eletronicos (nome, marca, modelo, preco) VALUES ('Smartphone', 'Apple', 'iPhone 13 Pro', 1099.99);
INSERT INTO eletronicos (nome, marca, modelo, preco) VALUES ('Laptop', 'Dell', 'XPS 13', 1299.99);
INSERT INTO eletronicos (nome, marca, modelo, preco) VALUES ('Televisão', 'Samsung', 'QLED 4K', 999.99);
INSERT INTO eletronicos (nome, marca, modelo, preco) VALUES ('Tablet', 'Samsung', 'Galaxy Tab S7', 649.99);
INSERT INTO eletronicos (nome, marca, modelo, preco) VALUES ('Câmera Digital', 'Canon', 'EOS Rebel T7i', 599.99);