DROP TABLE IF EXISTS testbeds;
CREATE TABLE testbeds (
    id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL,
    hostname TEXT NOT NULL,
    ip_id INTEGER NOT NULL,
    occupied_by INTEGER,
    rdp INTEGER,
    PRIMARY KEY(id AUTOINCREMENT)
);

DROP TABLE IF EXISTS ips;
CREATE TABLE ips (
    id INTEGER NOT NULL UNIQUE,
    ip TEXT UNIQUE,
    name TEXT NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
);

DROP TABLE IF EXISTS clients;
CREATE TABLE clients (
    id INTEGER NOT NULL UNIQUE,
    ip_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
);