def soma(a: float, b: float) -> float:
    return a + b


def media(valores: list[float]) -> float:
    if not valores:
        raise ValueError("lista vazia")
    return sum(valores) / len(valores)
