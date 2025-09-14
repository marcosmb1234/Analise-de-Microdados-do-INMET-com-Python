from typing import List
from .registro import RegistroMeteorologico

class Estatisticas:
    """
    Calcula e fornece estatísticas a partir de uma lista de registros meteorológicos.
    """
    def __init__(self, registros: List[RegistroMeteorologico]):
        self.registros = registros
    def media_temperatura(self) -> float:
        temperaturas = [r.temperatura for r in self.registros if r.temperatura is not None]
        if not temperaturas:
            return 0.0
        return sum(temperaturas) / len(temperaturas)

    def max_umidade(self) -> float:
        umidades = [r.umidade for r in self.registros if r.umidade is not None]
        if not umidades:
            return 0.0
        return max(umidades)

    def total_precipitacao(self) -> float:
        precipitacoes = [r.precipitacao for r in self.registros if r.precipitacao is not None]
        if not precipitacoes:
            return 0.0
        return sum(precipitacoes)
    def __str__(self) -> str:
        return (f"Média Temp: {self.media_temperatura():.2f}°C | \n"
                f"Máx Umidade: {self.max_umidade():.2f}% | \n"
                f"Total Precipitação: {self.total_precipitacao():.2f}mm\n\n")