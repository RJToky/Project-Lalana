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
    (default, 'point(-18.986367 47.532749)', 25),
    (default, 'point(-18.986773 47.532481)', 25.4),
    (default, 'point(-18.992064 47.532851)', 28),
    (default, 'point(-18.993286 47.533693)', 28.5)
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
    (default, 7, 1, 2, 14),
    (default, 7, 3, 4, 10)
;

create table couche (
    idCouche serial primary key,
    karazany varchar(30)
);

insert into couche values
    (default, 'school'),
    (default, 'hospital'),
    (default, 'hotel'),
    (default, 'population')
;

create table couche_coord (
    idCouche_coord serial primary key,
    idCouche int,
    coord geography(point),
    nom varchar(30),
    nbr int,
    foreign key (idCouche) references couche(idCouche)
);

insert into couche_coord values
    (default, 1, 'point(-18.986021 47.532804)', 'IT University', 1),
    (default, 1, 'point(-18.993234 47.533721)', 'ISTS', 1),
    (default, 2, 'point(-18.919367 47.523027)', 'Hopital Befelatanana', 1),
    (default, 2, 'point(-18.889833 47.490656)', 'Hopital Manara-penitra', 1),
    (default, 4, 'point(-18.978590 47.533285)', 'Population 1', 535)
;

create or replace view couche_detail as (
    select cc.idCouche_coord, c.karazany, st_x(st_astext(cc.coord)) x, st_y(st_astext(cc.coord)) y, cc.nom, c.idCouche, st_astext(cc.coord) coord, cc.nbr
    from couche c
    natural join couche_coord cc
);

create or replace view simba_detail as (
    select simba.idSimba, st_x(st_astext(pk1.coord)) x_debut, st_y(st_astext(pk1.coord)) y_debut, st_x(st_astext(pk2.coord)) x_fin, st_y(st_astext(pk2.coord)) y_fin, pk1.coord coord_debut, pk2.coord coord_fin
    from simba
    join pk pk1 on simba.idPk_debut = pk1.idPk
    join pk pk2 on simba.idPk_fin = pk2.idPk
);