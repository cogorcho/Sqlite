-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: TipoEducacionNivel 
-- --------------------------------------
drop table if Exists TipoEducacionNivel;

create table TipoEducacionNivel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idTipoEducacion INT NOT NULL,
    idNivel INT NOT NULL,
    active char(1) not null check (active in ('Y','N')) default 'N',
    CONSTRAINT fk_NTE_TED foreign key (idTipoEducacion) references TipoEducacion(id),
    CONSTRAINT fk_NTE_NIV foreign key (idNivel) references Nivel(id)
);

create unique index uidx_tednivel on TipoEducacionNivel(idTipoEducacion,idNivel);

insert into TipoEducacionNivel (idTipoEducacion, idNivel)
select ted.id, niv.id
from TipoEducacion ted, Nivel niv 
order by 1,2;
