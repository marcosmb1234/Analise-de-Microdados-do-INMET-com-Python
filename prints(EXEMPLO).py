from modelos.estacao import *

o = EstacaoMeteorologica(
    nome="BRASILIA",
    codigo="A001",
    regiao="CO",
    uf="DF",
    latitude=-15.78944444,
    longitude=-47.92583332,
    altitude=1160.96
)

registro = RegistroMeteorologico(
    data="2023/01/01",
    hora="1200",
    precipitacao=0.0,
    temperatura=22.5,
    umidade=80.0
)

o.adicionar_registro(registro)
print(o.obter_registros())