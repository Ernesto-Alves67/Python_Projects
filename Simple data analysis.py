# 1b = 0.000000957 mb
# dado = x mb
texto = 'alexandre       456123789 anderson        1245698456 antonio         123456456 carlos          91257581 cesar           987458' \
        ' rosemary        789456125 '




# for linha in texto:
#     lin_new += linha
#     if (len(lin_new) >= 25 and linha == ' ') or (len(lin_new) >= 22 and linha == ' '):
#         file.write(f'{lin_new} \n')
#         lin_new = ''
#         continue


biteMB= (9.537*0.0000001)
def convbtomb(dado):
    mb = biteMB*dado
    return mb

def ext(linha):
    dado = linha[16:26]
    user = linha[:9]
    return dado, user

def percent(valor):
    cent = (valor/2581.65)*100
    return cent
#dado = input("entre com os dados: ")
total = 0.0
id = 1
with open('dados.txt', 'r') as file:
    for linha in file:
        dados = ext(linha)
        convertido = convbtomb(int(dados[0]))
        cento = percent(convertido)
        file2 = open('relatorio.txt', 'a+')
        file2.write(f'{id}    {dados[1]}       {convertido:.2f} MB             {cento:.2f} p/100\n')
        total += convertido
        id += 1
    medi = total/6
    file2.write('\n')
    file2.write(f'Total Ocupado: {total:.2f} MB\n')
    file2.write(f'Media do espaco ocupado: {medi:.2f} MB')
    file2.close()
    print(f'o total: {total:.2f}MB')