import csv
from produto import Produto

class RepositorioEstoque:
    
        #Classe para outros tipos de repositório
        
    def carregar(self): pass
    def salvar(self, catalogo): pass

class RepositorioCSV(RepositorioEstoque):
    def __init__(self, nome_arquivo: str):
        self.arquivo = nome_arquivo

    def carregar(self) -> dict:

        #Lê o CSV e devolve um dicionário de objetos produto
        novo_catalogo = {}
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                leitor = csv.reader(f)
                next(leitor) # Pula cabeçalho
                for linha in leitor:
                    p = Produto(linha[0], linha[1], float(linha[2]), int(linha[3]), 1000)
                    novo_catalogo[p.nome] = p
            return novo_catalogo
        except FileNotFoundError:
            return {}

    def salvar(self, catalogo: dict):
        
        #Pega o dicionário do gerente e grava 
        with open(self.arquivo, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(['Nome', 'Categoria', 'Preco', 'Estoque', 'Tela', 'Modelo'])
            for p in catalogo.values():
                escritor.writerow([p.nome, p.categoria, p.preco, p.estoque_atual, 'N/A', 'N/A'])
    