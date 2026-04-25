from fornecedor import Fornecedor

class Produto:
    def __init__(self, nome: str, categoria: str, preco: float, estoque_atual: int, capacidade_maxima: int):
        self.nome = nome.strip()
        self.categoria = categoria.strip()
        self._preco = preco
        self._estoque_atual = estoque_atual
        self._capacidade_maxima = capacidade_maxima
        
        # Formatação do objeto da classe produto
    def __str__(self):
        return f"{self.nome} ({self.categoria}) - R$ {self._preco:.2f} | Estq: {self._estoque_atual}/{self._capacidade_maxima}"

        # Getter para evitar que o usuário tenha acesso direto ao atributo do objeto
    @property
    def preco(self):
        return self._preco

    @property
    def estoque_atual(self):
        return self._estoque_atual

    @property
    def capacidade_maxima(self):
        # Corrigido o erro de recursão (adicionado o _)
        return self._capacidade_maxima
    
    def repor_estoque(self, quantidade: int, fornecedor: Fornecedor) -> bool:
        
            # Validar se quantidade maior que 0 (zero) ou se fornecedor existe
        if quantidade <= 0 or not fornecedor:
            print("Erro: Quantidade inválida ou fornecedor não identificado.")
            return False
        
            # Validar a capacidade máxima do estoque e armazenar o produto
        if self._estoque_atual + quantidade <= self._capacidade_maxima:
            self._estoque_atual += quantidade
            print(f"Sucesso: {self.nome} reposto por {fornecedor.nome}.")
            return True
        else:
            sobra = (self._estoque_atual + quantidade) - self._capacidade_maxima
            print(f"RECUSADO: Sem espaço para {sobra} itens da {fornecedor.nome}.")
            return False

    def vender(self, quantidade: int) -> bool:
            # Validar quantidade do produto requisitado para venda
        if 0 < quantidade <= self._estoque_atual:
            self._estoque_atual -= quantidade
            total = quantidade * self._preco
            print(f"Venda: {quantidade}x {self.nome} | Total: R$ {total:.2f}")
            return True
        print(f"Erro: Estoque insuficiente para vender {quantidade} unidades.")
        return False