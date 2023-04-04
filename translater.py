from deep_translator import GoogleTranslator
import sys

# Get arguments:
args = sys.argv

def check_arguments(args):
    options = ['--file', '--lang', '--help']

    if '--help' in args:
        print(f"\nUsage: \n\tpython3 {args[0]} --file <file> --lang <language>\n")
        sys.exit()

    elif '--file' in args and '--lang' in args:
        # Index of arguments:
        file_index = args.index('--file')
        lang_index = args.index('--lang')
        # Check if arguments are valid:
        file = args[file_index + 1]
        lang = args[lang_index + 1]
    
    return(file, lang)


def translate(file, lang):
    try:
        # Read JSON file:
        with open(file, 'r') as content:
            text = content.read()

        # Translate:
        translate = GoogleTranslator(source='auto', target=lang).translate(text)

        print(f"\n\n{translate}")
    except:
        print(f"\nUsage: \n\tpython3 {args[0]} --file <file> --lang <language>\n")



if __name__ == '__main__':
    file, lang = check_arguments(args)
    translate(file, lang)

# Usage:
#           https://pypi.org/project/deep-translator/
#           pip install deep-translator