import pygame as pg
from pygame.locals import *
from sys import exit
from time import sleep


pg.init()

rec_1 = pg.Rect(110, 113, 75, 75)
rec_2 = pg.Rect(210, 113, 75, 75)
rec_3 = pg.Rect(310, 113, 75, 75)
rec_4 = pg.Rect(110, 213, 75, 75)
rec_5 = pg.Rect(210, 213, 75, 75)
rec_6 = pg.Rect(310, 213, 75, 75)
rec_7 = pg.Rect(110, 313, 75, 75)
rec_8 = pg.Rect(210, 313, 75, 75)
rec_9 = pg.Rect(310, 313, 75, 75)

tabuleiro = pg.Rect(108, 108, 284, 284)

rec = [rec_1, rec_2, rec_3, rec_4, rec_5, rec_6, rec_7, rec_8, rec_9]
tela = pg.display.set_mode((500, 500), 0, 32)
pg.display.set_caption('Jogo da Velha')
arial = pg.font.SysFont('arial', 35, True)
mostra = arial.render('# Jogo da Velha #', True, (255, 255, 255))
tela.blit(mostra, (100, 30))

pon_X = 0
pon_o = 0
jogo = False
moves = 0
vez_a = ''
jogador = ['pl1', 'pl2']
winner = False
vez = jogador[0]
tabu = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]
def draw_tabu():
    # arial = pg.font.SysFont('arial', 35, True)
    # placar = f'X : {}pts  O : {}pts'
    # mostra = arial.render(placar, True, (0, 0, 150))
    # tela.blit(mostra, (70, 70))
    for i in range(100, 500, 100):
        pg.draw.line(tela, (100, 200, 100), (96, i), (400, i), 10)
        pg.draw.line(tela, (100, 200, 100), (i, 96), (i, 405), 10)

def xis(pos):
    x, y = pos
    pg.draw.line(tela, (100, 200, 100), (x-24, y-24), (x+30, y+24), 10)
    pg.draw.line(tela, (100, 200, 100), (x-24, y+24), (x+30, y-24), 10)

def desenha():
    global moves, vez, winner, jogo, vez_a
    for p in rec:
        if p.collidepoint(mouse_pos):
            if p == rec_1:
                if vez == 'pl1':
                    if tabu[0][0] == '':
                        xis(p.center)
                        tabu[0][0] = 'x'
                        moves += 1
                        jogo = True
                    else:
                        print('lugar ocupado')
                else:
                    if tabu[0][0] == '' and tabu[0][0] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[0][0] = 'o'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False

            if p == rec_2:
                if vez == 'pl1':
                    if tabu[0][1] == '':
                        xis(p.center)
                        tabu[0][1] = 'x'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
                else:
                    if tabu[0][1] == '' and tabu[0][1] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[0][1] = 'o'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
            if p == rec_3:
                if vez == 'pl1':
                    if tabu[0][2] == '':
                        xis(p.center)
                        tabu[0][2] = 'x'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
                else:
                    if tabu[0][2] == '' and tabu[0][2] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[0][2] = 'o'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
            if p == rec_4:
                if vez == 'pl1':
                    if tabu[1][0] == '':
                        xis(p.center)
                        tabu[1][0] = 'x'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
                else:
                    if tabu[1][0] == '' and tabu[1][0] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[1][0] = 'o'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
            if p == rec_5:
                if vez == 'pl1':
                    if tabu[1][1] == '':
                        xis(p.center)
                        tabu[1][1] = 'x'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
                else:
                    if tabu[1][1] == '' and tabu[1][1] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[1][1] = 'o'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
            if p == rec_6:
                if vez == 'pl1':
                    if tabu[1][2] == '':
                        xis(p.center)
                        tabu[1][2] = 'x'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
                else:
                    if tabu[1][2] == '' and tabu[1][2] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[1][2] = 'o'
                        moves += 1
                        jogo = True
                    else:
                        jogo = False
            if p == rec_7:
                if vez == 'pl1':
                    if tabu[2][0] == '':
                        xis(p.center)
                        tabu[2][0] = 'x'
                        moves += 1
                        jogo = True
                    else:
                         jogo = False
                else:
                    if tabu[2][0] == '' and tabu[2][0] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[2][0] = 'o'
                        moves += 1
                        jogo = True
                    else:
                         jogo = False
            if p == rec_8:
                if vez == 'pl1':
                    if tabu[2][1] == '':
                        xis(p.center)
                        tabu[2][1] = 'x'
                        moves += 1
                        jogo = True
                    else:
                         jogo = False
                else:
                    if tabu[2][1] == '' and tabu[2][1] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[2][1] = 'o'
                        moves += 1
                        jogo = True
                    else:
                         jogo = False
            if p == rec_9:
                if vez == 'pl1':
                    if tabu[2][2] == '':

                        xis(p.center)
                        tabu[2][2] = 'x'
                        moves += 1
                        jogo = True
                    else:
                         jogo = False
                else:
                    if tabu[2][2] == '' and tabu[2][2] != 'x':
                        pg.draw.circle(tela, (0, 0, 100), p.center, 35)
                        tabu[2][2] = 'o'
                        moves += 1
                        jogo = True
                    else:
                         jogo = False
            if jogo:
                if vez == jogador[0]:
                    vez_a = '"X"'
                    vez = jogador[1]
                else:
                    vez_a = '"O"'
                    vez = jogador[0]
        continue

def checa():
    global moves, vez
    arial = pg.font.SysFont('arial', 50)
    mensagem = f'Player {vez_a} Venceu!!'

    # horizontal
    if tabu[0][0] == tabu[0][1] == tabu[0][2] != '':
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (70, 430))
        return True
    elif tabu[1][0] == tabu[1][1] == tabu[1][2] != '':
        # print(f'O jogador {vez} ganhou')
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (70, 430))
        return True
    elif tabu[2][0] == tabu[2][1] == tabu[2][2] != '':
        # print(f'O jogador {vez} ganhou')
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (70, 430))
        return True
    # diagonal 1
    elif tabu[0][0] == tabu[1][1] == tabu[2][2] != '':
        # print(f'O jogador {vez} ganhou')
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (70, 430))
        return True
    # diagonal 2
    elif tabu[2][0] == tabu[1][1] == tabu[0][2] != '':
        # print(f'O jogador {vez} ganhou')
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (70, 430))
        return True
    # vertical
    elif tabu[0][0] == tabu[1][0] == tabu[2][0] != '':
        # print(f'O jogador {vez} ganhou')
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (70, 430))
        return True
    elif tabu[0][1] == tabu[1][1] == tabu[2][1] != '':
        # print(f'O jogador {vez} ganhou')
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (70, 430))
        return True
    elif tabu[0][2] == tabu[1][2] == tabu[2][2] != '':
        # print(f'O jogador {vez} ganhou')
        mens_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
        tela.blit(mens_vitoria, (70, 430))
        return True
    else:
        if moves == 9:
            texto_v()
            moves += 1
            return False
        else:
            return False



def restart():
    global winner, vez, tabu, moves, pon_o, pon_X
    winner = False
    moves = 0
    vez = jogador[0]
    tabu = [
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
    ]
    if pon_o == 5 or pon_X == 5:
        pon_o = 0
        pon_X = 0
    tela.fill(0)
    tela.blit(mostra, (100, 30))
    arial_2 = pg.font.SysFont('arial', 15, True)
    pt_x = arial_2.render(f'Pontuacao X:{pon_X}', True, (255,255,255))
    pt_o = arial_2.render(f'Pontuacao O:{pon_o}', True, (255, 255, 255))
    tela.blit(pt_x, (8, 80))
    tela.blit(pt_o, (370,80))


def texto_v():
    arial = pg.font.SysFont('arial', 50)

    mens_vitoria = arial.render('DEU VELHA',True ,(0, 255, 0), 0)
    tela.blit(mens_vitoria, (100, 430))

while True:
    mouse_pos = pg.mouse.get_pos()

    for e in pg.event.get():
        # print(winner, vez)
        if e.type == QUIT:
            pg.quit()
            exit()
        if e.type == MOUSEBUTTONDOWN:
            # desenha()
            if tabuleiro.collidepoint(mouse_pos):
                desenha()
        if winner:
            if vez_a == '"X"':
                pon_X += 1
            else:
                pon_o += 1
            sleep(2.00)
            restart()
        else:
            if moves > 9:
                sleep(2.00)
                restart()
    winner = checa()
    draw_tabu()
    pg.display.flip()