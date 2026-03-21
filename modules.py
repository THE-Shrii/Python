# =========================================================
# 📦 MODULE + PIP DEMO (PYJOKES + PYTTSX3)
# =========================================================

# Step 0:
# Install required modules:
# pip install pyjokes pyttsx3


# ---------------------------------------------------------
# Step 1: Import modules
# ---------------------------------------------------------
import pyjokes     # for jokes
import pyttsx3     # for text-to-speech


# ---------------------------------------------------------
# Step 2: Initialize text-to-speech engine
# ---------------------------------------------------------
engine = pyttsx3.init()


# ---------------------------------------------------------
# Step 3: Get and print joke
# ---------------------------------------------------------
joke = pyjokes.get_joke()

print("😂 Random Joke:")
print(joke)

# Speak the joke
engine.say("Here is a joke for you")
engine.say(joke)


# ---------------------------------------------------------
# Step 4: Another joke with parameters
# ---------------------------------------------------------
joke2 = pyjokes.get_joke(language='en', category='neutral')

print("\n😂 Another Joke:")
print(joke2)

engine.say("Here is another joke")
engine.say(joke2)


# ---------------------------------------------------------
# Step 5: Multiple jokes
# ---------------------------------------------------------
jokes_list = pyjokes.get_jokes()

print("\n😂 Multiple Jokes:")
for j in jokes_list[:3]:
    print("-", j)
    engine.say(j)


# ---------------------------------------------------------
# Step 6: Run speech engine
# ---------------------------------------------------------
engine.runAndWait()


# =========================================================
# 🎯 END
# =========================================================