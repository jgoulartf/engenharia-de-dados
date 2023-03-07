# Banco de dados simples para uma farmácia

# Tabela Cliente

| Campo | Tipo |
| --- | --- |
| ID\_Cliente | INT |
| Nome | VARCHAR |
| Endereço | VARCHAR |
| Telefone | VARCHAR |

---

# Tabela Medicamento

| Campo | Tipo |
| --- | --- |
| ID\_Medicamento | INT |
| Nome | VARCHAR |
| Descrição | VARCHAR |
| Preço | FLOAT |
| ID\_Fornecedor | INT |

---

# Tabela Fornecedor

| Campo | Tipo |
| --- | --- |
| ID\_Fornecedor | INT |
| Nome | VARCHAR |
| Endereço | VARCHAR |
| Telefone | VARCHAR |

---

# Tabela Pedido

| Campo | Tipo |
| --- | --- |
| ID\_Pedido | INT |
| Data | DATETIME |
| ID\_Cliente | INT |
| ID\_Fornecedor | INT |

---

# Tabela Venda

| Campo | Tipo |
| --- | --- |
| ID\_Venda | INT |
| Data | DATETIME |
| ID\_Cliente | INT |
| ID\_Medicamento | INT |
| Quantidade | INT |

---

# Tabela Pedido_Medicamento

| Campo | Tipo |
| --- | --- |
| ID\_Pedido | INT |
| ID\_Medicamento | INT |
| Quantidade | INT |

---

# Tabela Venda_Medicamento

| Campo | Tipo |
| --- | --- |
| ID\_Venda | INT |
| ID\_Medicamento | INT |
| Quantidade | INT |
