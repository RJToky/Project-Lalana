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
    (default, 'Goudron', 6000, 1),
    (default, 'Pave', 4570, 1)
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
    (default, 'RN3', 9, 1),
    (default, 'RN4', 7.2, 2),
    (default, 'RN5', 10, 2),
    (default, 'RN6', 7.1, 2),
    (default, 'RN7', 8.4, 2),
    (default, 'RN8', 5, 1)
;

create table pk (
    idPk serial primary key,
    valeur double precision,
    idLalana int,
    coord geography(point),
    foreign key (idLalana) references lalana(idLalana)
);

insert into pk values
    (default, 2, 2, 'point(-18.901530 47.539956)'),
    (default, 10, 2, 'point(-18.898739 47.545299)'),
    (default, 30, 2, 'point(-18.888481 47.626346)'),
    (default, 55, 2, 'point(-18.881906 47.634944)'),
    (default, 107, 2, 'point(-18.870505 47.655291)'),

    (default, 7, 7, 'point(-18.919501 47.521670)'),
    (default, 25, 7, 'point(-18.920985 47.521437)'),
    (default, 35, 7, 'point(-18.957140 47.529498)'),
    (default, 47, 7, 'point(-18.962610 47.529661)'),
    (default, 50, 7, 'point(-18.985933 47.532992)'),

    (default, 40, 5, 'point(-17.257263 49.405997)'),
    (default, 56, 5, 'point(-17.253031 49.407703)'),
    (default, 70, 5, 'point(-17.333246 49.409245)'),
    (default, 84, 5, 'point(-17.323383 49.409049)'),
    (default, 100, 5, 'point(-17.288047 49.404222)'),

    (default, 23, 3, 'point(-18.880267 47.543057)'),
    (default, 28, 3, 'point(-18.875354 47.548411)'),
    (default, 39, 3, 'point(-18.855969 47.553096)'),
    (default, 47, 3, 'point(-18.851328 47.555459)'),
    (default, 66, 3, 'point(-18.823710 47.558661)'),
    
    (default, 300, 8, 'POINT(-18.147246 49.389650)'),
    (default, 301, 8, 'POINT(-18.137295 49.397847)'),
    (default, 301.5, 8, 'POINT(-18.133624 49.399392)'),
    (default, 302, 8, 'POINT(-18.128743 49.400165)'),
    (default, 302.5, 8, 'POINT(-18.122071 49.399264)'), --start 25
    (default, 302.8, 8, 'POINT(-18.120686 49.398983)'), --end 26
    (default, 302.3, 8, 'POINT(-18.115891 49.396473)'),
    (default, 302.5, 8, 'POINT(-18.109202 49.394649)'),
    (default, 304, 8, 'POINT(-18.089796 49.393409)'),
    (default, 304.1, 8, 'POINT(-18.088225 49.392980)'), --start 30
    (default, 304.2, 8, 'POINT(-18.087573 49.392658)')   --end 31
;

create table simba (
    idSimba serial primary key,
    idPk_debut int,
    idPk_fin int,
    niveau int check(niveau between 0 and 100),
    foreign key (idPk_debut) references pk(idPk),
    foreign key (idPk_fin) references pk(idPk)
);

insert into simba values
    (default, 1, 2, 47),
    (default, 3, 4, 80),
    (default, 6, 7, 56),
    (default, 8, 9, 34),
    (default, 11, 12, 30),
    (default, 13, 14, 67),
    (default, 16, 17, 54),
    (default, 18, 19, 27),
    (default, 25, 26, 24),
    (default, 30, 31, 62)
;

create table typeCouche (
    idTypeCouche serial primary key,
    nomType varchar(15)
);

insert into typeCouche values
    (default, 'Etablissement'),
    (default, 'Hopital'),
    (default, 'Hotel'),
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
    (default, 2, 'point(-18.901208 47.540016)', default, 'HJRA'),
    (default, 2, 'point(-18.901749 47.540662)', default, 'Clinique Ily'),
    (default, 2, 'point(-18.899246 47.544376)', default, 'Maternité As'),
    (default, 2, 'point(-18.874038 47.654851)', default, 'IlafyC'),
    (default, 2, 'point(-18.919349 47.523183)', default, 'St André'),
    (default, 2, 'point(-18.956328 47.525067)', default, 'Avaradoha Maté'),
    (default, 2, 'point(-18.964103 47.528400)', default, 'Ostie'),
    (default, 2, 'point(-17.265764 49.405137)', default, 'Manarapé'),
    (default, 2, 'point(-17.333062 49.409921)', default, 'Andravoahangy'),
    (default, 2, 'point(-17.316674 49.401549)', default, 'Ankadifotsy'),
    (default, 2, 'point(-17.278048 49.408481)', default, 'Korama'),
    (default, 2, 'point(-18.876197 47.551844)', default, 'KSI'),
    (default, 2, 'point(-18.854938 47.550163)', default, 'St Marielle'),
    (default, 2, 'point(-18.828951 47.551363)', default, 'Oreo'),
    (default, 1, 'point(-18.896370 47.545465)', default, 'SFX'),
    (default, 1, 'point(-18.886026 47.632612)', default, 'StMichel'),
    (default, 1, 'point(-18.869825 47.651707)', default, 'Amparibe'),
    (default, 1, 'point(-18.868749 47.658713)', default, 'Francois'),
    (default, 1, 'point(-18.921602 47.523011)', default, 'Pepiniere'),
    (default, 1, 'point(-18.926318 47.516141)', default, 'LMA'),
    (default, 1, 'point(-18.965390 47.530140)', default, 'Epp'),
    (default, 1, 'point(-18.986037 47.532560)', default, 'IT University'),
    (default, 1, 'point(-18.988035 47.529528)', default, 'Lycée'),
    (default, 1, 'point(-17.255430 49.415376)', default, 'Parc des P'),
    (default, 1, 'point(-17.323219 49.412450)', default, 'ISTS'),
    (default, 1, 'point(-17.284984 49.406292)', default, 'ETI'),
    (default, 1, 'point(-18.884399 47.545889)', default, 'Enam'),
    (default, 1, 'point(-18.852229 47.557134)', default, 'Bird'),
    (default, 1, 'point(-18.841733 47.550382)', default, 'Alliance'),
    (default, 4, 'point(-18.887355 47.625445)', 634, 'Cité'),
    (default, 4, 'point(-18.868048 47.656084)', 134, 'Village TR'),
    (default, 4, 'point(-18.921125 47.519385)', 98, 'Kolotsaina'),
    (default, 4, 'point(-18.923745 47.521330)', 103, 'Kromania'),
    (default, 4, 'point(-18.961006 47.526569)', 129, 'Alakrima'),
    (default, 4, 'point(-18.958205 47.535742)', 87, 'Korinty'),
    (default, 4, 'point(-18.990481 47.532447)', 359, 'Ivandry'),
    (default, 4, 'point(-17.259061 49.414135)', 245, 'Soavina'),
    (default, 4, 'point(-17.333820 49.414706)', 124, 'Okalou'),
    (default, 4, 'point(-17.317084 49.409746)', 63, 'Antokotany'),
    (default, 4, 'point(-18.884714 47.537220)', 131, 'Betavoahangy'),
    (default, 4, 'point(-18.878989 47.541404)', 167, 'Malaza'),
    (default, 4, 'point(-18.823080 47.562373)', 182, 'Fietrana'),

    (default, 4, 'POINT(-18.142172 49.395385)', 10000, 'Toamasina'),
    (default, 1, 'POINT(-18.140156 49.397235)', default, 'EPP Lovasoa'),
    (default, 4, 'POINT(-18.137324 49.395273)', 500, 'Cite Haras'),
    (default, 3, 'POINT(-18.131494 49.400543)', default, 'Chez Diata')
;

-- View

create or replace view coucheDetail as (
    select c.idCouche, c.idTypeCouche, tc.nomType, st_x(st_astext(c.coord)) x, st_y(st_astext(c.coord)) y, c.nbr, c.nom, c.coord coord
    from couche c
    natural join typeCouche tc
);

create or replace view simbaDetail as (
    select s.idSimba, pk1.idLalana, s.idPk_debut, s.idPk_fin, st_x(st_astext(pk1.coord)) x_debut, st_y(st_astext(pk1.coord)) y_debut, st_x(st_astext(pk2.coord)) x_fin, st_y(st_astext(pk2.coord)) y_fin, pk1.coord coord_debut, pk2.coord coord_fin
    from simba s
    join pk pk1 on s.idPk_debut = pk1.idPk
    join pk pk2 on s.idPk_fin = pk2.idPk
);

create or replace view lalanaDetail as (
    select l.*, t.nomType, calc_cout_rn(l.idLalana) coutReparation, calc_duree_rn(l.idLalana) dureeReparation
    from lalana l
    join typeLalana t on l.idTypeLalana = t.idTypeLalana
);

create or replace view pkDetail as (
    select p.*, st_x(st_astext(p.coord)) x, st_y(st_astext(p.coord)) y, l.nomLalana, l.largeur
    from pk p join lalana l on p.idLalana = l.idLalana
);

-- Function

-- select * from pk where pk.idLalana = id_lalana order by pk.valeur asc

-- select *
-- from pkDetail pd
-- where (pd.coord in (select sd.coord_debut from simbaDetail sd)
-- or pd.coord in (select sd.coord_fin from simbaDetail sd)) and pd.idLalana = id_lalana
-- order by pd.valeur asc

-- select *
-- from pk p
-- where p.idLalana = id_lalana and p.valeur
-- between (
--     select p1.valeur v1
--     from simba s
--     join pk p1 on s.idPk_debut = p1.idPk
--     join pk p2 on s.idPk_fin = p2.idPk
--     where s.idSimba = r.idSimba
-- ) and (
--     select p2.valeur v2
--     from simba s join pk p1 on s.idPk_debut = p1.idPk
--     join pk p2 on s.idPk_fin = p2.idPk
--     where s.idSimba = r.idSimba
-- ) order by p.valeur asc

create or replace function couche_doublon_inclus(id_lalana int, rayon double precision)
returns table (idcouche int, idtypecouche int, nomtype varchar(15), x double precision, y double precision, nbr int, nom varchar(30), coord geography(point))
language plpgsql
as $$
declare
r record;
r1 record;
r2 record;

begin
    for r in (select * from simbaDetail sd where sd.idLalana = id_lalana)
    loop
        for r1 in (
            select *
            from pk p
            where p.idLalana = id_lalana and p.valeur
            between (
                select p1.valeur v1
                from simba s
                join pk p1 on s.idPk_debut = p1.idPk
                join pk p2 on s.idPk_fin = p2.idPk
                where s.idSimba = r.idSimba
            ) and (
                select p2.valeur v2
                from simba s join pk p1 on s.idPk_debut = p1.idPk
                join pk p2 on s.idPk_fin = p2.idPk
                where s.idSimba = r.idSimba
            ) order by p.valeur asc)
        loop
            if rayon < 0 then
                for r2 in (
                    select *
                    from coucheDetail cd)
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
            else
                for r2 in (
                    select *
                    from coucheDetail cd
                    where st_dwithin(cd.coord, (select pk.coord from pk where pk.idPk = r1.idPk), rayon))
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
            end if;
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

create or replace function calc_duree_rn(id_lalana int)
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
    for r in (select s.niveau, t.duree, l.largeur, p1.valeur pk_debut, p2.valeur pk_fin from simba s join pk p1 on s.idPk_debut = p1.idPk join pk p2 on s.idPk_fin = p2.idPk join lalana l on p1.idLalana = l.idLalana join typeLalana t on l.idTypeLalana = t.idTypeLalana where l.idLalana = id_lalana)
    loop
        longueur := (r.pk_fin - r.pk_debut) * 1000;
        profondeur := (r.niveau) * 0.001;
        retour := retour + (longueur * profondeur * r.largeur * r.duree);
    end loop;
    return retour;
end;
$$;

create or replace function trier_par_nbr_couche(id_typeCouche int, rayon double precision)
returns table (nomLalana varchar(15), nomType varchar(15), nbr int)
language plpgsql
as $$
declare
r1 record;

begin
    for r1 in (select * from lalana)
    loop
        nomLalana := r1.nomLalana;
        nomType := (select t.nomType nomType from typeCouche t where t.idTypeCouche = id_typeCouche);
        if id_typeCouche = 4 then
            nbr := (select coalesce(sum(f.nbr), 0) nbr from  find_couche_in_lalana(r1.idLalana, rayon) f where f.idTypeCouche = id_typeCouche);
        else
            nbr := (select count(f.*) nbr from  find_couche_in_lalana(r1.idLalana, rayon) f where f.idTypeCouche = id_typeCouche);
        end if;
        return next;
    end loop;
end;
$$;


-- insert into pk values
--     (default, 9, 7, 'point(-18.965778 47.529815)'),
--     (default, 10, 7, 'point(-18.978743 47.532961)'),
--     (default, 11, 7, 'point(-18.991739 47.532650)'),
--     (default, 12, 7, 'point(-19.002072 47.537811)'),
--     (default, 13, 7, 'point(-19.016187 47.537948)'),
--     (default, 14, 7, 'point(-19.026325 47.544493)'),
--     (default, 15, 7, 'point(-19.040620 47.545030)'),
--     (default, 16, 7, 'point(-19.054478 47.545459)')
-- ;

-- insert into simba values
--     (default, 1, 4, 47),
--     (default, 6, 7, 14)
-- ;

-- insert into typeCouche values
--     (default, 'Etablissement'),
--     (default, 'Hopital'),
--     (default, 'Village')
-- ;

-- insert into couche values
--     (default, 1, 'point(-18.986021 47.532804)', default, 'IT University'),
--     (default, 1, 'point(-18.993234 47.533721)', default, 'ISTS'),
--     (default, 2, 'point(-18.919367 47.523027)', default, 'Hopital Befelatanana'),
--     (default, 2, 'point(-18.889833 47.490656)', default, 'Hopital Manara-penitra'),
--     (default, 3, 'point(-18.978590 47.533285)', 535, 'Village 1')
-- ;

-- select st_distance(
--     st_makePoint(-19.040620, 47.545030)::geography,
--     st_makePoint(-19.054478, 47.545459)::geography
-- );