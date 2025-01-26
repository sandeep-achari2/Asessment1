
def word_count(sentence):
    words= sentence.split()
    word_count={}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def main():
    sentence=input("Enter a sentence: ")
    word_counts=word_count(sentence)
    for word,count in word_counts.items():
        print(f'{word} : {count}')
    
main()