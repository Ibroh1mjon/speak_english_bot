import requests

def getDefinition(word_id):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word_id
    r = requests.get(url)
    res = r.json()

    if isinstance(res, list) and len(res) > 0:
        output = {}
        meanings = res[0].get('meanings', [])

        if meanings:
            definitions = []
            for sense in meanings:
                definition = sense.get('definitions', [])
                if definition:
                    definitions.append(f"👉{definition[0]}")
            output['definition'] = "\n".join(definitions)

        phonetics = res[0].get('phonetics', [])

        if phonetics:
            musics = []
            for mp3 in phonetics:
                music = mp3.get('audio')
                if music:
                    musics.append(mp3)
            output['audio'] = musics
        # phonetics = res[0].get('phonetics', [])

        return output

    return False

if __name__ == '__main__':
    from pprint import pprint as print
    print(getDefinition("hello"))
