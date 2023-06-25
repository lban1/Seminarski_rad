CREATE TABLE table_narucitelji (
id_narucitelja INTEGER PRIMARY KEY,
ime CHAR(50) NOT NULL,
prezime CHAR(50) NOT NULL,
telefon VARCHAR(50) NOT NULL,
email CHAR(50) NOT NULL,
id_dob TINYINT,
id_luk TINYINT,
FOREIGN KEY (id_dob) REFERENCES table_dob_narucitelja(id) ON UPDATE CASCADE ON DELETE SET NULL,
FOREIGN KEY (id_luk) REFERENCES table_lukovi(id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE table_lukovi (
id INTEGER PRIMARY KEY AUTOINCREMENT,
naziv CHAR(50) NOT NULL
);

CREATE TABLE table_dob_narucitelja (
id INTEGER PRIMARY KEY AUTOINCREMENT,
dob CHAR(50) NOT NULL
);

INSERT INTO table_lukovi (naziv) VALUES
    ('Djecji'),
    ('Longbow'),
    ('Shortbow'),
    ('Recurve bow'),
    ('Reflex bow');

INSERT INTO table_dob_narucitelja (dob) VALUES
    ('Djete'),
    ('Adolescenti'),
    ('Odrasli'),
    ('Stari');