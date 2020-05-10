-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: Localidad
-- --------------------------------------
create table Localidad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idDepartamento INT NOT NULL,
    codigo varchar(32) NOT NULL,
    nombre varchar(256) not null,
    CONSTRAINT fk_localidad_depto foreign key (idDepartamento) references Departamento(id)
);

create unique index uidx_Localidad
on Localidad(idDepartamento, codigo, nombre);
