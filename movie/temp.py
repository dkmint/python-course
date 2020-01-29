mylist = [["hello world", 1987, 2.87],
          ["welkom hewlen", "1234", 9.3]]

year = input("Enter year: ")
for slist in mylist:
    for i in slist:
        if i == year:
            print ("Yes")
            print(i)
        else:
            pass
