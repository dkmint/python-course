print("The Test Score Program\n")

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
            score_total += test_score
            counter += 1
        else:
            print("Test score must be from 0 through 100. Try again.")

    average_score = round(score_total / counter)
    print('=' * len(mesage))
    print("Total Score: " + str(score_total)
        + "\nAverage Score: " + str(average_score))

    choise = input("\nEnter another set of test scores (y/n)? ")
    print()
