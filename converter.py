def toPigLatin(word) :

    vowels = ["a", "e", "i", "o", "u"]
    consonant_cluster = ""

    if word[0] not in vowels :
        for letter in word[:2] :
            if letter not in vowels :
                consonant_cluster += letter
        translation = word[len(consonant_cluster):] + consonant_cluster + 'ay'
    else :
        translation = word + 'ay'

    return translation

#print(toPigLatin(input('Type your work: ')))