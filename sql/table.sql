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

create table lalana (
    idLalana serial primary key,
    nomLalana varchar(15),
    largeur double precision,
    idTypeLalana int,
    foreign key (idTypeLalana) references typeLalana(idTypeLalana)
);

create table pk (
    idPk serial primary key,
    valeur double precision,
    idLalana int,
    coord geography(point),
    foreign key (idLalana) references lalana(idLalana)
);

create table simba (
    idSimba serial primary key,
    idPk_debut int,
    idPk_fin int,
    niveau int check(niveau between 0 and 100),
    foreign key (idPk_debut) references pk(idPk),
    foreign key (idPk_fin) references pk(idPk)
);

create table typeCouche (
    idTypeCouche serial primary key,
    nomType varchar(15)
);

create table couche (
    idCouche serial primary key,
    idTypeCouche int,
    coord geography(point),
    nbr int default 0,
    nom varchar(30),
    foreign key (idTypeCouche) references typeCouche(idTypeCouche)
);

-- select st_distance(
--     st_makePoint(-19.040620, 47.545030)::geography,
--     st_makePoint(-19.054478, 47.545459)::geography
-- );