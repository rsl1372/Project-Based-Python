
#practice 1 of Problem Set 2
def Sentence_maker(arr):
    Sentences = ''
    for item in arr:
        Sentences += item + " " 
    return Sentences

arr= ['Hi', 'world', 'this', 'is', 'great']
Sentence_maker(arr)


#practice 2 of Problem Set 2
def repeat(r, word):
    sentences= ""
    for i in range(r):
        sentences += word
    return sentences

repeat(6, "hello")


