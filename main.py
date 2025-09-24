import requests
import json
import os


try:
    with open('openapi.json', 'r') as f:
        data = json.load(f)
        API_KEY = 'sk-lWs1E41we0NIkt8JruuvO31pV3ZLsn8ZEsFzgsCILkaEw1Vc'


except FileNotFoundError:
    print("Erro: O arquivo 'openapi.json' não foi encontrado.")
    print("Por favor, crie um arquivo 'openapi.json' com a sua chave de API.")
    exit()
except json.JSONDecodeError:
    print("Erro: O arquivo 'openapi.json' não é um JSON válido.")
    exit()
except Exception as e:
    print(f"Ocorreu um erro ao carregar a chave de API: {e}")
    exit()


url = "https://api.stability.ai/v2beta/audio/stable-audio-2/text-to-audio"
headers = {
    "authorization": f"Bearer {API_KEY}",
    "accept": "audio/*",
}

def gerar_audio_ia(prompt):
    """
    Função que faz a chamada à API da Stability AI para gerar o áudio.
    """

    data = {
        "prompt": (None, prompt),
        "duration": (None, "15"),
        "output_format": (None, "wav"),
        "model": (None, "stable-audio-2.5"),
    }
    
    try:
        print("Enviando requisição para a API da Stability AI...")
        response = requests.post(
            url,
            headers=headers,
            files=data,
        )

        # Verifica se a requisição foi bem-sucedida (código 200)
        if response.status_code == 200:
            with open("trilha_sonora.wav", "wb") as f:
                f.write(response.content)
            print("Áudio gerado com sucesso! Arquivo 'trilha_sonora.wav' foi criado.")
            return "trilha_sonora.wav"
        else:
            print(f"Erro ao gerar o áudio. Código de status: {response.status_code}")
            print(f"Mensagem de erro: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de conexão: {e}")
        return None


if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Trilhas Sonoras com Stable Audio!")
    print("Descreva a cena para gerar a música (ex: 'calm piano melody with cinematic strings').")
    descricao = input("Sua descrição: ")

    if descricao:
        print("Gerando áudio, por favor aguarde...")
        arquivo_audio = gerar_audio_ia(descricao)
        if arquivo_audio:
            print(f"Para ouvir o áudio, abra o arquivo {arquivo_audio}.")