SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, l.leshoz_ru AS level2_label_ru,
f.gid AS level3_code, f.forestry_ru AS level3_label_ru
FROM forest.forestry f LEFT JOIN forest.leshoz l ON l.leshoz_id = f.leshoz_id
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, l.leshoz_ru AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM forest.leshoz l LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
0 AS level2_code, '' AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM topo.oblast o
ORDER BY level1_code, level2_label_ru, level3_label_ru


SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, l.leshoz_ru AS level2_label_ru,
f.gid AS level3_code, f.forestry_ru AS level3_label_ru
FROM forest.forestry f LEFT JOIN forest.leshoz l ON l.leshoz_id = f.leshoz_id AND l.leshoztype_id = 1
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, l.leshoz_ru AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM forest.leshoz l LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id AND l.leshoztype_id = 1
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
0 AS level2_code, '' AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM topo.oblast o
ORDER BY level1_code, level2_label_ru, level3_label_ru



SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, l.leshoz_ru AS level2_label_ru,
f.gid AS level3_code, ft.forestrytype_ru AS level3_label_ru
FROM forest.forestrytype ft
LEFT JOIN forest.forestry f ON ft.forestrytype_id = f.forestrytype_id
LEFT JOIN forest.leshoz l ON l.leshoz_id = f.leshoz_id 
AND (l.leshoztype_id = 3 OR l.leshoztype_id = 4 AND l.leshoztype_id = 5)
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, l.leshoz_ru AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM forest.leshoz l LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id 
AND (l.leshoztype_id = 3 OR l.leshoztype_id = 4 AND l.leshoztype_id = 5)
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
0 AS level2_code, '' AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM topo.oblast o
ORDER BY level1_code, level2_label_ru, level3_label_ru



SELECT ag.actiongroup_id AS level1_code, ag.actiongroup_ru AS level1_label_ru,
at.actiontype_id AS level2_code, at.actiontype_ru AS level2_label_ru
FROM forest.actiontype at 
LEFT JOIN forest.actiongroup ag ON ag.actiongroup_id = at.actiongroup_id 
WHERE ag.actiongroup_id IS NOT null
UNION
SELECT actiongroup_id AS level1_code, actiongroup_ru AS level1_label_ru,
0 AS level2_code, '' AS level2_label_ru
FROM forest.actiongroup
WHERE (SELECT count(*) FROM forest.actiontype WHERE actiongroup_id = actiongroup.actiongroup_id) > 0
ORDER BY level1_code, level2_label_ru



SELECT foresttype_id AS foresttype_code, CONCAT(foresttype_code, ' ', foresttype_ru) AS foresttype_label
FROM forest.foresttype
ORDER BY foresttype_id ASC



SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
r.gid AS level2_code, r.raion_ru AS level2_label_ru,
ai.gid AS level3_code, ai.aimak_ru AS level3_label_ru
FROM topo.aimak ai LEFT JOIN topo.raion r ON r.gid = ai.raion_id
LEFT JOIN topo.oblast o ON o.oblast_id = r.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
r.gid AS level2_code, r.raion_ru AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM topo.raion r LEFT JOIN topo.oblast o ON o.oblast_id = r.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
0 AS level2_code, '' AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM topo.oblast o
ORDER BY level1_code, level2_label_ru, level3_label_ru



SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, CONCAT(lt.leshoztype_ru, ' ', l.leshoz_ru) AS level2_label_ru
FROM forest.leshoz l LEFT JOIN forest.leshoztype lt ON lt.leshoztype_id = l.leshoztype_id 
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, CONCAT(lt.leshoztype_ru, ' ', l.leshoz_ru) AS level2_label_ru
FROM forest.leshoz l LEFT JOIN forest.leshoztype lt ON lt.leshoztype_id = l.leshoztype_id
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
0 AS level2_code, '' AS level2_label_ru FROM topo.oblast o
ORDER BY level1_code, level2_label_ru



SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, CONCAT(lt.leshoztype_ru, ' ', l.leshoz_ru) AS level2_label_ru,
f.gid AS level3_code, f.forestry_ru AS level3_label_ru
FROM forest.forestry f LEFT JOIN forest.leshoz l ON l.leshoz_id = f.leshoz_id 
LEFT JOIN forest.leshoztype lt ON lt.leshoztype_id = l.leshoztype_id 
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, CONCAT(lt.leshoztype_ru, ' ', l.leshoz_ru) AS level2_label_ru,
f.gid AS level3_code, f.forestry_ru AS level3_label_ru
FROM forest.forestry f LEFT JOIN forest.leshoz l ON l.leshoz_id = f.leshoz_id 
LEFT JOIN forest.leshoztype lt ON lt.leshoztype_id = l.leshoztype_id
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
0 AS level2_code, '' AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM topo.oblast o
ORDER BY level1_code, level2_label_ru


SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, CONCAT(lt.leshoztype_ru, ' ', l.leshoz_ru) AS level2_label_ru,
f.gid AS level3_code, CONCAT(f.forestry_ru, ' ', ft.forestrytype_ru) AS level3_label_ru
FROM forest.forestrytype ft
LEFT JOIN forest.forestry f ON ft.forestrytype_id = f.forestrytype_id
LEFT JOIN forest.leshoz l ON l.leshoz_id = f.leshoz_id 
LEFT JOIN forest.leshoztype lt ON lt.leshoztype_id = l.leshoztype_id 
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
l.leshoz_id AS level2_code, CONCAT(lt.leshoztype_ru, ' ', l.leshoz_ru) AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM forest.forestrytype ft
LEFT JOIN forest.forestry f ON ft.forestrytype_id = f.forestrytype_id
LEFT JOIN forest.leshoz l ON l.leshoz_id = f.leshoz_id 
LEFT JOIN forest.leshoztype lt ON lt.leshoztype_id = l.leshoztype_id
LEFT JOIN topo.oblast o ON o.oblast_id = l.oblast_id
UNION
SELECT o.oblast_id AS level1_code, o.oblast_ru AS level1_label_ru,
0 AS level2_code, '' AS level2_label_ru,
0 AS level3_code, '' AS level3_label_ru
FROM topo.oblast o
ORDER BY level1_code, level2_label_ru, level3_label_ru