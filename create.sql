CREATE TABLE "item" (
	"id"	INTEGER,
	"name"	TEXT,
	"amount"	INTEGER,
	"price"	INTEGER,
	"info"	TEXT,
	"discount"	INTEGER,
	"url"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "users" (
	"id"	INTEGER,
	"login"	TEXT,
	"password"	TEXT,
	"registration_date"	TEXT,
	"birth_date"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "history" (
	"id"	INTEGER,
	"user_id"	INTEGER,
	"item_item"	INTEGER,
	"amount"	INTEGER,
	"discount"	INTEGER,
	"date"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);