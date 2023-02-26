create database lalana;
\c lalana

drop table lalana cascade;
drop table pk cascade;
drop table simba cascade;
drop table couche cascade;
drop table couche_coord cascade;

create table lalana (
    idLalana serial primary key,
    nomLalana varchar(10),
    longueur double precision,  --km
    largeur double precision    --m
);

insert into lalana values
    (default, 'RN1', 149, 7.5),
    (default, 'RN2', 367, 7),
    (default, 'RN3', 91, 7.3),
    (default, 'RN4', 570, 7.2),
    (default, 'RN5', 402, 7.4),
    (default, 'RN6', 706, 7.1),
    (default, 'RN7', 956, 7)
;

create table pk (
    idPk serial primary key,
    coord geography(point),
    valeur double precision
);

insert into pk values
    (default, 'point(-18.983055 47.532568)', 25),
    (default, 'point(-18.994326 47.534231)', 27)
;

create table simba (
    idSimba serial primary key,
    idLalana int,
    idPk_debut int,
    idPk_fin int,
    niveau int,
    foreign key (idLalana) references lalana(idLalana),
    foreign key (idPk_debut) references pk(idPk),
    foreign key (idPk_fin) references pk(idPk)
);

insert into simba values
    (default, 7, 1, 2, 14)
;

create table couche (
    idCouche serial primary key,
    karazany varchar(30)
);

insert into couche values
    (default, 'ecole'),
    (default, 'hopital')
;

create table couche_coord (
    idCouche_coord serial primary key,
    idCouche int,
    coord geography(point),
    nom varchar(30),
    foreign key (idCouche) references couche(idCouche)
);

insert into couche_coord values
    (default, 1, 'point(-18.986021 47.532804)', 'IT University'),
    (default, 1, 'point(-18.993234 47.533721)', 'ISTS'),
    (default, 2, 'point(-18.919367 47.523027)', 'Hopital Befelatanana'),
    (default, 2, 'point(-18.889833 47.490656)', 'Hopital Manara-penitra')
;
