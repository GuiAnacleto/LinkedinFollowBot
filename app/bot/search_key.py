def escrever_arquivo_texto(texto , nome_arquivo = "search-key.txt"):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(texto)
        print(f"Chave de Busca Alterada com Sucesso.")
    except Exception as e:
        print(f"Erro ao alterar chave de busca: ", e)

def ler_arquivo_texto(nome_arquivo = "search-key.txt"):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{nome_arquivo}':", e)
