# Source: https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5
# pip install deep-translator
import deep_translator

# Please select on of the supported languages:
# {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
#  'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be',
#  'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb',
#  'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co',
#  'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en',
#  'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr',
#  'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu',
#  'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn',
#  'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga',
#  'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km',
#  'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku',
#  'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln',
#  'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai',
#  'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr',
#  'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne',
#  'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl',
#  'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm',
#  'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
#  'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
#  'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta',
#  'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk',
#  'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy',
#  'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', done}


import glob
import sys
from deep_translator import GoogleTranslator
# Translator class has the logic of translation from file and text.

class translator():


    def translate(to_translate, targetlang = 'pt', sourcelang = 'auto'):
        translated = GoogleTranslator(source=sourcelang, target=targetlang).translate(to_translate)
        print(translated)

    def translate_frm_file(filepath, targetlang, sourcelang):
        translated = GoogleTranslator(source=sourcelang, target=targetlang).translate_file(filepath)
        print(translated)
        return translated

# translateText function handles the translation of hard quoted text into the language of choice.
def translateText():
    print("This is the name of the script:", sys.argv[0])
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
    sourcelang = input("Hi, which language you want to translate from: please select among: " + str(textString))
    print(sourcelang)
    targetlang = input("Which language you want to translate to: " + str(textString))
    print(targetlang)
    texttotranslate = input("Please enter text you want to translate ")
    translator.translate(texttotranslate, targetlang,sourcelang )
    if len(sys.argv) >=2:
        text_to_translate = sys.argv[1]
        lang = sys.argv[2]
        srtFilesPath = sys.argv[3]

        print("Number of arguments:", len(sys.argv))
        print("The arguments are:", str(sys.argv))
        translator.translate(text_to_translate, lang)
        # translate_frm_file(srtFilesPath, 'pt')
# translateFromFile function handles the translation of srt files into the language of choice and stores result in the Results directory.
def translateFromFile(filesPath, outputPath, sourcelang, targetlang):

    to_translate = 'Ohh this work is giving something to work with'
    translator.translate(to_translate, targetlang, sourcelang)

    # translate_frm_file(filepath, 'pt')
    print(f'{filesPath}' '*/*.srt')
    srt_files_test = glob.glob(f'{filesPath}' '*/*.srt')
    print(srt_files_test)
    i=0
    for file_name in srt_files_test:

        #     Check whether file is in srt format or not
        # If you want to run few translation files, uncomment this.
        # if(i>10):
        #     break
        # i = i + 1
        if file_name.endswith(".srt"):
            file_encoding = 'iso-8859-1'
            tanslated = translator.translate_frm_file(file_name, targetlang, sourcelang)

            fnamesplit = file_name.split('/')
            print(fnamesplit)
            fname = targetlang+'_'+fnamesplit[-1]
            foldername = fnamesplit[-2]
            print('FOLDER NAME:::', foldername)
            import os
            print('Output folder name:::', os.path.join(outputPath,foldername))
            try:
                # if not os.path.exists(os.path.dirname(os.path.join(outputPath,foldername))):
                os.mkdir(os.path.join(outputPath,foldername))
            except:
                pass


            result_path = os.path.join(outputPath,foldername)
            fname = os.path.join(result_path,fname)
            print('Result path::',fname)
            f = open(fname, 'a')
            f.write(tanslated)
            f.close()
            # with open(file_name, encoding=file_encoding, errors='replace') as f:
            #     lines = f.readlines()
            #     print(lines)