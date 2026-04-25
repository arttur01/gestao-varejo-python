from repositorio import RepositorioEstoque
from fornecedor import Fornecedor
from produto import Produto
import pandas as pd

class EstoqueManager:
    def __init__(self, repositorio: RepositorioEstoque):
        self._repositorio = repositorio
        self._catalogo = {} # Começa vazio

    def carregar_dados(self):
        # Pega os dados do repositorio(catalogo) 
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
            print(f"Erro: Produto {nome} não cadastrado.")

    def dados_carregados(self, nome_arquivo):
        # Visualizar o catalogo em forma de tabela
        catalogo_carregado = pd.read_csv(nome_arquivo)
        print(catalogo_carregado)