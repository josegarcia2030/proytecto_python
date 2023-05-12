#Concatenar cadena de caracteres.
#Supongamos que queremos crear una cadena que diga:
#Aprende a programar con ______________________:


def historia_loca():

    texto = 'Programar es tan (adjetivo).\n' + \
            'Siempre me emociono porque me encanta (verbo1) problemas.\n' + \
            '¡Aprende a (verbo2) con freeCodeCamp y alcanza tus (sustantivo)\n'

    def problema_juego():
        print('El juego consiste en poder rellenar los espacios en blancos')
        print('===========================================================')

    def mostrar_texto(text):
        print(text)

    def adjetivo():
        adjetivo = input('Escribe Adjetivo: ')
        return adjetivo

    def verbo():
        verbo = input('Escribe un Verbo: ')
        return verbo

    def sustantivo():
        sustantivo = input('Escribe un sustantivo: ')
        return sustantivo

    #
    problema_juego()
    mostrar_texto(texto)

    
    adj = adjetivo()
    verbo_1 = verbo()
    verbo_2 = verbo()
    sustant = sustantivo()
    
    def rellenar_texto():
        texto_adjetivo = texto.replace('(adjetivo)', adj)
        texto_verbo1 = texto_adjetivo.replace('(verbo1)', verbo_1)
        texto_verbo2 = texto_verbo1.replace('(verbo2)', verbo_2)
        texto_cambiado = texto_verbo2.replace('(sustantivo)', sustant)
        print(f'\n{texto_cambiado}')


    rellenar_texto()



historia_loca()












