import requests
# https://dictionaryapi.dev/
def get_word_definitions(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def translate(word):
    definitions = get_word_definitions(word)
    
    if not definitions:
        return "No definitions found."
    
    translation = f"Definitions for '{word}':\n"
    for entry in definitions:
        translation += f"Word: {entry['word']}\n"
        if 'phonetic' in entry:
            translation += f"Phonetic: {entry['phonetic']}\n"
        if 'meanings' in entry:
            for meaning in entry['meanings']:
                if 'partOfSpeech' in meaning:
                    translation += f"Part of Speech: {meaning['partOfSpeech']}\n"
                if 'definitions' in meaning:
                    for definition in meaning['definitions']:
                        translation += f"Definition: {definition['definition']}\n"
                        if 'example' in definition:
                            translation += f"Example: {definition['example']}\n"
                        translation += "\n"
    
    return translation

if __name__ == "__main__":
    word_to_translate = input("Enter a word: ")
    translation_result = translate(word_to_translate)
    print(translation_result)



