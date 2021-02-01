def run():
    horas = 24
    minutos = 59
    segundos = 59

    while horas >= 0:
        while minutos >= 0:
            while segundos >= 0:
                print(f'{horas}: {minutos} : {segundos}')
                segundos-=1
            minutos-=1
            segundos = 59
        horas-=1
        minutos = 59
        



if __name__ == '__main__':
    run() ##D. Gatica