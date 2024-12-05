# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

correctanswer=(input("Put in the right answer: "))
if correctanswer!= ("a","b","c" or "d"):
    print("Your correct answer must be a,b,c or d (letter only)")
else: print(correctanswer," is the correct answer")

# reads the file contents into the string variable contents
inFile = open("questions.txt", 'r') #opens it first
contents = inFile.read()
correctcount=0
correctanswer=(input("What is your answer?: "))
if correctanswer not in ("a","b","c", "d"):
    print("Your answer must be a,b,c or d (letter only)")
else: 
    print(correctanswer," is the correct answer")
    correctcount+=1
    print("You have answered", correctcount," correctly!")
