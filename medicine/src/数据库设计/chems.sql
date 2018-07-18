/*这里设计的是一张化学药品的表,主要是为了存储化学药品的图片信息化学药品的图片数据主要是
存储成二进制的BLOB或者是MediumBlob的格式,前者存储的最大限制是64K,后者最大的是16M.*/
create table chems(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	source	varchar(20) COMMENT '数据来源',
	drugs	varchar(20) COMMENT '药品名称',
	chemical 	varchar(256) COMMENT '化学成分',
	photo	MediumBlob COMMENT '照片'
	)ENGINE=InnoDB
	DEFAULT CHARSET= 'utf8'
	COLLATE='utf8_general_ci';


#这部分主要是java中的指令处理方式的脚本信息.
insert into chems(source,drugs,chemical,photo) values (?,?,?,?,?);
	


插入数据的文件地址:
D:/MarinaJacks/project/reptilian/medicine/中药数据/TCMSP/三七/imags
D:/MarinaJacks/project/reptilian/medicine/中药数据/TCMSP/薏苡仁/imags
D:/MarinaJacks/project/reptilian/medicine/中药数据/TCMSP/浙贝母/imags

D:/MarinaJacks/project/reptilian/medicine/中药数据/TCMID/SAN QI/imags
D:/MarinaJacks/project/reptilian/medicine/中药数据/TCMID/YI YI REN/imags
D:/MarinaJacks/project/reptilian/medicine/中药数据/TCMID/ZHE BEI MU/imags

