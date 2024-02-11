# import gtts
import pyttsx3
from googletrans import Translator

"""with open("myfile.txt",mode="r") as myNewFile4:
    myContent = myNewFile4.read()"""

def ceviri():
    sentence = input("Çevirmek istediğiniz metini veriniz: ")
    translator = Translator()
    if sentence != "":
        example = translator.translate(sentence)
        return example.text
    else:
        example = ""
        return example

def ses():
    global x
    x = ceviri()
    engine = pyttsx3.init()
    engine.say(x)
    engine.setProperty("rate", 70)
    engine.setProperty("volume", 0.9)
    engine.runAndWait()



"""
def ses_file():
    audio = gtts.gTTS(text=example.text, lang="tr", slow=False)
    audio.save("test.mp3")
    os.system("start test.mp3")
    """


while True:
    ses()
    if x == "":
        break
    elif x != "":
        ses()





