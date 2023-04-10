create table vinho(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    uva VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    safra VARCHAR(255) NOT NULL,
    preco DECIMAL(10),
    regiao_colheita VARCHAR(255) NOT NULL
);


create table adega(
    vinho_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
        CONSTRAINT fk_vinho
            FOREIGN KEY(vinho_id)
                REFERENCES vinho(id)


);
