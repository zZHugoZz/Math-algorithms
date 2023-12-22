class CongruenceTable:
    @staticmethod
    def with_factor(mod: int, factor: int) -> dict[int, int]:
        return {k: factor * k % mod for k in range(mod)}

    @staticmethod
    def with_exponent(mod: int, exponent: int) -> dict[int, int]:
        return {k: k**exponent % mod for k in range(mod)}
