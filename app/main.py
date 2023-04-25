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


    # read path to image as command argument
    translatorType = input('Type one of the folowing: 1 for if you want interactive input for files translation,  2 for text translation: ')
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
            "Hi, which language you want to translate from: please select among: 'chinese (simplified)': 'zh-CN', 'japanese': 'ja', 'english': 'en' 'portuguese': 'pt','urdu': 'ur', 'hindi': 'hi':")
        print(sourcelang)
        targetlang = input("Hi, which language you want to translate to: please select among: 'chinese (simplified)': 'zh-CN', 'japanese': 'ja', 'english': 'en' 'portuguese': 'pt','urdu': 'ur', 'hindi': 'hi':")
        print(targetlang)
        video_path = input('Enter the srt files folder path:')
        output_path = input('Enter the path for storing the output:')
        if not os.path.isdir(video_path):
            sys.exit("The specified <path_to_video_directory> argument is not a valid directory")

        if not os.path.isdir(output_path):
            sys.exit("The specified <output_path> argument is not a valid directory")
        video_path = video_path + '/'
        print(video_path)
        languageTranslator.translateFromFile(video_path, output_path, targetlang)
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # This will call language translator function. This uses a package called deep translator.
    # Deep translator has multiple sub-packages, such as google package,
    import sys

    print(f'#cli1# Arguments received are : {sys.argv[1:]}')
    main()
    # deployTranslator = False
    # if deployTranslator:
    #     languageTranslator.translateText()
    # else:
    #     filepath = '/Users/aasimkhurshid/Documents/Aasim/Datasets/SrtFiles/SrtFiles/351/5-5203.srt'
    #     filesPath = '/Users/aasimkhurshid/Documents/Aasim/Datasets/SrtFiles/SrtFiles/'
    #     outputPath = '/Users/aasimkhurshid/Documents/Aasim/Datasets/SrtFiles/Results/'
    #     targetlang = 'pt'
    #     languageTranslator.translateFromFile(filesPath, outputPath, targetlang)
# add a comment

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
