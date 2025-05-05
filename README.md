# API Webhook BTG Posições

API para receber e processar dados de posições do BTG via webhook.

## Configuração

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o servidor:
```bash
python app.py
```

## Endpoints

### POST /webhook/posicoes

Recebe os dados de posições do BTG.

**Headers necessários:**
- X-API-Key: finacap2025
- Content-Type: application/json

**Resposta de sucesso:**
```json
{
    "mensagem": "Dados recebidos e salvos com sucesso",
    "arquivo": "dados/posicoes_YYYYMMDD_HHMMSS.json"
}
```

## Estrutura de Arquivos

- `app.py`: Código principal da aplicação
- `dados/`: Diretório onde os arquivos JSON são salvos
- `requirements.txt`: Dependências do projeto

## Deploy

Para deploy em produção, recomenda-se usar o Gunicorn:

```bash
gunicorn app:app
``` 