-- 코드를 입력하세요
SELECT a.NAME, a.DATETIME
FROM ANIMAL_INS AS a
LEFT JOIN ANIMAL_OUTS AS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE b.ANIMAL_ID IS NULL
ORDER BY a.DATETIME ASC
LIMIT 3;