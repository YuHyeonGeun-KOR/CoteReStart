-- 코드를 입력하세요
SELECT count(*) as USERS
FROM USER_INFO 
WHERE AGE >=20 AND AGE <=29 and year(JOINED) = 2021