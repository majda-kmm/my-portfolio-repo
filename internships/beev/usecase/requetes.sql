-- a. Total number of cars by model by country
SELECT 
    "Car Model",
    "Country",
    SUM("Sales Volume") AS total_sales
FROM car_reviews
GROUP BY "Car Model", "Country"
ORDER BY "Car Model", "Country";

/*  Car Model  | Country | total_sales 
-------------+---------+-------------
 124 spider  | France  |     1091154
 124 spider  | Germany |     1085161
 124 spider  | USA     |     1105590
 208         | France  |     2296774
 208         | Germany |     2170740
 208         | USA     |     2063343
 308         | France  |     2151590
 308         | Germany |     2178950
 308         | USA     |     2179891
 500         | France  |     3114757
 500         | Germany |     3227904
 500         | USA     |     3154031
 5008        | France  |     6670060
 5008        | Germany |     6489441
 5008        | USA     |     6377051
 500x        | France  |     1065332
 500x        | Germany |     1052300
 500x        | USA     |     1103586
 508         | France  |     2104745
 508         | Germany |     2056568
 508         | USA     |     2140226
 5 series    | France  |     3112136
 5 series    | Germany |     3361289
 5 series    | USA     |     3182984
 7 series    | France  |     5647610
 7 series    | Germany |     5368773
 7 series    | USA     |     5356643
 911         | France  |     2051045
 911         | Germany |     2144633
 911         | USA     |     2201418
 a4          | France  |     4288237
 a4          | Germany |     4556028
 a4          | USA     |     4295040
 a6          | France  |     1036587
 a6          | Germany |     1119014
 a6          | USA     |     1057596
 accord      | France  |     3238405
 accord      | Germany |     3142307
 accord      | USA     |     3236118
 altima      | France  |     4553658
 altima      | Germany |     4352182
 altima      | USA     |     4294569
 astra       | France  |     2167533
 astra       | Germany |     2183215
 astra       | USA     |     2213964
 atlas       | France  |     1045423
 atlas       | Germany |     1025528
 atlas       | USA     |     1030458
 bolt        | France  |     1097194
 bolt        | Germany |      957602
 bolt        | USA     |     1040208
 camry       | France  |     2172554
 camry       | Germany |     2198249
 camry       | USA     |     2094723
 captur      | France  |     3206624
 captur      | Germany |     3337181
 captur      | USA     |     3175861
 cayenne     | France  |     2224057
 cayenne     | Germany |     2096556
 cayenne     | USA     |     2050847
 c-class     | France  |     2156202
 c-class     | Germany |     2196147
 c-class     | USA     |     2022208
 civic       | France  |     4135384
 civic       | Germany |     4303380
 civic       | USA     |     4287404
 clio        | France  |     1102415
 clio        | Germany |     1067004
 clio        | USA     |     1121429
 corolla     | France  |     3480922
 corolla     | Germany |     3200501
 corolla     | USA     |     3205600
 corsa       | France  |     4356821
 corsa       | Germany |     4427332
 corsa       | USA     |     4128511
 crossland x | France  |     5369396
 crossland x | Germany |     5353738
 crossland x | USA     |     5367885
 cruze       | France  |     3275906
 cruze       | Germany |     3224788
 cruze       | USA     |     3252990
 cr-v        | France  |      977025
 cr-v        | Germany |     1085927
 cr-v        | USA     |     1087240
 cx-5        | France  |     3406545
 cx-5        | Germany |     3233901
 cx-5        | USA     |     3257206
 cx-9        | France  |     2106889
 cx-9        | Germany |     2238819
 cx-9        | USA     |     2136055
 elantra     | France  |     1159989
 elantra     | Germany |     1061003
 elantra     | USA     |     1078587
 enclave     | France  |     1007311
 enclave     | Germany |     1074110
 enclave     | USA     |     1116685
 envision    | France  |     7720788
 envision    | Germany |     7623697
 envision    | USA     |     7603567
 equinox     | France  |     3228002
 equinox     | Germany |     3158929
 equinox     | USA     |     3020125
 es          | France  |     5350305
 es          | Germany |     5138815
 es          | USA     |     5253723
 escape      | France  |     2072403
 escape      | Germany |     2095042
 escape      | USA     |     2158943
 e-tron      | France  |     1006644
 e-tron      | Germany |     1066150
 e-tron      | USA     |     1089811
 explorer    | France  |     5473155
 explorer    | Germany |     5479518
 explorer    | USA     |     5306090
 f-150       | France  |     3107246
 f-150       | Germany |     3155577
 f-150       | USA     |     3385942
 fit         | France  |     4379342
 fit         | Germany |     4241598
 fit         | USA     |     4371900
 forester    | France  |     3235608
 forester    | Germany |     3233019
 forester    | USA     |     3175402
 forte       | France  |     4383549
 forte       | Germany |     4317398
 forte       | USA     |     4310160
 f-pace      | France  |     6250621
 f-pace      | Germany |     6455641
 f-pace      | USA     |     6435501
 fusion      | France  |     1136278
 fusion      | Germany |     1043344
 fusion      | USA     |     1142379
 glc         | France  |     1058030
 glc         | Germany |     1064625
 glc         | USA     |     1102591
 gle         | France  |     3178270
 gle         | Germany |     3115124
 gle         | USA     |     3317676
 golf        | France  |     7405365
 golf        | Germany |     7518764
 golf        | USA     |     7734295
 grandland x | France  |     1113107
 grandland x | Germany |     1059194
 grandland x | USA     |     1098611
 gx          | France  |     1088600
 gx          | Germany |     1076717
 gx          | USA     |      980991
 highlander  | France  |     4282283
 highlander  | Germany |     4099465
 highlander  | USA     |     4231837
 impreza     | France  |      977178
 impreza     | Germany |     1086493
 impreza     | USA     |     1071660
 insignia    | France  |     1038613
 insignia    | Germany |     1034013
 insignia    | USA     |     1021220
 i-pace      | France  |     1104865
 i-pace      | Germany |     1089329
 i-pace      | USA     |     1071590
 jetta       | France  |     1134912
 jetta       | Germany |      994204
 jetta       | USA     |     1033628
 kadjar      | France  |     1163513
 kadjar      | Germany |     1109623
 kadjar      | USA     |     1056625
 leaf        | France  |     2041311
 leaf        | Germany |     2121958
 leaf        | USA     |     2222985
 legacy      | France  |     2115411
 legacy      | Germany |     2232956
 legacy      | USA     |     2168490
 ls          | France  |     5408838
 ls          | Germany |     5341619
 ls          | USA     |     5780281
 malibu      | France  |     2239711
 malibu      | Germany |     2241677
 malibu      | USA     |     1990584
 maxima      | France  |     2086858
 maxima      | Germany |     2342433
 maxima      | USA     |     2088643
 mazda3      | France  |     4161824
 mazda3      | Germany |     4223780
 mazda3      | USA     |     4349433
 mazda6      | France  |     2243593
 mazda6      | Germany |     2127644
 mazda6      | USA     |     2068254
 mdx         | France  |     4215895
 mdx         | Germany |     4283664
 mdx         | USA     |     4464511
 megane      | France  |     2159512
 megane      | Germany |     2106388
 megane      | USA     |     2029028
 model 3     | France  |     2159136
 model 3     | Germany |     2087820
 model 3     | USA     |     2040088
 model s     | France  |     9882084
 model s     | Germany |     9846032
 model s     | USA     |     9495266
 model x     | France  |     1090995
 model x     | Germany |     1076129
 model x     | USA     |     1034633
 model y     | France  |     1049741
 model y     | Germany |     1037977
 model y     | USA     |     1092768
 murano      | France  |     2177300
 murano      | Germany |     2259095
 murano      | USA     |     2061242
 mustang     | France  |     2086930
 mustang     | Germany |     2229627
 mustang     | USA     |     2118165
 mx-5        | France  |     1146690
 mx-5        | Germany |     1018986
 mx-5        | USA     |     1092301
 optima      | France  |     1111809
 optima      | Germany |     1142764
 optima      | USA     |     1100031
 outback     | France  |     7338692
 outback     | Germany |     7613492
 outback     | USA     |     7568885
 palisade    | France  |     1134788
 palisade    | Germany |     1081988
 palisade    | USA     |     1082472
 panamera    | France  |     3249964
 panamera    | Germany |     3221798
 panamera    | USA     |     3259543
 panda       | France  |     6175354
 panda       | Germany |     6421639
 panda       | USA     |     6583568
 passat      | France  |     3085364
 passat      | Germany |     3103176
 passat      | USA     |     3080113
 pilot       | France  |     1028834
 pilot       | Germany |     1050909
 pilot       | USA     |     1097477
 q5          | France  |     6522608
 q5          | Germany |     6334071
 q5          | USA     |     6303197
 q7          | France  |      991061
 q7          | Germany |     1123625
 q7          | USA     |     1214679
 rav4        | France  |     4232123
 rav4        | Germany |     4186472
 rav4        | USA     |     4254674
 rdx         | France  |     3279102
 rdx         | Germany |     3224902
 rdx         | USA     |     3284475
 regal       | France  |     5185650
 regal       | Germany |     5311099
 regal       | USA     |     5492209
 rlx         | France  |     5282405
 rlx         | Germany |     5439625
 rlx         | USA     |     5179582
 rogue       | France  |     3252826
 rogue       | Germany |     3240848
 rogue       | USA     |     3184340
 rx          | France  |      999600
 rx          | Germany |     1064892
 rx          | USA     |     1084120
 s60         | France  |     3323434
 s60         | Germany |     3186754
 s60         | USA     |     3164675
 s90         | France  |     4412164
 s90         | Germany |     4299589
 s90         | USA     |     4366186
 santa fe    | France  |     4322361
 santa fe    | Germany |     4345706
 santa fe    | USA     |     4377384
 scenic      | France  |     6648036
 scenic      | Germany |     6462022
 scenic      | USA     |     6570270
 s-class     | France  |     6438585
 s-class     | Germany |     6359882
 s-class     | USA     |     6563094
 sonata      | France  |     6347966
 sonata      | Germany |     6486193
 sonata      | USA     |     6323936
 soul        | France  |     4213124
 soul        | Germany |     4279610
 soul        | USA     |     4237802
 sportage    | France  |     2227152
 sportage    | Germany |     2163725
 sportage    | USA     |     2124957
 taycan      | France  |     6529049
 taycan      | Germany |     6541338
 taycan      | USA     |     6584795
 telluride   | France  |     1021744
 telluride   | Germany |      965957
 telluride   | USA     |      991790
 tiguan      | France  |     1008896
 tiguan      | Germany |     1026782
 tiguan      | USA     |     1169165
 tipo        | France  |     2312249
 tipo        | Germany |     2058596
 tipo        | USA     |     2141308
 tlx         | France  |     1085684
 tlx         | Germany |     1058389
 tlx         | USA     |     1165560
 traverse    | France  |     4292692
 traverse    | Germany |     4425552
 traverse    | USA     |     4339737
 tucson      | France  |     1188996
 tucson      | Germany |     1022481
 tucson      | USA     |     1162149
 x3          | France  |     3112891
 x3          | Germany |     3176786
 x3          | USA     |     3312323
 x5          | France  |     2027650
 x5          | Germany |     2101315
 x5          | USA     |     2101550
 xc40        | France  |     1169354
 xc40        | Germany |     1029339
 xc40        | USA     |     1106320
 xc60        | France  |     2312091
 xc60        | Germany |     2224037
 xc60        | USA     |     2179455
 xc90        | France  |     3238279
 xc90        | Germany |     3130926
 xc90        | USA     |     3085302
 xe          | France  |     4094681
 xe          | Germany |     4345498
 xe          | USA     |     4207222
 xf          | France  |     2300644
 xf          | Germany |     2131448
 xf          | USA     |     2043056

*/
-- b. Country with the most of each model and how many they have
SELECT sub."Car Model", sub."Country", sub.max_sales
FROM (
    SELECT 
        "Car Model",
        "Country",
        SUM("Sales Volume") AS max_sales,
        RANK() OVER (PARTITION BY "Car Model" ORDER BY SUM("Sales Volume") DESC) AS rk
    FROM car_reviews
    GROUP BY "Car Model", "Country"
) sub
WHERE sub.rk = 1;

/*
 Car Model  | Country | max_sales 
-------------+---------+-----------
 124 spider  | USA     |   1105590
 208         | France  |   2296774
 308         | USA     |   2179891
 500         | Germany |   3227904
 5008        | France  |   6670060
 500x        | USA     |   1103586
 508         | USA     |   2140226
 5 series    | Germany |   3361289
 7 series    | France  |   5647610
 911         | USA     |   2201418
 a4          | Germany |   4556028
 a6          | Germany |   1119014
 accord      | France  |   3238405
 altima      | France  |   4553658
 astra       | USA     |   2213964
 atlas       | France  |   1045423
 bolt        | France  |   1097194
 camry       | Germany |   2198249
 captur      | Germany |   3337181
 cayenne     | France  |   2224057
 c-class     | Germany |   2196147
 civic       | Germany |   4303380
 clio        | USA     |   1121429
 corolla     | France  |   3480922
 corsa       | Germany |   4427332
 crossland x | France  |   5369396
 cruze       | France  |   3275906
 cr-v        | USA     |   1087240
 cx-5        | France  |   3406545
 cx-9        | Germany |   2238819
 elantra     | France  |   1159989
 enclave     | USA     |   1116685
 envision    | France  |   7720788
 equinox     | France  |   3228002
 es          | France  |   5350305
 escape      | USA     |   2158943
 e-tron      | USA     |   1089811
 explorer    | Germany |   5479518
 f-150       | USA     |   3385942
 fit         | France  |   4379342
 forester    | France  |   3235608
 forte       | France  |   4383549
 f-pace      | Germany |   6455641
 fusion      | USA     |   1142379
 glc         | USA     |   1102591
 gle         | USA     |   3317676
 golf        | USA     |   7734295
 grandland x | France  |   1113107
 gx          | France  |   1088600
 highlander  | France  |   4282283
 impreza     | Germany |   1086493
 insignia    | France  |   1038613
 i-pace      | France  |   1104865
 jetta       | France  |   1134912
 kadjar      | France  |   1163513
 leaf        | USA     |   2222985
 legacy      | Germany |   2232956
 ls          | USA     |   5780281
 malibu      | Germany |   2241677
 maxima      | Germany |   2342433
 mazda3      | USA     |   4349433
 mazda6      | France  |   2243593
 mdx         | USA     |   4464511
 megane      | France  |   2159512
 model 3     | France  |   2159136
 model s     | France  |   9882084
 model x     | France  |   1090995
 model y     | USA     |   1092768
 murano      | Germany |   2259095
 mustang     | Germany |   2229627
 mx-5        | France  |   1146690
 optima      | Germany |   1142764
 outback     | Germany |   7613492
 palisade    | France  |   1134788
 panamera    | USA     |   3259543
 panda       | USA     |   6583568
 passat      | Germany |   3103176
 pilot       | USA     |   1097477
 q5          | France  |   6522608
 q7          | USA     |   1214679
 rav4        | USA     |   4254674
 rdx         | USA     |   3284475
 regal       | USA     |   5492209
 rlx         | Germany |   5439625
 rogue       | France  |   3252826
 rx          | USA     |   1084120
 s60         | France  |   3323434
 s90         | France  |   4412164
 santa fe    | USA     |   4377384
 scenic      | France  |   6648036
 s-class     | USA     |   6563094
 sonata      | Germany |   6486193
 soul        | Germany |   4279610
 sportage    | France  |   2227152
 taycan      | USA     |   6584795
 telluride   | France  |   1021744
 tiguan      | USA     |   1169165
 tipo        | France  |   2312249
 tlx         | USA     |   1165560
 traverse    | Germany |   4425552
 tucson      | France  |   1188996
 x3          | USA     |   3312323
 x5          | USA     |   2101550
 xc40        | France  |   1169354
 xc60        | France  |   2312091
 xc90        | France  |   3238279
 xe          | Germany |   4345498
 xf          | France  |   2300644
(108 rows)
*/

-- c. Models sold in USA but not in France
SELECT DISTINCT "Car Model"
FROM car_reviews
WHERE "Country" = 'USA'
  AND "Car Model" NOT IN (
    SELECT DISTINCT "Car Model"
    FROM car_reviews
    WHERE "Country" = 'France'
  );
/*
 Car Model 
-----------
(0 rows)
*/

-- d. Average car price by country and engine type
SELECT 
    "Country",
    "Engine Type",
    AVG("Price") AS avg_price
FROM car_reviews
GROUP BY "Country", "Engine Type"
ORDER BY "Country", "Engine Type";
 /*
  Country | Engine Type |     avg_price      
---------+-------------+--------------------
 France  | Electric    | 48159.057385229541
 France  | Thermal     | 45285.995760963349
 Germany | Electric    | 48181.378708551483
 Germany | Thermal     | 45291.830195754894
 USA     | Electric    | 48186.420344053852
 USA     | Thermal     | 45292.207680192005
(6 rows)
*/

-- e. Average review scores for electric vs thermal cars
SELECT 
    "Engine Type",
    AVG("Review Score") AS avg_review_score
FROM car_reviews
GROUP BY "Engine Type"
ORDER BY "Engine Type";

/*
 Engine Type |  avg_review_score  
-------------+--------------------
 Electric    | 2.9992186201163915
 Thermal     | 2.9963594994311897
(2 rows)
*/