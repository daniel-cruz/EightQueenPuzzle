CREATE DATABASE eightqueens;
\c eightqueens
CREATE TABLE solutions (id int NOT NULL GENERATED ALWAYS AS IDENTITY,n int NOT NULL,solution text NOT NULL,CONSTRAINT solutions_pk PRIMARY KEY (id));