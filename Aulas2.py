from colorama import Fore, Style

pergunta1 = '1) Como usamos o present continuous? Descreva brevemente.'
pergunta2 = '2) Exemplos de present continuous? Forneça alguns.'
pergunta3 = '3) Quando usamos o gerúndio (ing) nos verbos? Explique em poucas palavras.'
pergunta4 = '4) Como formamos o present continuous? Dê uma breve explicação.'
s = True

resposta1 = f"{Fore.GREEN}O present continuous, também conhecido como presente contínuo, é um tempo verbal usado para expressar ações que estão ocorrendo no momento da fala ou em torno do presente, incluindo planos futuros definidos. Por exemplo, 'She is reading a book.' indica uma ação em andamento no momento da fala. Além disso, podemos dizer 'I am meeting friends tomorrow', onde a ação está planejada para o futuro próximo. Esse tempo verbal é formado com o verbo 'to be' no presente (am, is, are) seguido do verbo principal no gerúndio (-ing), como em 'He is eating' (Ele está comendo). É importante notar que o present continuous é usado para ações temporárias e não para estados permanentes.{Style.RESET_ALL}"

resposta2 = f"{Fore.BLUE}Exemplos comuns de present continuous incluem frases como 'He is swimming', 'They are dancing', 'I am writing', entre outros. Essas frases descrevem ações que estão ocorrendo no momento da fala ou em torno do presente. Cada exemplo mostra o verbo principal no gerúndio (-ing), seguindo o verbo 'to be' no presente (am, is, are), de acordo com a conjugação adequada. O presente contínuo é usado para expressar atividades temporárias e não estados permanentes. Ele também pode ser usado para descrever ações que estão em andamento no momento da fala ou planos futuros definidos.{Style.RESET_ALL}"

resposta3 = f"{Fore.YELLOW}O gerúndio (ing) é empregado nos verbos para denotar ações contínuas, em progresso ou repetidas. Ele é frequentemente utilizado com o presente contínuo para indicar que uma ação está ocorrendo no momento da fala ou em torno do presente. Por exemplo, em 'I am studying' (Eu estou estudando), 'studying' é o gerúndio do verbo 'to study'. Além disso, o gerúndio é usado em frases como 'He enjoys swimming' (Ele gosta de nadar) para indicar atividades habituais ou prazeres. Em geral, o gerúndio é versátil e é usado em várias situações para expressar ações contínuas ou repetidas.{Style.RESET_ALL}"

resposta4 = f"{Fore.MAGENTA}Para formar o present continuous, primeiro selecionamos o verbo 'to be' no presente, que pode ser 'am', 'is' ou 'are', dependendo do sujeito. Em seguida, acrescentamos o verbo principal no gerúndio (também conhecido como forma -ing), independente do sujeito. Por exemplo, para a primeira pessoa do singular (I), usamos 'am', como em 'I am eating' (Eu estou comendo). Para a terceira pessoa do singular (he/she/it), usamos 'is', como em 'He is reading' (Ele está lendo). Para a segunda pessoa do singular e todas as pessoas do plural, usamos 'are', como em 'They are playing' (Eles estão jogando). Assim, a formação do present continuous é bastante regular e segue essa estrutura básica.{Style.RESET_ALL}"

print(pergunta1)
print(pergunta2)
print(pergunta3)
print(pergunta4)

while s:
    rnum = input('Digite o número da pergunta que você quer saber: ')

    if rnum == "1":
        print(pergunta1)
        print(resposta1)
  
    elif rnum == "2":
        print(pergunta2)
        print(resposta2)
  
    elif rnum == "3":
        print(pergunta3)
        print(resposta3)
        
    elif rnum == "4":
        print(pergunta4)
        print(resposta4)
  
    elif rnum == '101':
        s = False
  
    elif rnum == 'cu':
        print('Quem leu é viado')
  
    elif rnum == 'gay':
        print('Gay é o Arthur')

    elif rnum == '123':
        print('Arthur corno muito manso')

    else:
        print('O número digitado não corresponde a nenhuma pergunta, tente novamente.')
