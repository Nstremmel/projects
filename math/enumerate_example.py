from collections import Counter

f = open("sonnet_18.txt")
sonnet_lines = [x.strip() for x in f.readlines()]
sonnet_words = []
for line in sonnet_lines:
	for word in line.split(" "):
		sonnet_words.append(word)
f.close()

print(Counter(sonnet_words).most_common(3))





# my_list = ["I", "love", "Taylor"]
# for i, word in enumerate(my_list):
# 	print("Value in my_list at index {} is {}.".format(i, word))

