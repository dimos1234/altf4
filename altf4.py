import time
import os

# TEXT EDITOR
print("Write your program under. Ctrl-D or Ctrl-Z (windows) then 'Enter' to save and run.\nNOTE: altf4 only has 2 integer variable slots called VAR1 and VAR2, as well a print funcitonto print the 2 variables")
program = []
while True:
	try:
		line = input()
	except EOFError:
		break
	program.append(line)

# THE COMPILER
print("=============================================")
print("COMPILING")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")

def clean():
	# For Windows
	if os.name == "nt":
		_=os.system("cls")

	# For MAC and Linux
	else:
		_=os.system("clear")

clean()

# KEYWORDS
keyWords = ["print", "if", "while", "=", ".", "!"]
VAR1 = ""
VAR2 = ""

# counts the line number
lineCount = 0
for line in program:
	lineCount += 1

	# Checks for empty lines
	if line == "":
		continue

	# PRINT STATEMENT
	if (line.split()[0] == "print"):
		inString = False
		phrase = []
		for word in line.split():
			if word == "VAR1":
				phrase.append(str(VAR1))
				inString = True
				break
			if word == "VAR2":
				phrase.append(str(VAR2))
				inString = True
				break
			if word[0] == '"':
				inString = True
			if inString:
				for charI in range(len(word)):

					# Takes out the quotation
					if word[charI] == '"':
						continue

					# Add exceptions like \n, \t, \\, and so on...
					if word[charI] == "\\":
						pass
					phrase.append(word[charI])
				phrase.append(" ")

		# In case no input after print
		if not inString:
			raise Exception('in line ' + str(lineCount) + ': please enter a string surrounded by quotes after print statement')

		print("".join(phrase))
		continue

	# VARIABLES
	if (line.split()[0] == "VAR1"):
		if (line.split()[1] == "="):
			try:
				VAR1 = int(line.split()[2])
			except ValueError:
				raise Exception('in line ' + str(lineCount) + ': cannot convert VAR1 to int')

	elif (line.split()[0] == "VAR2"):
		if (line.split()[1] == "="):
			try:
				VAR2 = int(line.split()[2])
			except ValueError:
				raise Exception('in line ' + str(lineCount) + ': cannot convert VAR2 to int')
	else:
		raise Exception('in line ' + str(lineCount) + ': unknown identifier')