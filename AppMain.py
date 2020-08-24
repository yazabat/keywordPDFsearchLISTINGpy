import os
import PyPDF2


class ProcesarPDF():
    def __init__(self):
        pass

    def procesar(self, ruta, lista_frases):
        archivos_en_dir = os.listdir(ruta)

        for archivo in archivos_en_dir:
            ruta_archivo = ruta + archivo
            abre_pdf = open(ruta_archivo, 'rb')
            lector_pdf = PyPDF2.PdfFileReader(abre_pdf)
            num_paginas = lector_pdf.numPages
            print("El archivo {} tiene {} páginas.".format(archivo, num_paginas))
            for indice_pagina in range(num_paginas):
                pagina = lector_pdf.getPage(indice_pagina)
                contenido = pagina.extractText()

                resultado_existe, resultado_frase = self.comparar(contenido, lista_frases)
                if resultado_existe:
                    ruta_csv_resultados = ruta + 'resultados_proces.csv'
                    cabecera = 'ARCHIVO,PAGINA,FRASE'
                    if not os.path.isfile(ruta_csv_resultados):
                        with open(ruta_csv_resultados, 'w') as out:
                            out.write(cabecera + '\n')

                    with open(ruta_csv_resultados, 'a') as out:
                        registro = '{},{},{}'.format(archivo, indice_pagina, resultado_frase)
                        out.write(registro + '\n')

    def comparar(self, contenido, lista_frases):
        existe_frase = False
        frase_encontrada = ""
        for frase in lista_frases:
            if frase.lower() in contenido.lower():
                existe_frase = True
                frase_encontrada = frase
                break
        return  existe_frase, frase_encontrada





if __name__=='__main__':
    ruta_pdf = 'C:/Ruta_PDF/'
    lista_frases = [
        "keyword1",
        "keyword2",
        "keyword3"
    ]
    procesar = ProcesarPDF()
    procesar.procesar(ruta_pdf, lista_frases)