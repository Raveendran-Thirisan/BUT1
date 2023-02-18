Drop table if exists Bateau;
Drop table if exists Passengers;
create table Passengers(PassengersId integer primary key, Survived varchar(80), Age varchar(100), Sexe varchar(100),Name varchar(100),SibSp integer, Parch varchar(100));
create table Bateau (ticket varchar(100) ,Pclass varchar(100),cabin varchar(100),passengersId integer, primary key(ticket,passengersId),foreign key (PassengersId) references Passengers(PassengersId) );
\Copy passengers from passengers.txt
\copy Bateau from bateau.txt
