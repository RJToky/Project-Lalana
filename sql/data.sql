insert into typeLalana values
    (default, 'Goudron', 6000, 1),
    (default, 'Pave', 4570, 1)
;

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

insert into typeCouche values
    (default, 'Etablissement'),
    (default, 'Hopital'),
    (default, 'Hotel'),
    (default, 'Village')
;

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