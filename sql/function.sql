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