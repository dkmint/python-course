counter = 0
score_total = 0
test_score = [0, 0, 0]

welcome = "Enter 3 test scores" 
print(welcome)
print("=" * (len(welcome) + 3)) 
while counter < 3:
    test_score[counter] = int(input("Enter test score: "))
    if test_score[counter] >= 0 and test_score[counter] <= 100:
        score_total += test_score[counter]
        counter += 1


average_score = round(score_total / counter)

print("=" * (len(welcome) + 3)) 
print("Your Score:\t", end="")

for i in range(3):
    print(test_score[i], " ", end="")


print("\nTotal Score:\t" + str(score_total)
    + "\nAverage Score:\t" + str(average_score))
