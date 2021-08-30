class Translator():
    def __init__(self):
        self.morse_dictionary = {
            "a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..",
            "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.",
            "s":"...", "t":"-", "u":"..-", "v":"...-", "x":"-..-", "y":"-.--", "z":"--..", "w":".--", "1":".----",
            "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.",
            "0":"----",
        }
    def translate_morse_to_words(self, phrase):
            try:
                a = self.morse_dictionary[phrase.split()[0][0].lower()]
                words_list = phrase.split()
                translated_phrase = ""
                for word in words_list:
                    translated_word = ""
                    for letter in word:
                        try:
                            translated_word = translated_word + self.morse_dictionary[letter.lower()] + " "
                        except KeyError:
                            return "Please only use letters and digits"
                    translated_phrase = translated_phrase + translated_word + "/"
                return translated_phrase
            except KeyError:
                words_list = phrase.split("/")
                translated_phrase = ""
                for word in words_list:
                    translated_word = ""
                    for letter in word.split():
                        translated_word = translated_word + list(self.morse_dictionary.keys())[list(self.morse_dictionary.values()).index(letter)]
                    translated_phrase = translated_phrase + translated_word + " "
                return translated_phrase
translator = Translator()

word = input("Welcome to morse code translator."
             " Be sure to only use letter and digits for this translator to work. Type your phrase here: ")
print(translator.translate_morse_to_words(word))