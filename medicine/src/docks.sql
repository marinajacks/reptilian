use ecnu;
select * from compounds;

SELECT 
    molecule,
    OB,
    DL,
    pubchemcid,
    GROUP_CONCAT(drug) AS drug
FROM
    compounds
GROUP BY molecule;

SELECT 
    *
FROM
    target;

SELECT a.* ,b.*,c.* from 
(SELECT 
    PDBID, PUBCHEMCID, SCORES
FROM
    docked
WHERE
    scores IS NOT NULL)a
    left join target b on a.pdbid=b.pdbid
    left join
    (SELECT 
    molecule,
    OB,
    DL,
    pubchemcid,
    GROUP_CONCAT(drug) AS drug
FROM
    compounds
GROUP BY molecule) c on a.pubchemcid=c.pubchemcid

;


SELECT a.* ,b.*#,c.* 
from 
(SELECT 
    PDBID, PUBCHEMCID, SCORES
FROM
    docked
WHERE
    scores IS NOT NULL)a
    left join target b on a.pdbid=b.pdbid
    left join
    
(select pubchemcid,molecule,group_concat(drug) as drug from druginfos1 group by  pubchemcid) c on a.pubchemcid=c.pubchemcid
where c.pubchemcid is null
/*
 (select a.OB,a.dl,b.pubchemcid,b.molecule,b.names from
(SELECT 
    molecule,
    OB,
    DL,
    pubchemcid,
    GROUP_CONCAT(drug) AS drug
FROM
    compounds
GROUP BY molecule)  c on a.pubchemcid=c.pubchemcid
/*
   right join 
(select pubchemcid,molecule,group_concat(drug) as names from names group by pubchemcid)  b
on a.molecule=b.molecule) c on a.pubchemcid=c.pubchemcid*/
;
select distinct id1 from(
select  a.pubchemcid as id1,c.pubchemcid id2 from 
(SELECT 
    PDBID, PUBCHEMCID, SCORES
FROM
    docked
WHERE
    scores IS NOT NULL)a
    left join
    (select pubchemcid,molecule,group_concat(drug) as drug from druginfos1 group by  pubchemcid) c on a.pubchemcid=c.pubchemcid
where c.pubchemcid is null
    )d
    
    
    
    use ecnu;

SELECT a.* ,b.*,c.* 
from 
(SELECT 
    PDBID, PUBCHEMCID, SCORES
FROM
    docked
WHERE
    scores IS NOT NULL)a
    left join target b on a.pdbid=b.pdbid
    left join
    (SELECT 
    molecule,
    OB,
    DL,
    pubchemcid,
    GROUP_CONCAT(drug) AS drug
FROM
    compounds
GROUP BY molecule) c on a.pubchemcid=c.pubchemcid
#where molecule is null;
;

select a.OB,a.dl,b.pubchemcid,b.molecule,b.names from
(SELECT 
    molecule,
    OB,
    DL,
    pubchemcid,
    GROUP_CONCAT(drug) AS drug
FROM
    compounds
GROUP BY molecule)  a
   right join 
(select pubchemcid,molecule,group_concat(drug) as names from names group by pubchemcid)  b
on a.molecule=b.molecule;



select * from drugs1;

SELECT 
    *
FROM
    (SELECT 
        pubchemcid, GROUP_CONCAT(molecule) AS molecules, drug
    FROM
        drugs1
    GROUP BY pubchemcid) a
WHERE
    pubchemcid IN (101130267)
    
    
    
    
    use ecnu;
select * from names;


create table drugs as 
(
select
	replace(replace(replace(molecule,'\"',''),',',''),'\'','') as molecule,
	replace(replace(drug,'\'',''),',','') as drug,
	replace(replace(pubchemcid,'\'',''),',','') as pubchemcid
from names);

select pubchemcid,molecule,group_concat(drug) as drug from druginfos group by  pubchemcid
;



select a.*,b.* from compounds a
left join 
(select pubchemcid,molecule from  moles group by  pubchemcid)b on a.molecule=b.molecule
where a.pubchemcid in (445638,440832,131900)