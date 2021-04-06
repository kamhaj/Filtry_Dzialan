CREATE TABLE IF NOT EXISTS FTD_ELEMENTY (
    id_ftd_element INTEGER NOT NULL,
    id_ftd INTEGER NOT NULL,
    id_dzialanie INTEGER NOT NULL,	
	PRIMARY KEY (id_ftd_element),
	FOREIGN KEY (id_ftd) REFERENCES FTD(id_ftd)
);