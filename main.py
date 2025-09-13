import leitor
import csv
from modelos.estatisticas import Estatisticas

def carregar_dados():
    """
    Função dedicada a lidar com a lógica de carregar os dados.
    Pede ao usuário a pasta e o ano, e chama o leitor.
    """
    print("\n--- Carregando Dados das Estações ---")
    pasta = input("Digite o nome da pasta base (ex: dados_estacoes): ")
    ano = input("Digite o ano que deseja analisar (ex: 2024): ")

    dados = leitor.carregar_dados_pasta(pasta, ano)

    if not dados:
        print("\nNenhum dado foi carregado. Verifique se a pasta e o ano estão corretos.")
        return None

    return dados


def exibir_estacoes(lista_estacoes):
    """
    Função dedicada a exibir os detalhes de todas as estações carregadas.
    """
    if not lista_estacoes:
        print("\nERRO: Você precisa carregar os dados primeiro (Opção 1).")
        return 

    print("\n--- Detalhes das Estações Carregadas ---")
    for estacao in lista_estacoes:
        print(estacao) 

        if registros:
            print("    - Primeiros 5 registros:")
            for registro in registros[:5]:
                print(f"      -> {registro}") 
        else:
            print("    - Esta estação não possui registros.")
        print("-" * 55)


def exibir_estatisticas(lista_estacoes):
    """
    Função dedicada a exibir as estatísticas de uma estação escolhida pelo usuário.
    """
    if not lista_estacoes:
        print("\nERRO: Você precisa carregar os dados primeiro (Opção 1).")
        return

    print("\n--- Escolha uma Estação para ver as Estatísticas ---")
    for i, estacao in enumerate(lista_estacoes):
        print(f"{i + 1}. {estacao.nome} ({estacao.codigo})")

    try:
        escolha = int(input("\nDigite o número da estação: "))
        estacao_selecionada = lista_estacoes[escolha - 1]

        stats = Estatisticas(estacao_selecionada.obter_registros())

        print(f"\n--- Estatísticas para a Estação: {estacao_selecionada.nome} ---")
        print(f"Temperatura Média: {stats.media_temperatura():.2f}°C")
        print(f"Umidade Máxima: {stats.max_umidade():.1f}%")
        print(f"Precipitação Total no Período: {stats.total_precipitacao():.2f}mm")
        print("-" * 55)

    except (ValueError, IndexError):
        print("ERRO: Escolha inválida. Por favor, digite um número da lista.")


def filtrar_dados_por_data(lista_estacoes):
    """
    Permite ao usuário escolher uma estação e filtrar seus registros por um período de datas.
    """
    if not lista_estacoes:
        print("\nERRO: Você precisa carregar os dados primeiro (Opção 1).")
        return

    print("\n--- Escolha uma Estação para Filtrar os Dados ---")
    for i, estacao in enumerate(lista_estacoes):
        print(f"{i + 1}. {estacao.nome} ({estacao.codigo})")

    try:
        escolha = int(input("\nDigite o número da estação: "))
        estacao_selecionada = lista_estacoes[escolha - 1]

        data_inicio = input("Digite a data de início (formato AAAA/MM/DD): ")
        data_fim = input("Digite a data de fim (formato AAAA/MM/DD): ")

        if len(data_inicio) != 10 or len(data_fim) != 10 or data_inicio[4] != '/' or data_fim[4] != '/':
            print("ERRO: Formato de data inválido. Use AAAA/MM/DD e tente novamente.")
            return

        registros_filtrados = []
        todos_os_registros = estacao_selecionada.obter_registros()

        for registro in todos_os_registros:
            if registro.data and (data_inicio <= registro.data <= data_fim):
                registros_filtrados.append(registro)

        print(f"\n--- Registros para '{estacao_selecionada.nome}' entre {data_inicio} e {data_fim} ---")

        if not registros_filtrados:
            print("Nenhum registro encontrado para este período.")
        else:
            for registro in registros_filtrados:
                print(f" -> {registro}")
            print(f"\nTotal de {len(registros_filtrados)} registros encontrados.")
        print("-" * 55)

    except (ValueError, IndexError):
        print("ERRO: Escolha inválida. Por favor, digite um número da lista.")

def exportar_relatorio(lista_estacoes):
    """
    Permite ao usuário escolher uma estação e exportar um relatório completo em .txt,
    contendo dados da estação, estatísticas e todos os registros.
    """
    if not lista_estacoes:
        print("\nERRO: Você precisa carregar os dados primeiro (Opção 1).")
        return

    print("\n--- Escolha uma Estação para Exportar o Relatório ---")
    for i, estacao in enumerate(lista_estacoes):
        print(f"{i + 1}. {estacao.nome} ({estacao.codigo})")

    try:
        escolha = int(input("\nDigite o número da estação: "))
        estacao_selecionada = lista_estacoes[escolha - 1]

        registros = estacao_selecionada.obter_registros()
        if not registros:
            print("ERRO: Esta estação não possui registros para exportar.")
            return

        from modelos.estatisticas import Estatisticas
        stats = Estatisticas(registros)

        temp_media = stats.media_temperatura()
        umid_max = stats.max_umidade()
        precip_total = stats.total_precipitacao()

        if registros:
            data_inicio = registros[0].data
            data_fim = registros[-1].data
        else:
            data_inicio = data_fim = "N/A"

        nome_arquivo = input("Digite o nome para o arquivo de relatório (ex: relatorio_brasilia.txt): ")

        if not nome_arquivo.lower().endswith('.txt'):
            nome_arquivo += '.txt'

        linhas_dados = ""
        for reg in registros:
            linhas_dados += f"{reg.data:10} {reg.hora:6} {reg.temperatura!s:9} {reg.umidade!s:8} {reg.precipitacao!s:12}\n"

        relatorio = (
            "===========================\n"
            " RELATÓRIO METEOROLÓGICO\n"
            "===========================\n\n"
            f"Estação: {estacao_selecionada.nome}\n"
            f"Código WMO: {estacao_selecionada.codigo}\n"
            f"Região: {estacao_selecionada.regiao}\n"
            f"UF: {estacao_selecionada.uf}\n"
            f"Latitude: {estacao_selecionada.latitude}\n"
            f"Longitude: {estacao_selecionada.longitude}\n"
            f"Altitude: {estacao_selecionada.altitude} m\n\n"
            f"Total de registros: {len(registros)}\n\n"
            "---------------------------\n"
            "Estatísticas:\n"
            "---------------------------\n"
            f"Temperatura média: {temp_media:.2f} °C\n"
            f"Umidade máxima: {umid_max:.2f} %\n"
            f"Precipitação total: {precip_total:.2f} mm\n"
            "---------------------------\n"
            "Fim do relatório.\n"
        )

        with open(nome_arquivo, mode='w', encoding='utf-8') as f:
            f.write(relatorio)

        print(f"\nRelatório '{nome_arquivo}' exportado com sucesso na pasta do projeto!")
        print("-" * 55)

    except (ValueError, IndexError):
        print("ERRO: Escolha inválida. Por favor, digite um número da lista.")

def menu():
    """
    Exibe o menu principal e chama as funções apropriadas com base na escolha do usuário.
    """
    dados_carregados = None

    while True:
        print("\n===== MENU DE ANÁLISE DE DADOS METEOROLÓGICOS =====")
        print("1. Carregar arquivos da pasta")

        if dados_carregados is not None:
            print("2. Exibir dados das estações")
            print("3. Exibir estatísticas de uma estação")
            print("4. Filtrar dados por data")
            print("5. Exportar relatório")

        print("6. Sair")
        print("=" * 55)

        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("ERRO: Por favor, digite um número válido.")
            continue

        if op == 1:
            dados_carregados = carregar_dados()
        elif op == 2:
            exibir_estacoes(dados_carregados)
        elif op == 3:
            exibir_estatisticas(dados_carregados)
        elif op == 4:
            filtrar_dados_por_data(dados_carregados)
        elif op == 5:
            exportar_relatorio(dados_carregados)
        elif op == 6:
            print("Saindo do programa. Até mais!")
            break
        else:
            print("ERRO: Opção inválida. Tente novamente.")


# +-+-+- INICIO -+-+-+

def main():
    print("Bem-vindo ao Sistema de Análise Meteorológica!")
    menu()


if __name__ == "__main__":
    main()