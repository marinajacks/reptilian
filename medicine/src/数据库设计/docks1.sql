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


select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid