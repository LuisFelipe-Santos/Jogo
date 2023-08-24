from models.calcular import Calcular


class Jogo:
    def __init__(self):
        self.pontos = 0

    @staticmethod
    def mensagem() -> None:
        print(
            "\nBem-vindo!\nEste é um mini jogo para testar suas habilidades em matemática.\nPrimeiro, "
            "escolha a dificuldade do jogo e, em seguida, resolva o cálculo gerado aleatoriamente. "
            "terá que resolver.")

    def run(self):
        self.mensagem()
        while True:
            iniciar = input('Vamos começar? [Sim, Não]: ').strip().lower()
            if iniciar.lower() in ['sim', 's', 'ss', 'si']:
                while True:
                    dificuldade = self.obter_dificuldade()
                    calc = Calcular(dificuldade)

                    self.jogar_rodada(calc)
                    if not self.continuar_jogando():
                        return False
            elif iniciar.lower() in ['não', 'nao', 'n', 'no']:
                print('Até a próxima! 👋😊')
                return False
            else:
                print('Entrada inválida. Por favor, digite "Sim" ou "Não".')

    @staticmethod
    def obter_dificuldade():
        while True:
            try:
                dificuldade = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))
                if dificuldade in [1, 2, 3, 4]:
                    return dificuldade
                else:
                    print('Opção inválida. Escolha um nível entre 1, 2, 3 ou 4.')
            except ValueError:
                print('Entrada inválida. Por favor, insira um número inteiro.')

    def jogar_rodada(self, calc):
        while True:
            try:
                print('Informe o resultado da seguinte operação:')
                calc.mostrar_operacao()
                resultado = float(input('Resposta: '))

                if calc.checar_resultado(resultado):
                    self.pontos += 1
                    print(f'Você tem \033[1;33m{self.pontos}\033[0m ponto(s).')
                else:
                    if self.pontos > 0:
                        self.pontos -= 1  # Subtrai um ponto quando a resposta está errada
                        print(f'Você tem \033[1;31m{self.pontos}\033[0m ponto(s).')
                    else:
                        print(f'Você tem \033[1;31m{self.pontos}\033[0m ponto(s).')
                break
            except ValueError:
                print('Entrada inválida. Por favor, verifique sua resposta.\nPara respostas com número decimal, '
                      'use " . " invés de " , " e considere apenas um número após a virgula.')

    def continuar_jogando(self):
        while True:
            continuar = input('Deseja continuar no jogo? [Sim, Não] \nResposta: ').strip()

            if continuar.lower() in ['sim', 's', 'ss', 'si']:
                return True
            elif continuar.lower() in ['não', 'nao', 'n', 'no']:
                if self.pontos > 0:
                    print(f'Você finalizou com \033[1;33m{self.pontos}\033[0m ponto(s)🏆.')
                else:
                    print(f'Você finalizou com \033[1;31m{self.pontos}\033[0m! ponto(s).')
                print('Até a próxima! 👋😊')
                return False
            elif continuar.isnumeric():
                print('Entrada inválida. Por favor, digite "Sim" ou "Não".')
            else:
                print('Entrada inválida.')
