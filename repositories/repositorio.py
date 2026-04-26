import csv
from pathlib import Path
from models.produto import Produto

# BASE_DIR fica APENAS aqui. O repositório é o único que toca no disco rígido.
BASE_DIR = Path(__file__).resolve().parent.parent

class RepositorioEstoque:
    # Interface base para outros tipos de repositório (ex: RepositorioSQL no futuro)
    def carregar(self): pass
    def salvar(self, catalogo): pass

class RepositorioCSV(RepositorioEstoque):
    def __init__(self, nome_arquivo: str):
        # O repositório encapsula a lógica da pasta 'data/'. 
        # O resto do sistema nem precisa saber que essa pasta existe.
        self.caminho_arquivo = BASE_DIR / 'data' / nome_arquivo

    def carregar(self) -> dict:
        # Lê o CSV e devolve um dicionário de objetos produto
        novo_catalogo = {}
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
                leitor = csv.reader(f)
                next(leitor) # Pula cabeçalho
                for linha in leitor:
                    p = Produto(linha[0], linha[1], float(linha[2]), int(linha[3]), 1000)
                    novo_catalogo[p.nome] = p
            return novo_catalogo
        except FileNotFoundError:
            print(f"Aviso: Arquivo de banco de dados não encontrado em {self.caminho_arquivo}")
            return {}

    def salvar(self, catalogo: dict):
        # Pega o dicionário do gerente e grava no disco
        with open(self.caminho_arquivo, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(['Nome', 'Categoria', 'Preco', 'Estoque', 'Tela', 'Modelo'])
            for p in catalogo.values():
                escritor.writerow([p.nome, p.categoria, p.preco, p.estoque_atual, 'N/A', 'N/A'])