# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()

def count_words():
    sentences = ''.join(read_from_file("en_resa_genom_svenska_skogen.txt"))
    sentences.replace('\n',' ')
    sentences=sentences.split()
    word_count=len(sentences) 
    print(word_count)

def most_frequent():
    sentences = ''.join(read_from_file("en_resa_genom_svenska_skogen.txt"))
    sentences.replace('\n',' ')
    sentences=sentences.lower()
    sentences=sentences.split()
    dict={}
    for word in sentences:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    most_freq=max(dict,key=dict.get)
    print(most_freq)

def avg_len():
    sentences = ''.join(read_from_file("en_resa_genom_svenska_skogen.txt"))
    sentences=sentences.replace('\n',' ')
    sentences=sentences.lower()
    sentences2=sentences
    sentences=sentences.replace(' ','')    
    sentences2=sentences2.split()
    avg=len(sentences)/len(sentences2)
    print(avg)

def main():
    
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt") # Här har du nu en lista av strängar från den inlästa filen.

if __name__ == "__main__":
    avg_len()