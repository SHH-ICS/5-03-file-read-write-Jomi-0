# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
  # opens the file to read - this file must already exist("")
question=("Input your question: ")
a=(input(" Question a: "))
b=(input(" Question b: "))
c=(input(" Question c: "))
d=(input(" Question d: "))

correctanswer=(input("Put in the right answer: "))
if correctanswer!= ("a","b","c" or "d"):
    print("Your correct answer must be a,b,c or d (letter only)")
else: print(correctanswer," is the correct answer")

# with ensures the file closes properly even if an error occurs
with open("questions.txt", 'a') as outFile:
    outFile.write(f"Question: {question}\n")
    outFile.write(f"a) {a}\n")
    outFile.write(f"b) {b}\n")
    outFile.write(f"c) {c}\n")
    outFile.write(f"d) {d}\n")
# reads the file contents into the string variable contents
inFile = open("questions.txt", 'r') #opens it first
contents = inFile.read()
# outputs the file contents
print (contents)
inFile.close()