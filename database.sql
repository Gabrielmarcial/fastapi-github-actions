-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

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