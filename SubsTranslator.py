import os
import deepl
import srt

print("****************************")
print("* Welcome to SubsTransator *")
print("****************************")
print("\nCase sensitive! (accepted example : EL or el)")
print('''Supported Languages : 
    BG - Bulgarian
    CS - Czech
    DA - Danish
    DE - German
    EL - Greek
    EN - English
    ES - Spanish
    ET - Estonian
    FI - Finnish
    FR - French
    HU - Hungarian
    ID - Indonesian
    IT - Italian
    JA - Japanese
    LT - Lithuanian
    LV - Latvian
    NL - Dutch
    PL - Polish
    PT - Portuguese (all Portuguese varieties mixed)
    RO - Romanian
    RU - Russian
    SK - Slovak
    SL - Slovenian
    SV - Swedish
    TR - Turkish
    UK - Ukrainian
    ZH - Chinese
''')

inputSrtPath = input("Enter input srt path : ")[1:-2]
outputLanguage = input("\nTo wich language : ").upper()
srtName = os.path.basename(inputSrtPath)
fin = open(inputSrtPath, 'r+')
fout = open(srtName[:-4] + "_greek" + srtName[-4:], 'w')
translator = deepl.Translator("your deepl api key")
finalSrt = ""

print("Perfect! Please be patient while we are doing our magic!...")
for currentSrt in srt.parse(fin) :
	finalSrt += str(currentSrt.index) + '\n'
	finalSrt += str(currentSrt.start).replace('.', ',')[:-3] + " --> " + str(currentSrt.end).replace('.', ',')[:-3] +  '\n'
	finalSrt += translator.translate_text(currentSrt.content.replace('\n', ' '), target_lang = outputLanguage).text + '\n\n'
print("All ready! Enjoy the movie :)")

fout.write(finalSrt)
fin.close()
fout.close()
