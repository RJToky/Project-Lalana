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