from random import randint


class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 4)  # 1 = somar, 2 = diminuir, 3 = multiplicar, 4 = dividir
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        elif self.operacao == 4:
            op = 'Dividir'
        else:
            op = 'Operação desconhecida.'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:

        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(1, 100)
        elif self.dificuldade == 3:
            return randint(1, 1000)
        elif self.dificuldade == 4:
            return randint(1, 10000)
        else:
            return randint(1, 100000)

    @property
    def _gerar_resultado(self: object) -> int:

        if self.operacao == 1:  # somar
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # subtrair
            return self.valor1 - self.valor2
        elif self.operacao == 3:  # multiplicar
            return self.valor1 * self.valor2
        else:  # dividir
            return self.valor1 / self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return 'x'
        else:
            return '/'

    def checar_resultado(self: object, resposta: float) -> bool:
        certo: bool = False

        if round(self.resultado, 1) == round(resposta, 1):
            print('Resposta 🎉\033[1;32mCERTA\033[0m!🎉')
            certo = True
        else:
            print('Resposta \033[1;31mERRADA\033[0m!😥')
            print(f'A resposta correta é: \n{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado:.1f}')

        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
