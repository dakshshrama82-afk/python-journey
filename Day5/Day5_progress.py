#taking the input from the person till he/she enter done
sentence_list =[]
while True:
    collect = input("enter the sentence:")
    collection = collect.lower()
    if collection != "done":
        sentence_list.append(collection)
    elif collection == "done":
        break

singel_word = []
punctuation = ["!","@","#","$",",","?","."]
for word_str in sentence_list:
        i = 0
        while i < len(punctuation):
         item = punctuation[i]
         word_str = word_str.replace(item,"")
         i += 1
        singel_word.extend(word_str.split())

word_dic = {}
for word in singel_word:
    if word in word_dic:
        