def soma(a: float, b: float) -> float:
    return a + b


def media(valores: list[float]) -> float:
    if not valores:
        raise ValueError("lista vazia")
    return sum(valores) / len(valores)

if __name__ == "__main__":
    print("APP OK")
    print("soma(2,3) =", soma(2, 3))
    print("media([2,4,6]) =", media([2, 4, 6]))

