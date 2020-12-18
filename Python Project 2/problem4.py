def capitalise(phrase):
    lowerWordList = ["a", "an", "the", "am", "is", "are", "and", "of", "in", "on", "with", "from", "to"]

    arr = ""
    #writeyourcodegoesfromheretoperformwordcapitalisation
    wordsList = phrase.split(" ")
#     print(wordsList)
    for word in wordsList:
        if word in lowerWordList: 
            w = word.lower()
            arr = arr + w + " "
        else:
            w = word[0: 1].upper()
            wl = word[1:].lower()
            arr = arr + w + wl + " "
    print(arr)

# Output: "I am an Educator and a Researcher"
capitalise("I am an educator and a researcher")

# Output: "Big Data is the Future of Information Technology"
capitalise("big data  is  the  future  of  information  technology")  

# Output: "He Wants to Have Breakfast with Her in the Hotel"
capitalise("He wants to have break fast with her in the hotel")