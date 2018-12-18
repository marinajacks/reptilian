# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:24:45 2018
这个程序专门用来
@author: hello
"""
import pandas as pd
import pymysql
    
    sql='''
        select  a.*,b.*,c.*
         from 
        (
        select * from docked  where scores is not null ORDER BY SCORES  
        )a
        left join target b on a.pdbid =b.pdbid
        
        
        left join 
        (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid
        )
        c on a.pubchemcid=c.pubchemcid
        where c.pubchemcid is not null
        '''
    
    sql='''
    
        select *from (select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
        from
        (select * from docked  where scores is not null ORDER BY SCORES )a
        left join target b on a.pdbid =b.pdbid
        left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
        on a.pubchemcid=c.pubchemcid
        where c.molecule is not null order by a.scores ) a where scores between 4.25 and 5
        
        '''
    
    sql1='''
    
        select *from (select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
        from
        (select * from docked  where scores is not null ORDER BY SCORES )a
        left join target b on a.pdbid =b.pdbid
        left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
        on a.pubchemcid=c.pubchemcid
        where c.molecule is not null order by a.scores ) a where scores between 5 and 7
        
        '''
    
    sql2='''
    
        select *from (select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
        from
        (select * from docked  where scores is not null ORDER BY SCORES )a
        left join target b on a.pdbid =b.pdbid
        left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
        on a.pubchemcid=c.pubchemcid
        where c.molecule is not null order by a.scores ) a where scores>7
        
        '''
    
    sql3='''
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
        
        '''
    
    sql4='''
        select * from tcmid'''
    
    
    
    sql5='''
    select * from (select distinct 
    pubchemcid ,drug,molecule from 
    (select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
    from
    (select * from docked  where scores is not null ORDER BY SCORES )a
    left join target b on a.pdbid =b.pdbid
    left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
    on a.pubchemcid=c.pubchemcid
    where c.molecule is not null order by a.scores desc) result) a 
    where   find_in_set('龙血竭', drug);
    '''
    
    sql6='''
    select * from (select distinct 
    pubchemcid ,drug,molecule from 
    (select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
    from
    (select * from docked  where scores is not null ORDER BY SCORES )a
    left join target b on a.pdbid =b.pdbid
    left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
    on a.pubchemcid=c.pubchemcid
    where c.molecule is not null order by a.scores desc) result) a 
    where   find_in_set('浙贝母', drug);
    '''
    
    sql7='''
    select * from (select distinct 
    pubchemcid ,drug,molecule from 
    (select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
    from
    (select * from docked  where scores is not null ORDER BY SCORES )a
    left join target b on a.pdbid =b.pdbid
    left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
    on a.pubchemcid=c.pubchemcid
    where c.molecule is not null order by a.scores desc) result) a 
    where   find_in_set('三七', drug);
    '''
    
    sql8='''
    select * from (select distinct 
    pubchemcid ,drug,molecule from 
    (select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
    from
    (select * from docked  where scores is not null ORDER BY SCORES )a
    left join target b on a.pdbid =b.pdbid
    left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
    on a.pubchemcid=c.pubchemcid
    where c.molecule is not null order by a.scores desc) result) a 
    where   find_in_set('薏苡仁', drug);
    '''

def test(sql,path):
    conn = pymysql.connect(host='127.0.0.1', 
               user='root',password='', 
               db='ecnu',charset='utf8', 
               use_unicode=True)
    df = pd.read_sql(sql5, con=conn)
    print(df.head())
    
    path='D:\MarinaJacks\project\\reptilian\medicine\对接数据\中药成分数据.xlsx'
    
    df1 = pd.read_sql(sql6, con=conn)
    df2 = pd.read_sql(sql7, con=conn)
    df3 = pd.read_sql(sql8, con=conn)

    writer = pd.ExcelWriter(path)
    df.to_excel(excel_writer=writer,sheet_name='龙血竭')
    df1.to_excel(excel_writer=writer,sheet_name='浙贝母')
    df2.to_excel(excel_writer=writer,sheet_name='三七')
    df3.to_excel(excel_writer=writer,sheet_name='薏苡仁')
    writer.save()
    writer.close()
    
    
    

if __name__=="__main__":
    sql0='''
    select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
    from
    (select * from docked  where scores is not null ORDER BY SCORES )a
    left join target b on a.pdbid =b.pdbid
    left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
    on a.pubchemcid=c.pubchemcid
    where c.molecule is not null order by a.scores desc;
        '''
    path="D:\MarinaJacks\project\\reptilian\medicine\对接数据\data6.xlsx"
    sql1='''select  * from (select distinct 
    pubchemcid ,drug,molecule from 
    (select  c.molecule,c.pubchemcid,c.drug,b.uniprotid,b.protein,b.gene,b.pdbid,a.scores #a.*,b.*,c.*
    from
    (select * from docked  where scores is not null ORDER BY SCORES )a
    left join target b on a.pdbid =b.pdbid
    left join (select pubchemcid,molecule,group_concat(distinct drug) as drug from druginfos group by pubchemcid)c 
    on a.pubchemcid=c.pubchemcid
    where c.molecule is not null order by a.scores desc) result) a where '龙血竭' in (drug)
    '''
    test(sql1,path)
    
    df=pd.read_excel('D:\MarinaJacks\project\\reptilian\medicine\对接数据\打分结果.xlsx',sheet_name='可视化分析')