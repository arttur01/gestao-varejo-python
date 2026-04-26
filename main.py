from models.fornecedor import Fornecedor
from services.estoque_manager import EstoqueManager
from repositories.repositorio import RepositorioCSV

def main():
    # 1. Configuração Inicial
    # Passamos apenas o nome do arquivo. O Repositorio cuida do caminho "data/"
    repo = RepositorioCSV("meu_estoque.csv")
    gerente = EstoqueManager(repo)
    
    # O sistema 'acorda' com os dados do arquivo CSV
    gerente.carregar_dados() 
    
    # Exibe o Pandas usando o novo método refatorado
    gerente.exibir_tabela_pandas()

    # 2. Criando objeto Fornecedor para o teste
    distribuidora = Fornecedor("Atacado Tech", "12345678000199", 3)

    # 3. Simulando programa
    print("--- Início da Operação ---")

    # Tentativa de Reposição
    gerente.receber_mercadoria("Teclado Mecânico", 20, distribuidora)

    # Tentativa de Venda
    monitor = gerente.buscar_produto("Monitor Odssey 27'")
    if monitor:
        monitor.vender(2)

    print("--- Operação Finalizada ---")
    
    # Garante que tudo foi gravado no CSV antes do programa fechar
    gerente.salvar_dados() 
    
    # Exibe novamente para comprovar que o Pandas lê os dados atualizados
    gerente.exibir_tabela_pandas()

if __name__ == "__main__":
    main()