drop table if exists MailTel;

create table MailTel (
    id int not null PRIMARY KEY,
    codigo varchar(32), 
    telefono varchar(128), 
    mail varchar(255)
);

create unique index uidx_MailTel on MailTel(Codigo);

INSERT INTO Mailtel( id, Codigo, telefono, mail)
select e.id, db.CUE_Anexo , lower(trim(db.Mail)),
'('||ifnull(db.Codigo_de_area,'000')||')'||trim(ifnulL(db.telefono,'XXXYYYY'))
from DatosBase db
inner join Escuela e
 on e.Codigo = db.CUE_Anexo;

 select count(*) from MailTel;






