from estoque_manager import EstoqueManager
from repositorio import RepositorioCSV
from fornecedor import Fornecedor

def main():
    # Configuração Inicial
    repo = RepositorioCSV("meu_estoque.csv")
    gerente = EstoqueManager(repo)
    gerente.carregar_dados() # O sistema 'acorda' com os dados do arquivo
    gerente.dados_carregados('meu_estoque.csv')
    

    # criando objeto Fornecedor para o teste
    distribuidora = Fornecedor("Atacado Tech", "12345678000199", 3)

    # Simulando programa
    print("--- Início da Operação ---")

    # Tentativa de Reposição
    gerente.receber_mercadoria("Teclado Mecânico", 20, distribuidora)

    # Tentativa de Venda
    monitor = gerente.buscar_produto("Monitor Odssey 27'")
    if monitor:
        monitor.vender(2)

    print("--- Operação Finalizada ---")
    gerente.salvar_dados() # Garante que tudo foi gravado no CSV

if __name__ == "__main__":
    main()