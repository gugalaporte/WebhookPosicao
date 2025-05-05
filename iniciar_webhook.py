import requests
import json

# Configurações
CLIENT_ID = "69c668816d77c505c03ffe7cbbedbfb4"
CLIENT_SECRET = "CA35950C3C7C9606035C5312A8ACA44F48DFE43BF6D8790F3F895A87736DCA0E"
TOKEN_URL = "https://api.btgpactual.com/oauth/token"
BASE_URL = "https://api.btgpactual.com/iaas-api-position/api/v1/position/partner"

def obter_token():
    # Dados para obter o token
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        # Fazendo a requisição para obter o token
        response = requests.post(TOKEN_URL, data=data, headers=headers)
        
        if response.status_code == 200:
            token_data = response.json()
            return token_data.get("access_token")
        else:
            print(f"Erro ao obter token. Status code: {response.status_code}")
            print("Resposta:", response.text)
            return None
            
    except Exception as e:
        print(f"Erro ao obter token: {str(e)}")
        return None

def iniciar_webhook():
    # Primeiro, obtém o token
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJ0cmFkZU5hbWUiOiJGSU5BQ0FQIOKAkyBDT05TVUxUT1JJQSBGSU5BTkNFSVJBIEUgTUVSQ0FETyBERSBDQVBJVEFJUyBMVERBLiIsImFsbG93ZWRSb3V0ZXMiOiJINHNJQUFBQUFBQUEvNjFYUzIrY01CRCtRN0dzNXRoelYxV2xxbzNVM0N0akJoZ3R0cWx0U0dpVS85N3hMckFCakNGVkxydkx6amZ2Snc4L2Z6MSs1cUpCM24zaVQ1QlZ4cHhaSTZ6WFlMbkRVZ3ZmV3JqN2VycWhHdVBRbzlGM0QyOTVSZXNyWS9HdkNDUnV3dU05RjFLQ2M5NmNRVWRGOEVGVG5QaEM3S2JWL2tlck1yQ3ZNMUFPR2VpVmFhNUZMektzMGZkOFlFNUtHVWhNQ1MxS1VDUnhpNDJqTG94Vll1MDR1U2ZQek5pY0FuYjVkSE1WZVlmTzJGR3Vtek5qWTdpRnhsaFBYdzVzRjFId0J0TzBycG9Ud3ovTVc1SERnSmtwdHlDTklyZHl5Qm44b2VBZ09DYnEyc2lJbmtOeHI3RUFodHExVm1nSlNlaVFXOWFBdllRdTRCdHI4bFpTZEljZjMvSUZqd1ZtaU9GcTNpYUZkNkxHWFBoNTlsc0tJSDhCSmJCK0pVUDFlVWFkbUIxeklLeXMwdFM0aWdNRmRxbVVhQWtFazBhdVJmTnMxK0ZtM1kwbGNRMGtvKzlpc20xUm9XdWpkd0ZyTHdaOVJtZEcyQngxR1RYblJtWlp6MWJ4RzFES2RCY3ZIYXVRK3NlaWpBcGJ3NEpReWhTYVBDYTJ3R2NxZE5SVTlGRzFKY216T2toa21kRlJFZE5jY1RHcXRJSkppMUdTVVpRQ2hjNkpYRVNaRXhtS0liSitGYjJ4VERMaFlHT2dqTmEwRksrOFQrVmdnTXpaQzZ5QnVVcFk0Q1Y0Rmg2MzVhdlEzTzl6S2wwTTJqeEZHOGNVQmNvd2RxWldXQVJZc2Fzc3gxK3VQNWdXQ2w0WDlteWh2cHkrbng1UEc1dHNPZUVTU3krNWFXWklSeU9aU1hJamxPSzF0dnVsR2JtUjdXVVNURnVZRHh4ekd4SzRmWWxLMkRQbHVhbUZEN0hkbFp6RWw3UVRQQnVTRnRvMGRNTnlqdDltK09BM0YyVnBvYVFxWlpzYmFLYm1BeVQ0Wmh6dnF6VXpDaGhsSnpmY0V0eHFESk9ZaW5WanRXNEJkaFkxcDcxUTl3NlhjeVhORkVxOE1EV2FhRitLcG5GRjNkUHhGYVBDTXgwVmtweDZTNzIvT1RLdWliRjQ0NmlSZXJQNmZuWDc3WWk0UlN5UmlqaCtQNFZwdnZFNGpjWEgrVTdGYXlGaHdHLzluNWEvbXpHK0hGSkJuVlFjVGtPTVkza2c3dHdJOFFoYUtHai9WZ2M2NURZS2hxUGcyQld4TVUvWWxQajFoYkVHRlcxZFQrZlVBV2hxa0t4WmxORytxdnRqcUlObWpPajNXZklFY040MTVBbzZhTWNBVG83bzZHMHdRMlNXWGlzdG5jdEU4dURpbCswU1JLOW5HTjZ4dXVsKytnZktRRHloQVE4QUFBPT0iLCJwYXJ0bmVyIjp7ImNnZSI6IjUwNDA4MCIsInRyYWRlTmFtZSI6IkZJTkFDQVAg4oCTIENPTlNVTFRPUklBIEZJTkFOQ0VJUkEgRSBNRVJDQURPIERFIENBUElUQUlTIExUREEuIiwiY25waiI6IjAxMjk0OTI5MDAwMTMzIn0sImF1dGgiOiJvYXV0aDIiLCJpc3MiOiJidGdwYWN0dWFsIiwiZXhwIjoxNzQ2NDc5Njk1LCJ0eXBlIjoiZGV2ZWxvcGVyIiwidXNlciI6eyJuYW1lIjoiR3VzdGF2byBMYXBvcnRlIiwiaWQiOjE2OTQsImVtYWlsIjoiZ3VzdGF2by5sYXBvcnRlQGZpbmFjYXAuY29tLmJyIn0sImlhdCI6MTc0NjQ3NjA5NX0.E220Dil85zrav09W-tA4vK7IpMeaWxE-ZCZK9RbzYyKUfnecKr7hBaLQTS8UPzfpzUEpdcXY9OA9nBQfehCNqR3ZIRIIWXxwneQ-AKzcy6g3Q7J6nU5RQG5D3jUd4SsxYuuz9iCTlBvDGkIC36Z2MvQx5QJPj-w3eKq5-Xw5dZz8ui3zk0r-xF3KSXNM-cjEnG8qq8x1w2JQ97qNSffAJO_2x2n3hOCkAq_zQVJ6qxROvhnI2IWRmXXilTy3y-6ZDgim5UAnYLh2Hja4P-cchI7Kx_2cTLVY84aRUFh5oe8-jno7tQghuZRWpaysqs3HMEg4U5sKAuG87dlOgMie9Q",
    "cache-control: max-age=0,no-cache",
    "content-length: 0", 
    "date: Mon,05 May 2025 20:14:55 GMT", 
    "expires: Mon,05 May 2025 20:14:55 GMT", 
    "pragma: no-cache",
    "x-id-pactual: ed1e82d3-0cef-4a71-886d-fbed504424e6"
    
    if not token:
        print("Não foi possível obter o token de acesso")
        return
    
    # Headers com o token de acesso
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        # Fazendo a chamada POST para iniciar o webhook
        response = requests.post(BASE_URL, headers=headers)
        
        # Verificando a resposta
        if response.status_code == 200:
            print("Webhook iniciado com sucesso!")
            print("Resposta:", json.dumps(response.json(), indent=2))
        else:
            print(f"Erro ao iniciar webhook. Status code: {response.status_code}")
            print("Resposta:", response.text)
            
    except Exception as e:
        print(f"Erro ao fazer a requisição: {str(e)}")

if __name__ == "__main__":
    iniciar_webhook() 