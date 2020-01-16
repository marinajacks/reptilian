use ecnu;
#这部分的脚本主要是成分对应的信息，数据的来源主要是对应的druginfos这张表的信息与数据。
select 
*
from (select distinct 
pubchemcid ,drug,molecule from 
(select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
from
(select * from docked  where scores is not null ORDER BY SCORES )a
left join target b on a.pdbid =b.pdbid
left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
on a.pubchemcid=c.pubchemcid
where c.molecule is not null order by a.scores desc) result) a 
where   find_in_set('龙血竭', drug)
;


select  distinct a.pubchemcid
 from 
(
select * from docked  where scores is not null ORDER BY SCORES  
)a
left join target b on a.pdbid =b.pdbid
left join druginfos c on a.pubchemcid =c.pubchemcid

where c.pubchemcid is null
;
/*
select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid
select * from druginfos;

select distinct pubchemcid from docked

*/

#这个命令主要是为了获取到
select molecule,pubchemcid,group_concat(distinct drug) as drug from druginfos group by pubchemcid;