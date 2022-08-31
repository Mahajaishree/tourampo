import pyttsx3
import datetime
import os
import shutil
from twilio.rest import Client
import win32com.client as wincl
from urllib.request import urlopen
import gtts as gt 
import os     
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
    else:
        speak("Good Evening Sir !") 
    assname =("Jarvis 1 point o")
    speak("Welcome to Meenakshi Amman Temple !!.I am your Tourist guide Assistant")
     # speak(assname)
def username():
    speak("How should i call you")
    # uname = take command()
    print("enter your name:")
    uname = input() 
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")
if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
def searchplaceseng():
    hnorthrajagorpuram = '•It is a Nine Tier Gopuram •Construction of this tower was started by Krishnaveerappa Naicker (1564 – 1572) and completed by the family of Amaravathi Pudur Vayinagaram Nagappa Chetti in 1878.'
    snorthrajagorpuram='•Gopuram remained unfinished for a number of years and was therefore called Mottai Gopuram meaning a tower without a roof.•This is 152 feet in height and the length of the base is 111.6 feet with a width of 66.6 feet.•This houses 404 carvings depicting mythological stories.'
    hHallofThousandPillars = '•This is the largest mandapam in the holy temple complex, this mandapam is situated near Veeravasantharayar Mandapam to the north.•This was built by Ariyanatha Mudaliyar, minister and commander of Viswanatha Naicker in the year 1569.'
    sHallofThousandPillars='•Mandapam has a total of 985 pillars and these pillars have been so arranged that from whatever angle one looks from within, the pillars look in rows.•At the centre of the mandapam is the idol of Chira Sabha of Lord Natarajar.•The pillars at the beginning and end of the row are big ones with small circular blocks and the one at the bottom could be rolled. These pillars are called musical pillars and they produce musical notes when tapped.'
    timings=('Maalai Pooja – 4:30 AM to 5:15 AM \nThiruvanandal Pooja – 5:00 AM to 6:00 AM\nVizha Pooja – 6:30 AM to 7:15 AM\nKalasandhi Pooja  6:30 AM to 7:15 AM\nThrukalasandhi pooja – 10:30 AM to 11:15 AM\nUchikkala Pooja (Noon Pooja) – 10:30 AM – 11:15 AM\nArdhajama Pooja (Night Pooja) – 7:30 PM – 8:15 PM\nPalliarai pooja – 9:30 PM – 10:00 PM')
    print('you can search any of the below places')
    print('1.North RajaGopuram')
    print('2.Hall of Thousand pillars')
    print('3.Aarathi Timings')
    search =int(input())
    if(search==1):  
        print('do you want North Rajagorpuram:       1.History                         2.Significance')
        b=int(input())
        if(b==1):
            print(hnorthrajagorpuram)
            speak(hnorthrajagorpuram)
        else:
            print(snorthrajagorpuram)
            speak(snorthrajagorpuram)
    if(search==2):
        print('do you want Hall of Thousand Pillars:       1.History                         2.Significance')
        b=int(input())
        if(b==1):
            print(hHallofThousandPillars)
            speak(hHallofThousandPillars)
        else:
            print(sHallofThousandPillars)
            speak(sHallofThousandPillars)
    if(search==3):
        print(timings)
        speak(timings)
    print('do you want to continue or not')
    choice=input()
    if(choice=='yes'):
        searchplaceseng()
    else:
        festivalseng()
def searchplacestam():
    hn = '•இது ஒன்பது அடுக்கு கோபுரம்•இந்த கோபுரத்தின் கட்டுமானம் கிருஷ்ணவீரப்ப நாயக்கரால் (1564 - 1572) தொடங்கப்பட்டு 1878 இல் அமராவதி புதூர் வயிநகரம் நாகப்ப செட்டியின் குடும்பத்தினரால் முடிக்கப்பட்டது.'
    sn = '•இந்த கோபுரம் பல ஆண்டுகளாக முடிக்கப்படாமல் இருந்ததால், கூரை இல்லாத கோபுரம் என்று பொருள்படும் மொட்டை கோபுரம் என்று அழைக்கப்பட்டது.\n•இது 152 அடி உயரம் மற்றும் அடிவாரத்தின் நீளம் 111.6 அடி மற்றும் அகலம் 66.6 அடி.\n•இதில் புராணக் கதைகளை சித்தரிக்கும் 404 சிற்பங்கள் உள்ளன.'
    hh = '•புனித கோவில் வளாகத்தில் உள்ள மிகப்பெரிய மண்டபம், இந்த மண்டபம் வடக்கே வீரவசந்தராயர் மண்டபத்திற்கு அருகில் அமைந்துள்ளது. \n•இது 1569 ஆம் ஆண்டு விஸ்வநாத நாயக்கரின் அமைச்சரும் தளபதியுமான அரியநாத முதலியார் என்பவரால் கட்டப்பட்டது.'
    sh = '•மண்டபத்தில் மொத்தம் 985 தூண்கள் உள்ளன. இந்தத் தூண்கள் எந்தக் கோணத்தில் இருந்து பார்த்தாலும், தூண்கள் வரிசையாகத் தெரியும்படி அமைக்கப்பட்டுள்ளன.\n•மண்டபத்தின் மையத்தில் நடராஜரின் சிரா சபை சிலை உள்ளது.\n•வரிசையின் தொடக்கத்திலும் முடிவிலும் உள்ள தூண்கள் சிறிய வட்டத் தொகுதிகளுடன் பெரியவை மற்றும் கீழே உள்ளதை உருட்டலாம். இந்த தூண்கள் இசைத் தூண்கள் என்று அழைக்கப்படுகின்றன, மேலும் அவை தட்டும்போது இசைக் குறிப்புகளை உருவாக்குகின்றன.'
    timings=('மாலை பூஜை – 4:30  - 5:15  \nதிருவனந்தாள் பூஜை – 5:00 - 6:00 \nவிழா பூஜை – 6:30  - 7:15 \nகாலசந்தி பூஜை  6:30  - 7:15 \nத்ருகாலசந்தி பூஜை – 10:30  -  11:15 \nஉச்சிகால பூஜை – 10:30  -  11:15 \nஅர்த்தஜாம பூஜை – 7:30  -  8:15 \nபள்ளியறை பூஜை – 9:30 -  10:00 ')
    print('you can search any of the below places')
    print('1.வடக்கு ராஜகோபுரம்')
    print('2.ஆயிரம் தூண்கள் மண்டபம்')
    print('3.ஆரத்தி நேரங்கள்')
    search =int(input())
    if(search==1):  
        print('do you want North Rajagorpuram:\n1.வரலாறு\n2.தனிமுறைச் சிறப்பு')
        b=int(input())
        if(b==1):
            tts = gt.gTTS(text=hn, lang='ta')
            print(hn)
            tts.save("Tamil-Audio.mp3")
            os.system("Tamil-Audio.mp3")
        else:
            tts = gt.gTTS(text=sn, lang='ta')
            print(sn)
            tts.save("Tamil-Audio.mp3")
            os.system("Tamil-Audio.mp3")
    if(search==2):
        print('do you want Hall of Thousand Pillars:\n1.வரலாறு\n2.தனிமுறைச் சிறப்பு')
        b=int(input())
        if(b==1):
            tts = gt.gTTS(text=hh, lang='ta')
            print(hh)
            tts.save("Tamil-Audio.mp3")
            os.system("Tamil-Audio.mp3")
        else:
            tts = gt.gTTS(text=sh, lang='ta')
            print(sh)
            tts.save("Tamil-Audio.mp3")
            os.system("Tamil-Audio.mp3")
    if(search==3):
            tts = gt.gTTS(text=timings, lang='ta')
            print(timings)
            tts.save("Tamil-Audio.mp3")
            os.system("Tamil-Audio.mp3")
    print('do you want to continue or not')
    choice=input()
    if(choice=='yes'):
        searchplacestam()
    else:
        festivalstam()
def festivalseng():
    chithirai='Chithirai Festival, also known as Chithirai Thiruvizha, Meenakshi Kalyanam or Meenakshi Thirukalyanam, is an annual Tamil Hindu celebration in the city of Madurai during the month of April. It is celebrated during the Tamil month of Chithirai.'
    vasantham='The spring festival is held for ten days and on the last day devotees make offerings of milk and mango to the deities. Lord Sundareswara and Meenakshi Amman are taken to the hall called New Mandapam and then taken out in procession. On the day of the Moola star there is a procession of the images of the sixty three Nayanar saints. '
    unjal='This is a ten day festival and on the last day the triple fruit puja is performed. The abhishekham ritual is performed to the images of Sivakami Amman and Arulmighu Nataraja on the day of Uthiram. The Nataraja image is then taken out in procession along the four Masi streets. '
    aadi='This ten day festival is reserved for the worship of Meenakshi Amman only. The image of the goddess is taken out in a procession along the Aadi streets. Also there are special music programmes with nadeswaram recitals.'
    aavani='The Aavani festival goes on for eighteen days. For six days the festival is devoted to the god Chandrashekhar and the next twelve days to the Panchamoorthi that are taken out in procession along the Aavani Moola streets. On the seventh day there is a coronation of Lord Sundareswarar and the miracles performed by the Lord of Madurai are enacted by the Sivachariars.'
    navarathri='The Navarathri is a grand ten day festival where the goddess appears in new garments to bless her devotees in the Kolu Mandapam. Kalpa puja and Lakshacharna are performed every day in the Amman sanctum. There are cultural performances and the temple is decorated with many coloured lights and arrangement of dolls '
    kolattam='The Kanda Sashti festival is celebrated for six days at the Koodal Kumarar Sannidhi. A durbar is held on Deepavali for the employees of the temple. On the days of Pooram the ceremony of the hoisting and swinging of Meenakshi Amman is performed.'
    print('*************FESTIVAL IN MEENAKSHI AMMAN TEMPLE********************')
    print('you can search any festival')
    print('1.Chithirai Festival')
    print('2.Vasantham Festival')
    print('3.Unjal Festival ')
    print('4.Aadi Mulai Kottu ')
    print('5.Aavani Moolam')
    print('6.Navarathri')
    print('7.kolattam')
    festival=int(input())
    if(festival==1):  
        print(chithirai)
        speak(chithirai)
    if(festival==2):  
        print(vasantham)
        speak(vasantham)
    if(festival==3):  
        print(unjal)
        speak(unjal)
    if(festival==4):  
        print(aadi)
        speak(aadi)
    if(festival==5):  
        print(aavani)
        speak(aavani)
    if(festival==6):  
        print(navarathri)
        speak(navarathri)
    if(festival==7):  
        print(kolattam)
        speak(kolattam)
    print('do you want to continue or not')
    choice=input()
    if(choice=='yes'):
        festivalseng()
    else:
        print('Thank you')
def festivalstam():   
    chithirai='சித்திரைத் திருவிழா, சித்திரைத் திருநாள், மீனாட்சி கல்யாணம் அல்லது மீனாட்சி திருக்கல்யாணம் என்றும் அழைக்கப்படும் சித்திரைத் திருவிழா, ஏப்ரல் மாதத்தில் மதுரை நகரத்தில் நடைபெறும் ஒரு வருடாந்திர தமிழ் இந்து விழாவாகும். இது தமிழ் மாதமான சித்திரை மாதத்தில் கொண்டாடப்படுகிறது.'
    vasantham='வசந்த திருவிழா பத்து நாட்கள் நடைபெறும், கடைசி நாளில் பக்தர்கள் தெய்வங்களுக்கு பால் மற்றும் மாம்பழம் காணிக்கை செலுத்துகின்றனர். சுந்தரேஸ்வரரையும், மீனாட்சி அம்மனையும் புதிய மண்டபம் என்று அழைக்கப்படும் மண்டபத்திற்கு அழைத்துச் சென்று ஊர்வலமாக எடுத்துச் செல்கின்றனர். மூல நட்சத்திரத்தன்று அறுபத்து மூன்று நாயனார்களின் திருவுருவச் சிலைகள் ஊர்வலமாகச் செல்கின்றன. '
    unjal='இது பத்து நாள் திருவிழாவாகும், கடைசி நாளில் மூன்று பழ பூஜை செய்யப்படுகிறது. உத்திரத்தன்று சிவகாமி அம்மன் மற்றும் அருள்மிகு நடராஜர் திருவுருவப் படங்களுக்கு அபிஷேக ஆராதனை செய்யப்படுகிறது. பின்னர் நடராஜர் சிலை நான்கு மாசி வீதிகளிலும் ஊர்வலமாக எடுத்துச் செல்லப்படுகிறது. '
    aadi='இந்த பத்து நாள் திருவிழா மீனாட்சி அம்மன் வழிபாட்டிற்கு மட்டுமே ஒதுக்கப்பட்டுள்ளது. தேவியின் உருவம் ஆடி வீதிகளில் ஊர்வலமாக எடுத்துச் செல்லப்படுகிறது. மேலும் நாதேஸ்வரம் பாராயணங்களுடன் கூடிய சிறப்பு இசை நிகழ்ச்சிகளும் உள்ளன.'
    aavani='ஆவணி திருவிழா பதினெட்டு நாட்கள் நடக்கிறது. ஆறு நாட்கள் திருவிழா சந்திரசேகரர் கடவுளுக்கும், அடுத்த பன்னிரண்டு நாட்கள் ஆவணி மூல வீதிகளில் ஊர்வலமாக எடுத்துச் செல்லப்படும் பஞ்சமூர்த்திக்கும் அர்ப்பணிக்கப்படுகிறது. ஏழாம் நாள் சுந்தரேஸ்வரருக்கு முடிசூட்டு விழாவும், மதுரைப் பெருமான் செய்த அற்புதங்கள் சிவாச்சாரியார்களால் நிகழ்த்தப்படுகின்றன.'
    navarathri='நவராத்திரி என்பது பத்து நாள் திருவிழாவாகும், அங்கு கொலு மண்டபத்தில் தேவி புதிய ஆடைகளில் தோன்றி பக்தர்களுக்கு அருள்பாலிக்கிறார். அம்மன் சன்னதியில் தினமும் கல்ப பூஜையும், லட்சார்ச்சனையும் நடைபெறுகின்றன. கலாச்சார நிகழ்ச்சிகள் உள்ளன, மேலும் கோயில் பல வண்ண விளக்குகள் மற்றும் பொம்மைகளின் ஏற்பாடு ஆகியவற்றால் அலங்கரிக்கப்பட்டுள்ளது '
    kolattam='கூடல் குமரர் சன்னிதியில் கந்த சஷ்டி விழா ஆறு நாட்கள் கொண்டாடப்படுகிறது. தீபாவளியன்று கோயில் ஊழியர்களுக்காக தர்பார் நடத்தப்படுகிறது. பூரம் தினத்தன்று மீனாட்சி அம்மனின் கொடியேற்றம் மற்றும் ஊஞ்சலாடும் வைபவம் நடைபெறுகிறது.'
    print('*************FESTIVAL IN MEENAKSHI AMMAN TEMPLE********************')
    print('you can search any festival')
    print('1.சித்திரை  திருவிழா')
    print('2. வசந்தம் திருவிழா')
    print('3. ஊஞ்சல் திருவிழா ')
    print('4.ஆடி திருவிழா ')
    print('5. ஆவணி  திருவிழா')
    print('6.நவராத்திரி திருவிழா')
    print('7.கோலாட்டம் திருவிழா')
    festival=int(input())
    if(festival==1):  
        tts = gt.gTTS(text=chithirai, lang='ta')
        print(chithirai)
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    if(festival==2):  
        tts = gt.gTTS(text= vasantham, lang='ta')
        print( vasantham)
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    if(festival==3):  
        tts = gt.gTTS(text= unjal, lang='ta')
        print( unjal)
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    if(festival==4):  
        tts = gt.gTTS(text=aadi, lang='ta')
        print(aadi)
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    if(festival==5):  
        tts = gt.gTTS(text= aavani, lang='ta')
        print( aavani)
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    if(festival==6):  
        tts = gt.gTTS(text=navarathri, lang='ta')
        print(navarathri)
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    if(festival==7):  
        tts = gt.gTTS(text=kolattam, lang='ta')
        print(kolattam)
        tts.save("Tamil-Audio.mp3")
        os.system("Tamil-Audio.mp3")
    print('do you want to continue or not')
    choice=input()
    if(choice=='yes'):
        festivalstam()
    else:
        print('Thank you')
    
def lang():
    print("choose language")
    print("1.English")
    print("2.Tamil")
    lang=int(input())
    if(lang==1):
        print("1.places")
        print("2.Festival")
        a=int(input())
        if(a==1):
            searchplaceseng()
        else:
            festivalseng()
    else:
        print("1.இடங்கள்")
        print("2.திருவிழா")
        a=int(input())
        if(a==1):
            searchplacestam()
        else:
            festivalstam()

print('WELCOME TO MEENAKSHI AMMAN TEMPLE')
lang()
print('do you want to continue to search places')
choice=input()
if(choice=='yes'):
    lang()
else:
    print('Thanks for visiting')
