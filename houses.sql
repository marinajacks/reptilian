#select length('明发滨江新城三期') as n,length('中楼层(共5层)2013年建板塔结合') as n2

use ecnu;
/*
create table house(
id	int(11) primary key auto_increment,
city	varchar(100),
village	varchar(100),
rooms	varchar(100),
area	varchar(100),
orientation	varchar(100),
lift	varchar(100),
floor	varchar(200),
address	varchar(200),
totalprice	varchar(100),
unitprice	varchar(100)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='房价信息表';
*/

#select a.* ,replace(unitprice,'元/平米','') as unit from house a order by unit desc;

#select *  from house where city ='sh' order by cast( trim(replace(totalprice,'元/平米','')) as SIGNED) desc ;


#下面的程序主要是为了获取到每个城市的房价单价信息
SELECT 
    city,
    CONCAT(areas, '平米') AS areas,
    CONCAT(total, '万') AS total,
    CONCAT(ROUND(10000 * total / areas),
            '元/平米') AS price
FROM
    (SELECT 
        city,
            SUM(CAST(TRIM(REPLACE(area, '平米', '')) AS SIGNED)) AS areas,
			SUM(CAST(TRIM(REPLACE(area, '平米', '')) AS SIGNED)) AS areas1,
            SUM(CAST(TRIM(REPLACE(totalprice, '元/平米', ''))
                AS SIGNED)) AS total
    FROM
        house
    GROUP BY city) a
ORDER BY areas1 DESC