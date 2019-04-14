create database PharmaDBTest;

use PharmaDBTest;

create table TestTypeClass(TypeID varchar(4) primary key, TypeName varchar(30), DemandAmt int(3), AvbltyAmt int(3), StockLimt int(5));

create table TestProfitTab(TransactID int(4) primary key auto_increment, MedicNomen varchar(30), EarnedCash int(4));

create table TestManufacts(MfgrID varchar(4) primary key, MfgName varchar(30), Country varchar(30), IfAvail varchar(30), IfPrice int(3), UserRev varchar(10), MakesAnPy int(1), MakesAnGe int(1), MakesAnBi int(1), MakesAnSe int(1), MakesMoSt int(1), MakesStim int(1), MakesTran int(1));

create table TestMedicines(MedicineID varchar(4) primary key, MedName varchar(30), MedTypeID varchar(4), MedMfgrID varchar(4), MfgDate date, ExpDate date, IsAntiPytc int(1), IsAnalGesc int(1), IsAntiBiot int(1), IsAntiSept int(1), IsMoodStab int(1), IsStimulan int(1), IsTranquil int(1), foreign key(MedTypeID) references TestTypeClass(TypeID), foreign key(MedMfgrID) references TestManufacts(MfgrID));

create table TestWarehouse(InvID varchar(4) primary key, WareMedID varchar(4), StckLimit int(4), MfgWareDt date, ExpWareDt date, foreign key(WareMedID) references TestMedicines(MedicineID));

create table TestUserCreds(StoreUser varchar(30) primary key, StorePass varchar(30));

create table TestMedPrices(PricID varchar(4) primary key, MediID varchar(4), BasePrice int(3), ProductTx int(3), TotalPric int(3), foreign key (MediID) references TestMedicines(MedicineID));

drop table TestTypeClass;

drop table TestManufacts;

drop table TestMedicines;

drop table TestWarehouse;

drop table TestMedPrices;

drop table TestProfitTab;

select * from TestTypeClass;

select * from TestManufacts;

select * from TestMedicines;

select * from TestWarehouse;

select * from TestMedPrices;

select * from TestProfitTab;

LOAD DATA INFILE "/var/lib/mysql-files/TestTypeClass.csv"
INTO TABLE TestTypeClass
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE "/var/lib/mysql-files/TestManufacts.csv"
INTO TABLE TestManufacts
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE "/var/lib/mysql-files/TestMedicines.csv"
INTO TABLE TestMedicines
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE "/var/lib/mysql-files/TestWarehouseWO.csv"
INTO TABLE TestWarehouse
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA INFILE "/var/lib/mysql-files/TestMedPrices.csv"
INTO TABLE TestMedPrices
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

desc TestTypeClass;

desc TestManufacts;

desc TestWarehouse;

desc TestMedicines;

desc TestMedPrices;

desc TestProfitTab;
