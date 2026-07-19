#taking the input from the person till he/she enter done.
#also convert the text to lowercase.
sentence_list =[]
while True:
    collect = input("enter the sentence:")
    collection = collect.lower()
    if collection != "done":
        sentence_list.append(collection)
    elif collection == "done":
        if not sentence_list:
            print("you did not enter any thing")
        break

#removing punctuation from the text.
# using len so that if we change the item count in punctation code do not break.
singel_word = []
sentence_set = []
punctuation = ["!","@","#","$",",","?",".",":",";","'","-"]
for word_str in sentence_list:
        i = 0
        while i < len(punctuation):
         item = punctuation[i]
         word_str = word_str.replace(item,"")
         i += 1
        singel_word.extend(word_str.split())
        sentence_set.append(set(word_str.split()))

#increasing the count and counting the word or repeted word.

word_dic = {}
for word in singel_word:
    if word in word_dic:
        word_dic[word] += 1
    else:
        word_dic[word] = 1

#storing all unique word.


word_sat = set(singel_word)

#total no of word use in accourding to there lengeth.

word_len = {"short":0, "medium":0, "long":0}

for word in word_sat:   
    if len(word) < 4:
        word_len["short"] += 1
    elif len(word) <= 6:
        word_len["medium"] += 1
    else:
        word_len["long"] += 1
common_word = {}
if not sentence_list:
    pass
else:
    common_word = sentence_set[0]



for s in sentence_set:
    common_word = common_word.intersection(s)

most_u_word = ""
max_u_count = 0
for max_word,max_count in word_dic.items():
    if max_count >= max_u_count:
        most_u_word = max_word
        max_u_count = max_count



print("---summary report showing:---")
print("Total number of words entered:", len(singel_word))
print("Total number of unique words:",len(word_sat))
print("The most frequently used word:",most_u_word,"and its count:",max_u_count)
print("common words:", common_word)
print("count of short word:",word_len["short"])
print("count of medium word:",word_len["medium"])
print("count of larg word:",word_len["long"])