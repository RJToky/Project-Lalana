create database lalana;
\c lalana

drop table typeLalana cascade;
drop table lalana cascade;
drop table pk cascade;
drop table simba cascade;
drop table typeCouche cascade;
drop table couche cascade;

create table typeLalana (
    idTypeLalana serial primary key,
    nomType varchar(15),
    prix double precision,
    duree double precision
);

insert into typeLalana values
    (default, 'Goudron', 6000, 5),
    (default, 'Pavee', 3000, 6)
;

create table lalana (
    idLalana serial primary key,
    nomLalana varchar(15),
    largeur double precision,
    idTypeLalana int,
    foreign key (idTypeLalana) references typeLalana(idTypeLalana)
);

insert into lalana values
    (default, 'RN1', 7.5, 1),
    (default, 'RN2', 7, 1),
    (default, 'RN3', 7.3, 1),
    (default, 'RN4', 7.2, 2),
    (default, 'RN5', 7.4, 1),
    (default, 'RN6', 7.1, 2),
    (default, 'RN7', 7, 1)
;

create table pk (
    idPk serial primary key,
    valeur double precision,
    idLalana int,
    coord geography(point),
    foreign key (idLalana) references lalana(idLalana)
);

insert into pk values
    (default, 25, 7, 'point(-18.965778 47.529815)'),
    (default, 28, 7, 'point(-18.994434 47.534318)'),
    (default, 25.5, 7, 'point(-18.965778 47.529815)')
;

create table simba (
    idSimba serial primary key,
    idPk_debut int,
    idPk_fin int,
    niveau int check(niveau between 0 and 101),
    foreign key (idPk_debut) references pk(idPk),
    foreign key (idPk_fin) references pk(idPk)
);

insert into simba values
    (default, 1, 2, 47)
;

create table typeCouche (
    idTypeCouche serial primary key,
    nomType varchar(15)
);

insert into typeCouche values
    (default, 'Etablissement'),
    (default, 'Hopital'),
    (default, 'Village')
;

create table couche (
    idCouche serial primary key,
    idTypeCouche int,
    coord geography(point),
    nbr int default 0,
    nom varchar(30),
    foreign key (idTypeCouche) references typeCouche(idTypeCouche)
);

insert into couche values
    (default, 1, 'point(-18.986021 47.532804)', default, 'IT University'),
    (default, 1, 'point(-18.993234 47.533721)', default, 'ISTS'),
    (default, 2, 'point(-18.919367 47.523027)', default, 'Hopital Befelatanana'),
    (default, 2, 'point(-18.889833 47.490656)', default, 'Hopital Manara-penitra'),
    (default, 3, 'point(-18.978590 47.533285)', 535, 'Village 1')
;

create or replace view coucheDetail as (
    select c.idCouche, c.idTypeCouche, tc.nomType, st_x(st_astext(c.coord)) x, st_y(st_astext(c.coord)) y, c.nbr, c.nom, st_astext(c.coord) coord
    from couche c
    natural join typeCouche tc
);

create or replace view simbaDetail as (
    select s.idSimba, st_x(st_astext(pk1.coord)) x_debut, st_y(st_astext(pk1.coord)) y_debut, st_x(st_astext(pk2.coord)) x_fin, st_y(st_astext(pk2.coord)) y_fin, pk1.coord coord_debut, pk2.coord coord_fin
    from simba s
    join pk pk1 on s.idPk_debut = pk1.idPk
    join pk pk2 on s.idPk_fin = pk2.idPk
);
