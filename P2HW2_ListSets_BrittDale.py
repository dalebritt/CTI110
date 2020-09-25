# CTI-110
# P2HW2 - List and Sets
# Dale Britt
# 09/24/2020
#Initialize a list called test_scores
test_scores = []
#Input first test score from user, add to test_scores list
test_scores.append(int(input('Enter first test score: '))) 
#Input second test score from user, add to test_scores list
test_scores.append(int(input('Enter second test score: ')))
#Input third test score from user, add to test_scores list
test_scores.append(int(input('Enter third test score: '))) 
#Input fourth test score from user, add to test_scores list
test_scores.append(int(input('Enter fourth test score: ')))
#Input fifth test score from user, add to test_scores list
test_scores.append(int(input('Enter fifth test score: '))) 
#Input sixth test score from user, add to test_scores list
test_scores.append(int(input('Enter sixth test score: ')))
#Input seventh test score from user, add to test_scores list
test_scores.append(int(input('Enter seventh test score: '))) 
#Input eigth test score from user, add to test_scores list
test_scores.append(int(input('Enter eigth test score: ')))
#Input ninth test score from user, add to test_scores list
test_scores.append(int(input('Enter ninth test score: '))) 
#Input tenth test score from user, add to test_scores list
test_scores.append(int(input('Enter tenth test score: ')))

#Find lowest and highest test score, outputting to user
print('Lowest test score:', min(test_scores))
print('Higest test score:', max(test_scores))
#Find sum of all test scores, outputting to user
print('Sum of test scores:', sum(test_scores))
#Find average of all test scores, save as average_score
average_score = sum(test_scores) / 10
print('Average of test scores:', average_score)

#Convert test_scores list into set
test_scores_set = set(test_scores)
#Output new set to user
print('Set of unique test scores submitted:', test_scores_set)
