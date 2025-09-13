import csv
import os
import glob

from typing import List
from modelos.estacao import EstacaoMeteorologica
from modelos.registro import RegistroMeteorologico


def carregar_dados_pasta(caminho_base: str, ano: str) -> List[EstacaoMeteorologica]:
    """
    Busca por todos os arquivos .csv, lê cada um e cria objetos EstacaoMeteorologica
    e RegistroMeteorologico para estruturar os dados.
    """
    pasta_ano = os.path.join(caminho_base, str(ano))
    if not os.path.isdir(pasta_ano):
        print(f"AVISO: A pasta '{pasta_ano}' não foi encontrada.")
        return []

    lista_arquivos = glob.glob(os.path.join(pasta_ano, '*.csv'))
    if not lista_arquivos:
        print(f"AVISO: Nenhum arquivo .csv encontrado em '{pasta_ano}'.")
        return []

    print(f"Arquivos encontrados em '{pasta_ano}':")
    lista_de_estacoes = []

    for arquivo in lista_arquivos:
        print(f" - Processando: {os.path.basename(arquivo)}")
        try:
            with open(arquivo, mode='r', encoding='latin-1', newline='') as f:
                linhas_cabecalho = [next(f) for _ in range(8)]

                # Cabeçalho
                regiao = linhas_cabecalho[0].split(';')[1].strip()
                uf = linhas_cabecalho[1].split(';')[1].strip()
                nome_estacao = linhas_cabecalho[2].split(';')[1].strip()
                codigo_wmo = linhas_cabecalho[3].split(';')[1].strip()

                latitude = float(linhas_cabecalho[4].split(';')[1].strip().replace(',', '.'))
                longitude = float(linhas_cabecalho[5].split(';')[1].strip().replace(',', '.'))
                altitude = float(linhas_cabecalho[6].split(';')[1].strip().replace(',', '.'))

                estacao_atual = EstacaoMeteorologica(
                    nome=nome_estacao, codigo=codigo_wmo, regiao=regiao, uf=uf,
                    latitude=latitude, longitude=longitude, altitude=altitude
                )

                # Pula a nona linha, que é o cabeçalho das colunas de dados
                next(f)

                leitor_csv = csv.reader(f, delimiter=';')

                for linha in leitor_csv:
                    # LIMPEZA E CONVERSÃO DOS DADOS DE CADA LINHA
                    # Os dados vêm como texto, precisamos convertê-los para números.
                    data = linha[0]
                    hora = linha[1]

                    try:
                        precipitacao = float(linha[2].replace(',', '.'))
                    except ValueError:
                        precipitacao = None 

                    try:
                        temperatura = float(linha[7].replace(',', '.'))
                    except ValueError:
                        temperatura = None

                    try:
                        umidade = float(linha[15].replace(',', '.'))
                    except ValueError:
                        umidade = None
                    novo_registro = RegistroMeteorologico(
                        data=data, hora=hora, precipitacao=precipitacao,
                        temperatura=temperatura, umidade=umidade
                    )
                    estacao_atual.adicionar_registro(novo_registro)
                lista_de_estacoes.append(estacao_atual)

        except Exception as e:
            print(f"  ERRO ao processar o arquivo {os.path.basename(arquivo)}: {e}")

    print(f"\nSucesso! {len(lista_de_estacoes)} estações foram carregadas com seus respectivos dados.")
    return lista_de_estacoes