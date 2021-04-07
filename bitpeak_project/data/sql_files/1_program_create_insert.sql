CREATE TABLE IF NOT EXISTS PROGRAM (
	ID_PROGRAM INTEGER NOT NULL, 
	NAZWA VARCHAR(100) NOT NULL,
	PRIMARY KEY (ID_PROGRAM),
	CHECK(length(NAZWA) >= 3)
);

/*
INSERT INTO PROGRAM (NAZWA) VALUES ('The ENI Cross-border Cooperation Programme Poland-Belarus-Ukraine 2014-2020'),
('The ENI Cross-border Cooperation Programme Poland-Russia 2014-2020'),
('Program Współpracy Interreg V-A Polska – Słowacja'),
('Program Współpracy Interreg V-A Polska – Saksonia'),
('Program Operacyjny Inteligentny Rozwój'),
('Program Operacyjny Infrastruktura i Środowisko 2014-2020'),
('Program Operacyjny Polska Cyfrowa'),
('Program Operacyjny Pomoc Techniczna 2014-2020'),
('Program Operacyjny Polska Wschodnia'),
('Program Operacyjny Wiedza Edukacja Rozwój'),
('Regionalny Program Operacyjny Województwa Dolnośląskiego 2014-2020'),
('Regionalny Program Operacyjny Województwa Kujawsko-Pomorskiego na lata 2014-2020'),
('Regionalny Program Operacyjny – Lubuskie 2020'),
('Regionalny Program Operacyjny Województwa Łódzkiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Lubelskiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Mazowieckiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Małopolskiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Opolskiego 2014-2020'),
('Regionalny Program Operacyjny Województwa Podlaskiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Podkarpackiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Pomorskiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Śląskiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Świętokrzyskiego na lata 2014-2020'),
('Regionalny Program Operacyjny Województwa Warmińsko-Mazurskiego na lata 2014-2020'),
('Wielkopolski Regionalny Program Operacyjny na lata 2014 – 2020'),
('Regionalny Program Operacyjny Województwa Zachodniopomorskiego 2014-2020'),
('South Baltic Cross-border Co-operation Programme 2014-2020');
*/