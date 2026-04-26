class Fornecedor:
    def __init__(self, nome: str, cnpj: str, tempo_entrega: int):
        # Formatando o CNPJ
        cnpj_limpo = cnpj.strip().replace(".", "").replace("/", "").replace("-", "")
        
        # Validação do CPNJ
        if len(cnpj_limpo) != 14:
            raise ValueError("CNPJ inválido! Deve conter 14 dígitos.")
            
        self._nome = nome.strip()
        self._cnpj = cnpj_limpo
        self._tempo_entrega = tempo_entrega
        
    def __str__(self):
        return f"{self.nome} (CNPJ: {self.cnpj}) - Entrega: {self.tempo_entrega} dias"
    
    @property
    def nome(self):
        return self._nome

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def tempo_entrega(self):
        return self._tempo_entrega