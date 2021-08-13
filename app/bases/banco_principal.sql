BEGIN TRANSACTION;
DROP TABLE IF EXISTS "change";
CREATE TABLE IF NOT EXISTS "change" (
	"token"	TEXT,
	"lhost"	TEXT,
	"data_hora"	TEXT
);