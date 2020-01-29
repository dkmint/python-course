print("The Test Score Program\n")
scores = []

counter = 0
score_total = 0
test_score = 0
choise = 'y'
mesage = "Enter 'ene' to end input"

while choise.lower() == 'y':
    print("Enter test scores")
    print(mesage)
    print('=' * len(mesage))
    while True:
        test = input("Enter test score: ")
        if test == 'end':
            break
        test_score = int(test)
        if test_score >= 0 and test_score <= 100:
            scores.append(test_score)
            counter += 1
        else:
            print("Test score must be from 0 through 100. Try again.")

    for score in scores:
        score_total += score

    average_score = round(score_total / counter)
    median_in = len(scores) // 2
    median = scores[median_in]
    minimum = min(scores)
    maximum = max(scores)
    print('=' * len(mesage))
    print("Total Score:      " + str(score_total))
    print("Number of scores: " + str(counter))
    print("Average Score:    " + str(average_score))
    print("Low score:        " + str(minimum))
    print("High score:       " + str(maximum))
    print("Median score:     " + str(median))

    choise = input("\nEnter another set of test scores (y/n)? ")
    print()
