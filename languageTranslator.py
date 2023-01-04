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
#  'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


def translator():
    from deep_translator import GoogleTranslator
    import glob
    import sys
    def translate(to_translate, targetlang = 'pt', sourcelang = 'auto'):
        translated = GoogleTranslator(source=sourcelang, target=targetlang).translate(to_translate)
        print(translated)

    def translate_frm_file(filepath, lang):
        translated = GoogleTranslator(source='english', target=lang).translate_file(filepath)
        print(translated)

    deployTranslator = True
    if deployTranslator:
        print("This is the name of the script:", sys.argv[0])
        sourcelang = input("Hi, which language you want to translate from: please select among: 'chinese (simplified)': 'zh-CN', 'japanese': 'ja', 'english': 'en' 'portuguese': 'pt','urdu': 'ur', 'hindi': 'hi':")
        print(sourcelang)
        targetlang = input("Which language you want to translate to: ")
        print(targetlang)
        texttotranslate = input("Please enter text you want to translate ")
        translate(texttotranslate, targetlang,sourcelang )
        if len(sys.argv) >=2:
            text_to_translate = sys.argv[1]
            lang = sys.argv[2]
            srtFilesPath = sys.argv[3]

            print("Number of arguments:", len(sys.argv))
            print("The arguments are:", str(sys.argv))
            translate(text_to_translate, lang)
            # translate_frm_file(srtFilesPath, 'pt')

    else:

        to_translate = 'Ohh this work is giving something to work with'
        translate(to_translate, 'urdu')
        filepath = '/Users/aasimkhurshid/Documents/Aasim/Datasets/SrtFiles/SrtFiles/351/5-5203.srt'
        filesPath = '/Users/aasimkhurshid/Documents/Aasim/Datasets/SrtFiles/SrtFiles/'
        # translate_frm_file(filepath, 'pt')
        print(f'{filepath}' '*/*.srt')
        srt_files_test = glob.glob(f'{filesPath}' '*/*.srt')
        print(srt_files_test)
        i=0
        for file_name in srt_files_test:

            #     Check whether file is in text format or not
            if(i>2):
                break
            i = i + 1
            if file_name.endswith(".srt"):
                file_encoding = 'iso-8859-1'
                translate_frm_file(file_name, 'pt')
                # with open(file_name, encoding=file_encoding, errors='replace') as f:
                #     lines = f.readlines()
                #     print(lines)