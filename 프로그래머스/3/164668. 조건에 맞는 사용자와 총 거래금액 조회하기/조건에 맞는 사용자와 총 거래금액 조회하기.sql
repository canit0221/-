-- 코드를 입력하세요
SELECT
    USER_ID,
    NICKNAME,
    SUM(PRICE) AS TOTAL_SALES
FROM 
    USED_GOODS_BOARD B
JOIN
    USED_GOODS_USER U
ON 
    B.WRITER_ID = U.USER_ID
WHERE
    STATUS = 'DONE'
GROUP BY 1,2
HAVING TOTAL_SALES >=700000
ORDER BY 3