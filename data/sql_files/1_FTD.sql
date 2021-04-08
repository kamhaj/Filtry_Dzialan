CREATE TABLE IF NOT EXISTS FTD (
    id_ftd INTEGER NOT NULL,
    nazwa VARCHAR(100) NOT NULL,
    opis VARCHAR(300) NULL,
	data_utworzenia DATE NOT NULL,
	PRIMARY KEY(id_ftd),
	CHECK(length(nazwa) >= 3)
);
