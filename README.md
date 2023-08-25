![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=Status:&message=Completo&color=GREEN&style=for-the-badge)  ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=Linguagem:&message=Python&color=GREEN&style=for-the-badge)
# Projeto 01 - Jogo

Projeto realizado durante o curso "Programação em Python do Básico ao Avançado" - Geek University.

> Projeto 1 - Jogo
> Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o
> nível de dificuldade do jogo e após isso gera e apresenta, de forma aletaória, um cálculo para que
> possamos informar o resultado.
> Iremos limitar as operações em somar, diminuir e multiplicar. Se o usuário acertar a resposta, somará 1 ponto ao seu. Acertando ou errando, ele poderá ou não continuar o jogo.

## Sobre esse projeto
Um jogo simples de matemática onde o jogador pode testar suas habilidades resolvendo cálculos matemáticos. O jogo possui as seguintes funcionalidades:

- **Escolha de Dificuldade**: Permite ao jogador escolher o nível de dificuldade (1 a 4) para os cálculos.

- **Geração de Cálculos**: Gera cálculos matemáticos aleatórios, incluindo operações de soma, subtração, multiplicação e divisão, dependendo da dificuldade escolhida.

- **Resolução de Cálculos**: Solicita ao jogador que resolva o cálculo apresentado e insira sua resposta.

- **Feedback de Resposta**: Fornece feedback imediato ao jogador sobre a precisão de sua resposta, informando se está correta ou errada.

- **Pontuação**: Mantém um registro da pontuação do jogador, atribuindo um ponto por cada resposta correta e permitindo que os pontos sejam perdidos caso a resposta esteja errada.

- **Continuação do Jogo**: Permite que o jogador escolha continuar jogando após cada rodada ou encerrar o jogo.

- **Gerenciamento de Erros**: Lida com entradas inválidas do jogador, como valores não numéricos ou fora do intervalo esperado.

## Melhorias
O código apresenta várias melhorias em comparação com a versão feita durante o curso, demonstrando uma abordagem mais robusta e organizada para a implementação do jogo. Aqui estão algumas das principais melhorias da versão atual em relação à versão base:
- **Separação de Responsabilidades**: O código foi dividido em métodos e classes específicas para tarefas como exibição de mensagens, controle do fluxo de jogo e geração de cálculos. Isso melhora a legibilidade e facilita a manutenção.

- **Controle de Fluxo Mais Claro**: Utiliza métodos como run(), jogar_rodada() e continuar_jogando() para gerenciar o fluxo do jogo. Isso torna o controle do jogo mais claro e permite uma abordagem mais interativa.

- **Tratamento de Erros Aprimorado**: Implementa tratamentos de erro mais abrangentes, lidando com respostas inválidas e fornecendo orientações claras para o jogador.

- **Gerenciamento de Pontos**: Permite que os pontos sejam incrementados quando o jogador responde corretamente e decrementados em caso de respostas erradas. Isso adiciona um elemento de desafio e recompensa ao jogo.

- **Feedback Detalhado**: Fornece feedback detalhado ao jogador, indicando se a resposta está certa ou errada e exibindo a resposta correta em caso de erro.

- **Personalização de Mensagens**: Possui mensagens formatadas com cores para melhorar a experiência do jogador, criando uma interface mais agradável e envolvente.

- **Legibilidade Aprimorada**: identação consistente, nomes de variáveis mais descritivos e comentários adequados para melhorar a legibilidade do código.

- **Reutilização de Código**: Encapsulamento de funcionalidades relacionadas em classes, o que facilita a reutilização do código em projetos futuros.



- **Versão antiga do projeto.**

![JogoRodandoOld](https://user-images.githubusercontent.com/117581817/263142978-679ae997-8742-49dc-92c6-6cad37265a87.png)

![JogoCodigoOLd](https://user-images.githubusercontent.com/117581817/263142985-215766d3-3b66-428e-9f9c-3f89d27ccffb.png)


- **Versão atualizada.**

![JogoRodandoNew](https://user-images.githubusercontent.com/117581817/263145422-4a36add1-0c57-4c39-9aa4-2ac78cdf9684.png)

![JogoCodigoNew](https://user-images.githubusercontent.com/117581817/263143940-6de4767b-0ec4-4385-ba18-8a96304a6d6e.png)


## Tecnologias utilizadas
- Python
- Orientação a objetos

## Bibliotecas utilizadas
- random
