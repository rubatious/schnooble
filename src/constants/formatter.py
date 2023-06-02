def get_words(filename):
    # Processes a file with words on each line and returns a list of lowercase words
    lines = open(filename, 'r').readlines()
    words = []
    seenwords = set()
    for line in lines:
        word = line.strip().lower()
        if word in seenwords or word == '' or not word.isalpha():
            continue
        else:
            words.append(word)
    return words

def export_words(words, header, outfile):
    # Export schnoob words
    outfile = open(outfile, 'w')
    outfile.write(header + '\n')
    for word in words:
        outfile.write(f"  \'{word}\',\n")
    outfile.write(']')

# Get schnoob words and extra words and write to constants files
words = get_words('schnoobwords.txt')
extras = get_words('allwords.txt')
export_words(words, 'export const WORDS = [', 'wordlist.ts')
export_words(words + extras, 'export const VALID_GUESSES = [', 'validGuesses.ts')
