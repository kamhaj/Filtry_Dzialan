/*
tabela FILTRY_ELEMENTY przechowuje strukturę, z której składa się dany Filtr Działań
(id_ftd_element – unikalny sztuczny identyfikator elementu FiltraDziałań,
id_ftd – identyfikator FiltraDziałań, do którego przynależy dany element, 
id_dzl – identyfikator Działania przypisanego do Filtra Działań)

Samymi elementami Filtra Działań są identyfikatory Działań z tabel słownikowych 
(każde z Działań jednoznacznie określa Oś i Program, do którego przynależy).
*/

-- leave default polish column names
CREATE TABLE IF NOT EXISTS FTD_ELEMENTY (
    id_ftd_element INTEGER NOT NULL,
    id_ftd INTEGER NOT NULL,
    id_dzialanie INTEGER NOT NULL,	-- z innych tabel wiemy do jakiego Programu i Ośi to działanie przynależy
	PRIMARY KEY(id_ftd_element),
	FOREIGN KEY(id_ftd)
);



/*
oryginalna tabela

CREATE TABLE FTD_ELEMENTY (
    id_ftd_element INTEGER NOT NULL,
    id_ftd INTEGER NOT NULL,
    id_dzialanie INTEGER NOT NULL
);
*/