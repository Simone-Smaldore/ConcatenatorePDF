from PyPDF2 import PdfFileMerger
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def schermo_iniziale():
	print(' ____________________________________')
	print('|        CONCATENATORE VIDEO         |')
	print('|____________________________________|')
	print('|1. Aggiungi nuovo pdf               |')
	print('|2. Concatena                        |')	
	print('|0. Esci                             |')
	print('|____________________________________|')


def converti(pdfs):
	merger = PdfFileMerger()

	for pdf in pdfs:
	    merger.append(pdf)

	nome_file = input("Inserisci nome file di destinazione:")

	merger.write(nome_file + '.pdf')
	merger.close()

def main():
	pdfs = []
	while(True):
		schermo_iniziale()
		try:
			scelta = int(input())

			if(scelta == 0):
				break
			if(scelta == 1):
				Tk().withdraw() 
				filename = askopenfilename() 
				print(filename)  
				pdfs.append(filename)
			if(scelta == 2 and len(pdfs) >= 2):
				converti(pdfs)
				break
			if(scelta == 2 and len(pdfs) < 2):
				print(' ____________________________________')
				print('|   INSERIRE PRIMA ALMENO DUE PDF    |')
				print('|____________________________________|')						
		except:
			print(' ____________________________________')
			print('|***ERRORE INSERIRE VALORE VALIDO*** |')
			print('|____________________________________|')

main()



