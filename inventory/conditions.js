5
zone_gpp != 1 and zone_gbz != 1

6
(((zone_gpp = 1 or zone_gbz = 1) and (land_category = 1 or land_category = 4 or land_category =5 or land_category = 6 or land_category = 7 or land_category = 11)) or (exploitation_category = 1) or (exploitation_category = 2 and land_category != 8 and land_category != 8) or (exploitation_category = 3 and (land_category = 1 or land_category = 4 or land_category =5 or land_category = 6 or land_category = 7 or land_category = 11)))

7
(((zone_gpp = 1 or zone_gbz = 1) and (land_category = 1 or land_category = 4)) or (exploitation_category =1 and (land_category = 1)) or (exploitation_category =2 and (land_category = 1  or land_category = 4)) or (exploitation_category = 3 and (land_category = 1  or land_category = 4)))

8
(((zone_gpp = 1 or zone_gbz = 1) and (land_category =1 and evolution_stage != 6)) or (exploitation_category =1 and (land_category =1 and evolution_stage != 6)) or (exploitation_category =2 and (land_category =1 and evolution_stage != 6)) or (exploitation_category = 3 and (land_category =1 and evolution_stage != 6)))

9
(((zone_gpp = 1 or zone_gbz = 1) and (land_category =1 and evolution_stage != 6)) or (exploitation_category =1 and (land_category =1)) or (exploitation_category =2 and (land_category =1)) or (exploitation_category = 3 and (land_category =1)))

10
(((zone_gpp = 1 or zone_gbz = 1) and (land_category = 1 or land_category = 4)) or (exploitation_category =1) or (exploitation_category =2 and (land_category = 1  or land_category = 2 or land_category = 4)) or (exploitation_category = 3 and (land_category = 1 or land_category = 4)))

11
(((zone_gpp = 1 or zone_gbz = 1) and (land_category = 1)) or (exploitation_category =1 and (land_category = 1)) or (exploitation_category =2 and (land_category = 1)) or (exploitation_category = 3 and (land_category = 1)))

12
(((zone_gpp = 1 or zone_gbz = 1) and (land_category = 1)) or (exploitation_category =1 and (land_category = 1)) or (exploitation_category =2 and (land_category = 1)) or (exploitation_category = 3 and (land_category = 1)))

13
exploitation_category = 1 and land_category = 1 and evolution_stage != 6

14
(((zone_gpp = 1 or zone_gbz =1) and (land_category = 1 or land_category = 4)) or (exploitation_category =1 and (land_category = 1 or land_category = 2)) or (exploitation_category =2 and (land_category = 1 or land_category = 2 or land_category = 3 or land_category = 4 or land_category = 12)) or (exploitation_category = 3 and (land_category = 1 or land_category = 4)))

15
(exploitation_category = 1 or exploitation_category = 2) and (land_category = 1 and evolution_stage != 6)

16
((exploitation_category = 1) or (exploitation_category =2 and (land_category = 1 or land_category = 2 or land_category = 4 or land_category = 5 or land_category = 6 or land_category = 7 or land_category = 10 or land_category = 11)))

17
((exploitation_category = 1 and ((land_category = 1 and evolution_stage != 6) or land_category = 2)) or (exploitation_category =2 and ((land_category = 1 and evolution_stage != 6) or land_category = 2 or land_category = 4)))

18
((exploitation_category = 1) or (exploitation_category =2 and (land_category = 1 or land_category = 2 or land_category = 4 or land_category = 10 or land_category = 11)))

19
((exploitation_category = 1) or (exploitation_category =2 and (land_category = 1 or land_category = 2 or land_category = 4 or land_category = 5 or land_category = 6 or land_category = 7 or land_category = 10 or land_category = 11 or land_category = 12)))

20
((exploitation_category = 1) or (exploitation_category =2 and (land_category = 1 or land_category = 2 or land_category = 4 or land_category = 5 or land_category = 6 or land_category = 7 or land_category = 10 or land_category = 11 or land_category = 12)))

21
((exploitation_category = 1 and land_category = 1 and evolution_stage != 6) or (exploitation_category =2 and ((land_category = 1 and evolution_stage !=6) or land_category = 4)))

22
always

23
land_category != 3

24
((exploitation_category = 1) or (exploitation_category =2 and (land_category != 3 or land_category != 8 or land_category != 9)))

25
(((parent()/zone_gpp = 1 or parent()/zone_gbz =1)) or (parent()/exploitation_category = 1) or (parent()/exploitation_category = 2 and (parent()/land_category != 3 and parent()/land_category !=8 and parent()/land_category != 9)))


26
((parent()/exploitation_category = 1) or (parent()/exploitation_category = 2 and (parent()/land_category != 3 and parent()/land_category !=8 and parent()/land_category != 9)))

27
((parent()/exploitation_category = 1) or (parent()/exploitation_category = 2 and (parent()/land_category != 3 and parent()/land_category !=8 and parent()/land_category != 9)))

28
((parent()/exploitation_category = 1 and parent()/evolution_stage !=6) or (parent()/exploitation_category = 2 and (parent()/land_category = 12)))

29
((parent()/exploitation_category = 1) or (parent()/exploitation_category = 2 and (parent()/land_category != 3)))

30
((parent()/exploitation_category = 1) or (parent()/exploitation_category = 2 and (parent()/land_category != 3)))

31
((parent()/exploitation_category = 1 and parent()/land_category != 2) or (parent()/exploitation_category = 2 and parent()/land_category != 3))

32
((parent()/exploitation_category = 1 and parent()/land_category != 2) or (parent()/exploitation_category = 2 and parent()/land_category != 3))

33
((parent()/exploitation_category = 1) or (parent()/exploitation_category = 2 and parent()/land_category != 3))

34
land_category != 3

35
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

36
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

37
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

38
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

39
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

40
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

41
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

42
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

43
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

44
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

45
land_category != 3

46
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

47
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12

48
land_category != 3 and land_category != 8 and land_category != 9 and land_category != 12












(((zone_gpp = 1 or zone_gbz =1) and ()) or (exploitation_category = 1 and ()) or (exploitation_category = 2 and ()) or (exploitation_category = 3 and ()))

((exploitation_category = 1) or (exploitation_category =2 and (land_category = 1 or land_category = 2 or land_category = 4 or land_category = 10 or land_category = 11)))

1-7, 9, 10-12, 14,16, 18-20, 22-27, 29, 30 (31, 32), 33-48.







inventory

1.1 -- 1.6, 1.8, 1.21, 2.1 -- 2.4 (availability == 2)


actions

