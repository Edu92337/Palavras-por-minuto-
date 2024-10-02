import curses
from curses import wrapper # inicia o codigo com a função de dentro
import time
import random

def fazer_frases(qtd):  # retorna uma lista com uma quantidade aleatória de frases
    frases = { 
    1: "A arte de ser feliz está em saber aproveitar os pequenos momentos",
    2: "O oceano é vasto e misterioso, guardando segredos ainda não descobertos",
    3: "A prática constante leva à perfeição em qualquer habilidade",
    4: "Aprender novas línguas pode abrir portas para culturas diferentes",
    5: "A Lua ilumina a noite escura, refletindo a luz do Sol distante",
    6: "O aroma de flores no campo traz paz e tranquilidade à alma",
    7: "O avanço tecnológico transformou a maneira como vivemos e nos comunicamos",
    8: "A criatividade floresce quando nos permitimos explorar o desconhecido",
    9: "O esporte ensina disciplina, trabalho em equipe e resiliência",
    10: "O tempo é uma das poucas coisas que não podemos recuperar, apenas usar bem",
    11: "As estrelas cintilam no céu, lembrando-nos da vastidão do universo",
    12: "Ler é uma forma de viajar sem sair do lugar, mergulhando em histórias",
    13: "A natureza segue seu curso, mostrando a harmonia entre todas as coisas vivas",
    14: "A persistência diante das dificuldades é o que diferencia os vencedores",
    15: "A inteligência emocional é tão importante quanto o conhecimento técnico",
    16: "A curiosidade é a chave que abre portas para novas descobertas",
    17: "O silêncio pode ser a resposta mais sábia em muitos momentos",
    18: "Cada passo dado com confiança nos leva mais perto de nossos sonhos",
    19: "O universo é uma sinfonia de átomos e energia em constante movimento",
    20: "A bondade é um presente que não custa nada, mas vale muito"
    }

    # Retorna uma lista de frases aleatórias
    return random.sample(list(frases.values()), qtd)

def iniciar(window):
    altura, largura = window.getmaxyx() # atribui às variáveis as dimensões da janela
    window.clear()
    mensagem = 'Aperte 1 para começar!'
    window.addstr(altura // 2, (largura // 2) - len(mensagem) // 2, mensagem)
    window.refresh()
    init = window.getch()
    window.clear()
    return chr(init) == '1'

def cores(tag):# cria um par de cores que podem ser usadas
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    verdadeiro = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    falso = curses.color_pair(2)
    return verdadeiro if tag else falso

def finalização(letras_erradas, letras_totais, palavras, tempo, window):
    porcentage_acerto = 100 * (1 - letras_erradas / letras_totais)
    window.clear()
    window.addstr(f'Você digitou {(palavras/tempo)*60:.2f} palavras por minuto \nTeve um aproveitamento de: {porcentage_acerto:.2f}% ')
    window.refresh()
    time.sleep(10)

def main(window):
    if iniciar(window):
        frases = fazer_frases(random.randint(1,4))# Seleciona várias frases
        total_letras_erradas = 0
        total_letras = 0
        total_palavras = 0
        tempo_total = 0
        for frase in frases:
            window.clear()
            window.addstr(frase)
            window.refresh()

            palavras = len(frase.split())
            total_palavras += palavras
            letras_totais = len(frase)
            letras_erradas = 0
            inicio = time.time()

            i = 0
            while i < letras_totais:
                tecla = window.getch()

                if 0 <= tecla <= 255:
                    tecla = chr(tecla)
                else:
                    continue

                if tecla == frase[i]:
                    window.addstr(0, i, frase[i], cores(True))
                    window.refresh()
                    i += 1

                elif tecla in (curses.KEY_BACKSPACE, 127, 8, '\b', '\x7f'):
                    i = max(0, i - 1)
                    window.move(0, i)

                else:
                    window.addstr(0, i, frase[i], cores(False))
                    window.refresh()
                    letras_erradas += 1
                    i += 1

            final = time.time()
            tempo_total += final - inicio
            total_letras_erradas += letras_erradas
            total_letras += letras_totais

        finalização(total_letras_erradas, total_letras, total_palavras, tempo_total, window)
    else:
        pass

if __name__ == '__main__':
    wrapper(main)
