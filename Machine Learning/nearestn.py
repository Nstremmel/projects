import pandas as pd
import random
#import RNG as random


# average = 0
# for x in range(500):
df = pd.read_csv("C:\\Users\\Andy\\Documents\\Sublime\\Machine Learning\\breast-cancer-data.csv")

#Default k is 3
def k_nearest_neighbors(data, predict, k=5):
	distances = []
	for group in data:
		for features in data[group]:
			sums = 0
			new_vector = [features - predict for features, predict in zip(features, predict)]
			for i, value in enumerate(new_vector):
				sums+=value*value
			euclidean_distance = (sums)**.5
			distances.append([euclidean_distance, group])
 
#IMPORTANT: K is the number of plotted points you analize to find the most common value out of those points.
#ALSO IMPORTANT: K must be odd
	votes = [i[1] for i in sorted(distances)[:k]]
	if votes.count(2)>votes.count(4):
		vote_result = 2
	else:
		vote_result = 4
	return vote_result



#for each "feature" in data[each vector in test_set[each vector in test_set]]

#shuffeling
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
full_data = df.astype(int).values.tolist()

# for i in range(699):
# 	randint = random.main(1,700)




random.shuffle(full_data)






# Spliting into training and test set
test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

for i in train_data:
	train_set[i[-1]].append(i[:-1])
for i in test_data:
	test_set[i[-1]].append(i[:-1])

#setting variables
correct = 0
total = 0

# lots of for loops for the calculations - calls nearest_neighbors function
for group in test_set:
	for data in test_set[group]:
		vote = k_nearest_neighbors(train_set, data, k=5)

#Checks if the guessed group was correct, and if correct it gives itself a point to find accuracy
		#print("The computer guessed ",str(vote))
		#print("The real answer was ",str(group))
		#print("")
		if group == vote:
			correct +=1
		total +=1
 


accuracy = float(correct) / float(total)
print("Accuracy: ",str(accuracy))
# 	print(str(x)," Accuracy: ",str(accuracy))
# 	average+=accuracy
# print("The average accuracy is "+str(average/(x+1))+".")