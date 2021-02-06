import pyttsx3  #get python text to speech engine


#conversation begins
friend = pyttsx3.init()
friend.say("Hello, My name is Banna! "
            "I am a computer. "
            "Can I be your Friend? "
            "What is Your Name?"
)
friend.runAndWait()

name = input("Name: ")

friend.say("Nice to meet you " + name)
friend.say("What do you do for fun?")
friend.runAndWait()

fun = input("--> ")

friend.say( fun) 
friend.say("That sounds cool, but I like to read!")
friend.say("Are you working?")
friend.runAndWait()

ans1 = input("Yes or No: ")
ans = ans1.lower()


while True:
    try:  #checking for error in response to "ans" variable
        if ans == 'yes':
            friend.say("What type of work do you do?")
            friend.runAndWait()
            work = input("Type of Work: ")
            friend.say(work)
            friend.say("Interesting")
            friend.say("Don't know much about that, but it sounds like fun")
            friend.runAndWait()
            break

        if ans == 'no':
            friend.say("I am sorry to hear that, hope you get a Job soon!")
            friend.runAndWait()
            break
    except:  #code pauses if executed(fix this***)
        if ans != 'yes' and ans != 'no':
            friend.say("Answer Yes or No please!")
            friend.runAndWait()

friend.say("How old are you?")
friend.runAndWait()

age = input("Age: ")

friend.say("Wow")
friend.say(age)
friend.say("I would have never guessed")
friend.say("Nice talking to you, " + name)
friend.say("I have to go now")
friend.say("See you soon!")
friend.runAndWait()
