class RegistroMeteorologico:
    """
    Representa os dados de uma única medição em um determinado momento.
    """
    def __init__(self, data: str, hora: str, temperatura: float, umidade: float, precipitacao: float):
        self.data = data
        self.hora = hora
        self.temperatura = temperatura
        self.umidade = umidade
        self.precipitacao = precipitacao

    def __str__(self) -> str:
        return (f"Data: {self.data} {self.hora} | "
                f"Temp: {self.temperatura}°C | "
                f"Umidade: {self.umidade}% | "
                f"Precipitação: {self.precipitacao}mm")