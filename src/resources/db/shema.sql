CREATE TABLE USUARIO (
    id_usr INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usr VARCHAR(225),
    email VARCHAR(225),
    password VARCHAR(225),
    ape_usr VARCHAR(225),
    numero_usr VARCHAR(225)
);

CREATE TABLE CURTIEMBRE (
    id_cr INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cr VARCHAR(100),
    numero_cr VARCHAR(20)
);

CREATE TABLE COLOR (
    id_cl INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cl VARCHAR(50),
    codigo_hx VARCHAR(10)
);

CREATE TABLE CATEMATERIAL (
    id_ct INT AUTO_INCREMENT PRIMARY KEY,
    nombre_ct VARCHAR(100),
    medida VARCHAR(50),
);

CREATE TABLE TIPO (
    id_tp INT AUTO_INCREMENT PRIMARY KEY,
    nombre_tp VARCHAR(100),
    precio_tp DECIMAL(10, 2),
    id_categoria INT,
    id_color INT,
    id_curtiembre INT,
    FOREIGN KEY (id_color) REFERENCES COLOR(id_cl),
    FOREIGN KEY (id_curtiembre) REFERENCES CURTIEMBRE(id_cr)
    FOREIGN KEY (id_categoria) REFERENCES CATEMATERIAL(id_ct)
);

CREATE TABLE MATERIAL (
    id_mt INT AUTO_INCREMENT PRIMARY KEY,
    medida_mt VARCHAR(50),
    id_tipo INT,
    FOREIGN KEY (id_tipo) REFERENCES TIPO(id_tp)
);

CREATE TABLE INVENTARIO (
    id_inv INT AUTO_INCREMENT PRIMARY KEY,
    id_material INT,
    FOREIGN KEY (id_material) REFERENCES MATERIAL(id_mt)
);

CREATE TABLE VENTA (
    id_vt INT AUTO_INCREMENT PRIMARY KEY,
    fecha_vt DATE,
    total_vt DECIMAL(10, 2),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usr)
);

CREATE TABLE VENTA_MATERIAL (
    id_venta INT,
    id_material INT,
    PRIMARY KEY (id_venta, id_material),
    FOREIGN KEY (id_venta) REFERENCES VENTA(id_vt),
    FOREIGN KEY (id_material) REFERENCES MATERIAL(id_mt)
);
