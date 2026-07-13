#taking the input from the person till he/she enter done
sentence_list =[]
while True:
    collect = input("enter the sentence:")
    collection = collect.lower()
    if collection != "done":
        sentence_list.append(collection)
    elif collection == "done":
        break

world_list = []
for word_str in sentence_list:
    world_list.extend(word_str.split())
print(world_list)
