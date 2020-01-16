use ecnu;
#该部分的脚本主要是进行对接的脚本，目的很简单，就是为了处获取对接后的结果
SELECT 
    gene AS `靶点`,
    pdbid AS `PDB ID`,
    molecule AS `成分`,
    scores AS `docking scores`
FROM
    (SELECT 
        *
    FROM
        (SELECT 
        c.molecule,
            c.pubchemcid,
            c.drug,
            b.uniprotid,
            b.protein,
            b.gene,
            b.pdbid,
            a.scores
    FROM
        (SELECT 
        *
    FROM
        docked
    WHERE
        scores IS NOT NULL
    ORDER BY SCORES) a
    LEFT JOIN target b ON a.pdbid = b.pdbid
    LEFT JOIN (SELECT 
        pubchemcid, molecule, GROUP_CONCAT(DISTINCT drug) AS drug
    FROM
        druginfos
    GROUP BY pubchemcid) c ON a.pubchemcid = c.pubchemcid
    WHERE
        c.molecule IS NOT NULL
    ORDER BY a.scores) a
    WHERE
        scores > 7
    ORDER BY scores DESC) a