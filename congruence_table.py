class CongruenceTable:
    @staticmethod
    def with_factor(mod: int, factor: int) -> list[int]:
        return [factor * k % mod for k in range(mod)]

    @staticmethod
    def with_exponent(mod: int, exponent: int) -> list[int]:
        return [k**exponent % mod for k in range(mod)]
