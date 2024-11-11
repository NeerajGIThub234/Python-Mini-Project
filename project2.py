# open -> allow us to open any file!! "r" -> read mode !! f-> variable to use this file
with open("story.txt","r") as f:
    story = f.read()  # get data of story.txt in story variable

words = set() #set  to store all the abjectives and remove duplicates 
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story): #enumerate give us access to the position as well the element at that position
    if char == target_start: # to find the <
        start_of_word = i 
    
    if char == target_end and start_of_word != -1:  # match the > and <
        word = story[start_of_word : i+1]           # give adjective from < to >
        words.add(word)   # put the adjective into set
        start_of_word = -1  # to start search for next adjectives

answers = {}  #Dict to access sets element in key value pair

# to replace <adjative> from user words
for word in words:
    answer = input("Enter a word for "+ word + ": ")
    answers[word] = answer  # it give us dict like {<place2>': 'Kota', '<place>': 'Jaipur', .....}

# to replace word in story
for word in words:
    story = story.replace(word, answers[word]) #generate a string 

print(story)
