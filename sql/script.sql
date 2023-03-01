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
    (default, 'Pave', 3000, 6)
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
    (default, 9, 7, 'point(-18.965778 47.529815)'),
    (default, 10, 7, 'point(-18.978743 47.532961)'),
    (default, 11, 7, 'point(-18.991739 47.532650)'),
    (default, 12, 7, 'point(-19.002072 47.537811)'),
    (default, 13, 7, 'point(-19.016187 47.537948)'),
    (default, 14, 7, 'point(-19.026325 47.544493)'),
    (default, 15, 7, 'point(-19.040620 47.545030)'),
    (default, 16, 7, 'point(-19.054478 47.545459)')
;

-- select st_distance(
--     st_makePoint(-19.040620, 47.545030)::geography,
--     st_makePoint(-19.054478, 47.545459)::geography
-- );

create table simba (
    idSimba serial primary key,
    idPk_debut int,
    idPk_fin int,
    niveau int check(niveau between 0 and 100),
    foreign key (idPk_debut) references pk(idPk),
    foreign key (idPk_fin) references pk(idPk)
);

insert into simba values
    (default, 1, 4, 47),
    (default, 6, 7, 14)
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

-- View

create or replace view coucheDetail as (
    select c.idCouche, c.idTypeCouche, tc.nomType, st_x(st_astext(c.coord)) x, st_y(st_astext(c.coord)) y, c.nbr, c.nom, c.coord coord
    from couche c
    natural join typeCouche tc
);

create or replace view simbaDetail as (
    select s.idSimba, s.idPk_debut, s.idPk_fin, st_x(st_astext(pk1.coord)) x_debut, st_y(st_astext(pk1.coord)) y_debut, st_x(st_astext(pk2.coord)) x_fin, st_y(st_astext(pk2.coord)) y_fin, pk1.coord coord_debut, pk2.coord coord_fin
    from simba s
    join pk pk1 on s.idPk_debut = pk1.idPk
    join pk pk2 on s.idPk_fin = pk2.idPk
);

create or replace view lalanaDetail as (
    select l.*, t.nomType, t.prix, t.duree, calc_cout_rn(l.idLalana) cout
    from lalana l
    join typeLalana t on l.idTypeLalana = t.idTypeLalana
);

-- Function

create or replace function couche_doublon_inclus(id_lalana int, rayon double precision)
returns table (idcouche int, idtypecouche int, nomtype varchar(15), x double precision, y double precision, nbr int, nom varchar(30), coord geography(point))
language plpgsql
as $$
declare
r1 record;
r2 record;

begin
    for r1 in (select * from pk where pk.idLalana = id_lalana order by pk.valeur asc)
    loop
        for r2 in (select * from coucheDetail cd where st_dwithin(cd.coord, (select pk.coord from pk where pk.idPk = r1.idPk), rayon))
        loop
            idcouche := r2.idcouche;
            idtypecouche := r2.idtypecouche;
            nomtype := r2.nomtype;
            x := r2.x;
            y := r2.y;
            nbr := r2.nbr;
            nom := r2.nom;
            coord := r2.coord;
            return next;
        end loop;
    end loop;
end;
$$;

-- Supprimer les doublons
create or replace function find_couche_in_lalana(id_lalana int, rayon double precision)
returns table (idcouche int, idtypecouche int, nomtype varchar(15), x double precision, y double precision, nbr int, nom varchar(30), coord geography(point))
language plpgsql
as $$
declare
r record;

begin
    for r in (select f.idcouche, f.idtypecouche, f.nomtype, f.x, f.y, f.nbr, f.nom, f.coord from couche_doublon_inclus(id_lalana, rayon) f group by f.idcouche, f.idtypecouche, f.nomtype, f.x, f.y, f.nbr, f.nom, f.coord)
    loop
        idcouche := r.idcouche;
        idtypecouche := r.idtypecouche;
        nomtype := r.nomtype;
        x := r.x;
        y := r.y;
        nbr := r.nbr;
        nom := r.nom;
        coord := r.coord;
        return next;
    end loop;
end;
$$;

create or replace function calc_cout_rn(id_lalana int)
returns double precision
language plpgsql
as $$
declare
r record;
longueur double precision;
profondeur double precision;
retour double precision;

begin
    retour := 0;
    for r in (select s.niveau, t.prix, l.largeur, p1.valeur pk_debut, p2.valeur pk_fin from simba s join pk p1 on s.idPk_debut = p1.idPk join pk p2 on s.idPk_fin = p2.idPk join lalana l on p1.idLalana = l.idLalana join typeLalana t on l.idTypeLalana = t.idTypeLalana where l.idLalana = id_lalana)
    loop
        longueur := (r.pk_fin - r.pk_debut) * 1000;
        profondeur := (r.niveau) * 0.001;
        retour := retour + (longueur * profondeur * r.largeur * r.prix);
    end loop;
    return retour;
end;
$$;
