# API de Consultas e Exportação para o Data Lake

Esta API em Django permite consultar dados de `DetailLine` e `GuestCheck`, e exportá-los para um Data Lake em formato JSON. A API possui três endpoints principais:

- **GetFiscalInvoiceAPIView**: Consulta faturas fiscais por `storeId` e `busDt`.
- **GetGuestChecksAPIView**: Consulta registros de `GuestCheck` por `storeId` e `busDt`.
- **GetTransactionsAPIView**: Consulta transações de `DetailLine` por `storeId` (e opcionalmente `busDt`).

Cada consulta retorna os dados em formato JSON e os salva no Data Lake.

## Pré-requisitos

- **Django** e **Django REST Framework** instalados.
- Banco de dados configurado com os modelos `DetailLine` e `GuestCheck`.
- Definir o caminho do Data Lake no `settings.py`:

```python
DATA_LAKE_PATH = '/caminho/para/data_lake'

Endpoints
1. POST /get-fiscal-invoice/
Consulta faturas fiscais por storeId e busDt.

Parâmetros:

storeId: ID da loja.
busDt: Data de negócios no formato YYYY-MM-DD.
Resposta:

200 OK: Dados de faturas fiscais.
400 Bad Request: Parâmetros ausentes ou inválidos.
404 Not Found: Nenhum dado encontrado.

2. POST /get-guest-checks/
Consulta GuestCheck por storeId e busDt.

Parâmetros:

storeId: ID da loja.
busDt: Data de fechamento no formato YYYY-MM-DD.
Resposta:

200 OK: Dados de GuestCheck.
400 Bad Request: Parâmetros ausentes ou inválidos.
404 Not Found: Nenhum dado encontrado.
3. POST /get-transactions/
Consulta transações por storeId (e opcionalmente busDt).

Parâmetros:

storeId: ID da loja.
busDt: Data de fechamento no formato YYYY-MM-DD (opcional).
Resposta:

200 OK: Dados de transações.
400 Bad Request: Formato de busDt inválido.
404 Not Found: Nenhum dado encontrado.
Exemplo de Arquivos no Data Lake
Os dados são salvos em arquivos JSON no seguinte formato:

Faturas fiscais: fiscal_invoices/{storeId}_{busDt}.json
GuestChecks: guest_checks/{storeId}_{busDt}.json
Transações: transactions/{storeId}_{busDt}.json ou transactions/{storeId}_no_date.json se busDt não for fornecido.

