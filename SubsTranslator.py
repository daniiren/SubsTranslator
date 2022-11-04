from python_translator import Translator

print('\n')
print("****************************")
print("* Welcome to SubsTransator *")
print("****************************")

inputSrtPath = input("\nEnter input srt path : ")
inputLanguage = input("\nFrom which language : ")
outputLanguage = input("To wich language : ")

fin = open(inputSrtPath[1:-2], 'r+')
fout = open(outputLanguage + ".srt", 'w')
fin.write('\n')

counter = 0
finalSrt = ""
plainText = ""
translator = Translator()

for line in fin.readlines() :
	counter += 1
	if (line == '\n') :
		plainText = str(translator.translate(plainText, outputLanguage, inputLanguage))
		finalSrt += plainText + "\n\n"
		plainText = ""
		counter = 0
	elif (counter > 2) :
		plainText += line
	else :
		finalSrt += line

fout.write(finalSrt)
fin.close()
fout.close()
