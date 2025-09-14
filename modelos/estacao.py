from typing import List
from .registro import RegistroMeteorologico

class EstacaoMeteorologica:
    """
    Representa uma estação meteorológica e agrega todos os seus registros.
    """
    def __init__(self, nome: str, codigo: str, regiao: str, uf: str, latitude: float, longitude: float, altitude: float):
        self.nome = nome
        self.codigo = codigo
        self.regiao = regiao
        self.uf = uf
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.registros: List[RegistroMeteorologico] = []

    def adicionar_registro(self, registro: RegistroMeteorologico) -> None:
        if isinstance(registro, RegistroMeteorologico):
            self.registros.append(registro)

    def obter_registros(self) -> List[RegistroMeteorologico]:
        return self.registros

    def __str__(self) -> str:
        return (
            f"Estação: {self.nome}\n"
            f"Código WMO: {self.codigo}\n"
            f"Região: {self.regiao}\n"
            f"UF: {self.uf}\n"
            f"Latitude: {self.latitude}\n"
            f"Longitude: {self.longitude}\n"
            f"Altitude: {self.altitude} m\n\n"
            f"Total de registros: {len(self.registros)}\n"
        )