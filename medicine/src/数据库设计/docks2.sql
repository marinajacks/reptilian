use ecnu;
select gene,pdbid,count(molecule) as nums 
from 
(

select *from (
select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
from
(select * from docked  where scores is not null ORDER BY SCORES )a
left join target b on a.pdbid =b.pdbid
left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
on a.pubchemcid=c.pubchemcid
where c.molecule is not null order by a.scores

 ) a where scores>7  order by scores desc

)

 a group by gene  order by nums desc  limit 6;
 
 /*
 
 
 select 
*
from (


select distinct 
pubchemcid ,drug,molecule from 
(select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
from
(select * from docked  where scores is not null ORDER BY SCORES )a
left join target b on a.pdbid =b.pdbid
left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
on a.pubchemcid=c.pubchemcid
where c.molecule is not null order by a.scores desc


) result


) a where '龙血竭' in (drug)
*/


#下面的脚本主要是根据对接打分的大小进行排序,然后按照打分数据获取前一部分的数据
select gene as `靶点`,pdbid as `PDB ID`, molecule as `成分`, scores as `docking scores`from (
select *from (
select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
from
(select * from docked  where scores is not null ORDER BY SCORES )a
left join target b on a.pdbid =b.pdbid
left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
on a.pubchemcid=c.pubchemcid
where c.molecule is not null order by a.scores

 ) a where scores>7  order by scores desc) a