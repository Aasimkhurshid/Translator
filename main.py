import glob
import sys
from deep_translator import GoogleTranslator

import languageTranslator
def print_hi(name):
    # This function never executed.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Correct for the deployment version
def main():
    import os
    print('running main... ')

    # Threre are two modes, interactive would ask you which type of translation you want.
    translatorType = input('Type one of the folowing: 1 for if you want interactive input for files translation,  2 for text translation: ')
    textString = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
                  'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu',
                  'belarusian': 'be',
                  'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
                  'cebuano': 'ceb',
                  'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co',
                  'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl',
                  'english': 'en',
                  'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr',
                  'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn',
                  'gujarati': 'gu',
                  'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi',
                  'hmong': 'hmn',
                  'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id',
                  'irish': 'ga',
                  'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km',
                  'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku',
                  'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
                  'lingala': 'ln',
                  'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai',
                  'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr',
                  'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne',
                  'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa',
                  'polish': 'pl',
                  'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru',
                  'samoan': 'sm',
                  'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st',
                  'shona': 'sn',
                  'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
                  'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta',
                  'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr',
                  'turkmen': 'tk',
                  'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi',
                  'welsh': 'cy',
                  'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'
                  }
    deployinput = False
    deploarg = False
    deploytexttr = False
    if translatorType ==str(1):
        deployinput = True
    elif translatorType ==str(2):
        deploytexttr = True
    else:
        deploarg = True

    if deployinput:

        sourcelang = input(
            "Hi, which language you want to translate from: Please select on of the supported languages:" + str(textString))
        print(sourcelang)
        targetlang = input("Hi, which language you want to translate to: please select among: " + str(textString))
        print(targetlang)
        video_path = input('Enter the srt files folder path:')
        output_path = input('Enter the path for storing the output:')
        if not os.path.isdir(video_path):
            sys.exit("The specified <path_to_video_directory> argument is not a valid directory")

        if not os.path.isdir(output_path):
            sys.exit("The specified <output_path> argument is not a valid directory")
        video_path = video_path + '/'
        print(video_path)
        languageTranslator.translateFromFile(video_path, output_path, sourcelang, targetlang)
    elif deploarg:
        if len(sys.argv) < 3:
            sys.exit("Usage: %s <path_to_video_directory> <output_path>" % sys.argv[0])
        video_path = os.path.abspath(sys.argv[1])
        output_path = os.path.abspath(sys.argv[2])
        targetlang = sys.argv[3]
        if not os.path.isdir(video_path):
            sys.exit("The specified <path_to_video_directory> argument is not a valid directory")

        if not os.path.isdir(output_path):
            sys.exit("The specified <output_path> argument is not a valid directory")
        video_path = video_path + '/'
        print(video_path)
        languageTranslator.translateFromFile(video_path, output_path, targetlang)
    elif deploytexttr:
        languageTranslator.translateText()
    else:
        print('Please select the correct flag')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # This will call language translator function. This uses a package called deep translator.
    # Deep translator has multiple sub-packages, such as google package, deep AI and more.
    import sys

    print(f'#cli1# Arguments received are : {sys.argv[1:]}')
    # Call main if you want interactive translaton service
    # For quick test, give srt files address as: SRTFiles/SrtFiles
    # The results address: Results/ES_Results/
    main()
    # deployTranslator = False
    # if deployTranslator:
    #     languageTranslator.translateText()
    # else:
    #     filepath = '/Users/aasimkhurshid/Documents/Aasim/Datasets/SrtFiles/SrtFiles/351/5-5203.srt'
    #     filesPath = '/Users/aasimkhurshid/Documents/Aasim/Datasets/SrtFiles/SrtFiles/'
    #     outputPath = '/Users/aasimkhurshid/Documents/Aasim/Datasets/SrtFiles/Results/ES_Results/'
    #     targetlang = 'es'
    #     languageTranslator.translateFromFile(filesPath, outputPath, targetlang)
# add a comment

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
