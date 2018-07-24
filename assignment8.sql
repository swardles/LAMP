DROP TABLE IF EXISTS c;
DROP TABLE IF EXISTS images;

CREATE TABLE c (
	state VARCHAR(32),
	geoid VARCHAR(32),
	code VARCHAR(32),
	name VARCHAR(32),
	population int,
	housing_units int,
	land_area_meters int,
	water_area_meters decimal(20,8),
	land_area_miles decimal(20,8),
	water_area_miles decimal(20,8),
	lat decimal(20,8),
	longg decimal(20,8),
	PRIMARY KEY(code)
	);

LOAD DATA LOCAL INFILE 'text.txt'
INTO TABLE c;