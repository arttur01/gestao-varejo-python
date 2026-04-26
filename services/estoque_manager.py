from repositories.repositorio import RepositorioEstoque
from models.fornecedor import Fornecedor
from models.produto import Produto
import pandas as pd

class EstoqueManager:
    # Injeção de dependência: O Manager recebe o repositório pronto.
    def __init__(self, repositorio: RepositorioEstoque):
        self._repositorio = repositorio
        self._catalogo = {} # Começa vazio

    def carregar_dados(self):
        # Pega os dados do repositorio (catalogo) 
        self._catalogo = self._repositorio.carregar()

    def salvar_dados(self):
        # Salva os dados catálogo atual
        self._repositorio.salvar(self._catalogo)

    def buscar_produto(self, nome: str) -> Produto:
        # Busca o produto no catalogo
        return self._catalogo.get(nome.strip())

    def receber_mercadoria(self, nome: str, qtd: int, fornecedor: Fornecedor):
        p = self.buscar_produto(nome)
        # Valida se o produto esta cadastrado/existe no catalogo
        if p:
            p.repor_estoque(qtd, fornecedor)
            self.salvar_dados() # Salva automaticamente após repor
        else:
            print(f"Erro: Produto '{nome}' não cadastrado.")

    def exibir_tabela_pandas(self):
        """
        Acessa o caminho do arquivo de forma segura através do repositório 
        para gerar a visualização via Pandas.
        """
        if hasattr(self._repositorio, 'caminho_arquivo'):
            df = pd.read_csv(self._repositorio.caminho_arquivo)
            print("\n--- Visão Geral do Estoque ---")
            print(df)
            print("------------------------------\n")