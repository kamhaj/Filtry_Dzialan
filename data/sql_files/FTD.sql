/* 
Tabela FTD zawiera pojedyncze wpisy na temat zapisanego Filtra Działań 
(id_ftd – unikalny sztucznyidentyfikator Filtra Działań,
nazwa – nazwa nadawana przez użytkownika, 
opis – opis nadawany przez użytkownika)
*/

-- leave default polish column names
CREATE TABLE IF NOT EXISTS FTD (
    id_ftd INTEGER NOT NULL,
    nazwa TEXT NOT NULL,
    opis TEXT NULL,
	PRIMARY KEY(id_ftd),
	CHECK(length(nazwa) >= 3)  -- 'nazwa' longer than 2 characrers, can add additionals checks
);


/*
oryginalna tabela

CREATE TABLE FTD (
    id_ftd INTEGER NOT NULL,
    nazwa TEXT NOT NULL,
    opis TEXT NULL
);
*/