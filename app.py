from flask import Flask, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

# Configuração da API key
API_KEY = "finacap2025"

# Função para validar a API key
def validar_api_key():
    api_key = request.headers.get('X-API-Key')
    if not api_key or api_key != API_KEY:
        return False
    return True

# Função para salvar os dados em JSON
def salvar_dados(dados):
    # Criar diretório para os arquivos se não existir
    if not os.path.exists('dados'):
        os.makedirs('dados')
    
    # Gerar nome do arquivo com timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f'dados/posicoes_{timestamp}.json'
    
    # Salvar dados em arquivo JSON
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    
    return nome_arquivo

@app.route('/webhook/posicoes', methods=['POST'])
def receber_posicoes():
    # Validar API key
    if not validar_api_key():
        return jsonify({'erro': 'API key inválida'}), 401
    
    try:
        # Obter dados da requisição
        dados = request.get_json()
        
        # Validar se os dados contêm as informações necessárias
        if not dados or 'response' not in dados:
            return jsonify({'erro': 'Dados inválidos'}), 400
        
        # Salvar dados em arquivo JSON
        nome_arquivo = salvar_dados(dados)
        
        return jsonify({
            'mensagem': 'Dados recebidos e salvos com sucesso',
            'arquivo': nome_arquivo
        }), 200
        
    except Exception as e:
        return jsonify({'erro': f'Erro ao processar requisição: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 