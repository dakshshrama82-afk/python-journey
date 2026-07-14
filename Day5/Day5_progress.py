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
        word_dic[word] += 1
    else:
        word_dic[word] = 1
word_sat = {

}
word_sat = set(singel_word)


print("word frequency:",word_dic)
print("unique word:",word_sat)


word_len = {"short":0, "medium":0, "long":0}

for word in word_sat:   # loop through unique words
    if len(word) < 4:
        word_len["short"] += 1
    elif len(word) <= 6:
        word_len["medium"] += 1
    else:
        word_len["long"] += 1

print("Word length categories:", word_len)
