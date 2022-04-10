import discord
import time
from random import randint
import logging
from termcolor import colored
# was der bot kann:
# dir hilfe anbieten = !help und !help1, !help2, !help3
# das instagram profil anzeigen
# dir zurück schreiben
# !info = gibt infos über denn Server
# !vote = startet eine Abstimmung
# !gameset = setz das Spiel, !game? = zeigt das aktuelle Game

# 1. wir verbessern den Code
# 2. logging weiter ausführen
# 3. kommentieren


################'!!!!!!!!!!!!!!!!!!!!!!!! alle x.ctime in ctime() ändern###
logging.basicConfig(
    filename = "BotClock.log",
    level = logging.DEBUG,
    style = "{",
    format = "{asctime} [{levelname:8}] {message}")
    
class MyClient(discord.Client):
    #Einloggen
    
    async def on_ready(self):
        print("~Bot aktiviert~")
        logging.info(" Bot was activated")
    async def on_message(self, message, when):# wenn Nachricht gepostet wird , zählt auch bei Privaten Nachrichten
        if message.author == client.user:
            return


        elif message.content.startswith("Hallo Bot"):# 1 bot wird kontaktiert
            await message.channel.send("Hallo ")
            await message.author.send("Du hast mich kontaktiert, was gibts?", delete_after=60.1)
            logging.info(str(message.author) + " ~hat denn Bot angefragt~" + str(when))
            print("Server Clock geschrieben")

        elif message.content.startswith("!insta"):# wird alles im Chat angezeigt 
            print("!insta wurde abgefragt" + str(when))# Usr gibt !insta
            # -> bot sendet Voreingestellten Instagram Account 
            await message.channel.send("Es gibt noch kein voreingestellten Instagram Account")
            logging.info(message.author + " hat !insta")
            print("Server Clock geschrieben")

        elif message.content.startswith("!help"):
            print("!help wurde abgefragt" + str(when))
            await message.channel.send("Hallo Bot = der Bot schreibt zurück")
            await message.channel.send("!insta = zeigt das Instagram Profil von Matti an")
            await message.channel.send("!info = zeigt Infos an")
            await message.channel.send("!vote = startet eine Umfrage")
            await message.channel.send("!wichtig = Pinnt deine Nachricht für 20 sec an (nur für Mods verfügbar)")
            await message.channel.send("!gameset = Setzt das aktuelle Spiel")
            await message.channel.send("!game? = zeigt das aktuelle Spiel an")
            await message.channel.send("!rules = zeigt die Regeln des Servers an")
            await message.channel.send("!feedback = schreibt dem Entwickler deine Kritik")
            await message.channel.send("!users = zeigt dir die Members an die online sind")
            await message.channel.send("!time = zeigt die aktuelle Zeit an (wer hätte es gedacht)")
            await message.channel.send("!emoji = zeigt dir ein Paar Emojis an")
            await message.channel.send("!happyhype = der Bot wünscht dir Alles Gute zum Geburtstag")
            await message.channel.send("!develop = ich bin ja nicht aus dem Boden gewachsen")
            
            logging.info(message.author + " !help")
            
            print("Server Clock geschrieben")

        elif message.content.startswith("!info"):
               await message.channel.send("Es wurden noch keine Infos vom Server hinterlegt")
    
        elif message.content.startswith("!vote "):
            print("!vote wurde abgefragt" + str(when))
            await message.pin()
            await message.channel.send("Eine Abstimmung hat gestartet, wenn du dafür bist , reagiere mit einem Daumen Hoch Emoji wenn du dafür bist wenn du dagegen bist mit einem Daumen runter.")
            time.sleep(20)
            await message.unpin()
            logging.info("[!vote]", message.author, str(when))

        elif message.content.startswith("!wichtig "):

            print("!wichtig wurde abgefragt" + str(when))
            await message.pin()
            await message.channel.send("Eine wichtige Nachricht wurde angepinnt")
            time.sleep(20)
            await message.unpin()
            logging.info("[!wichtig", message.author, str(when))

        elif message.content.startswith("!gameset "):
            print("!gameset wurde abgefragt" + str(when))
            game = message.content.split(' ')[1]
            print("Das aktuelle  Spiel wurde auf " + game + " gesetzt")
            await message.channel.send("Das aktuelle Spiel wurde auf " + game + " gesetz")
            logging.info("[!gameset]", message.author, str(when))
            logging.info("[!gameset]", "Current Game = ", game)
            

        elif message.content.startswith("!game?"):
            print("!game? wurde abgefragt" + str(when))
            print("Das aktuelle Spiel wurde abgefragt")
            await message.author.send("Das aktuelle Spiel ist " + game)
            logging.info("[!game?]", message.author, str(when))

        elif message.content.startswith("!rules"):
            RULES = ""# hier reinschreiben welche Regeln es gibt
            print("!rules wurde abgefragt" + str(when))
            await message.author.send(RULES)                 
            logging.info("[!rules]", message.author, str(when))
            

        elif message.content.startswith("!feedback"):
            feedback = message.content.split(' ')[1]
            print("!feedback wurde abgefragt" + str(when))
            print("Es wurde Feedback wieder gegeben:" + str(feedback))
            logging.info("[!feedback]", str(feedback), message.author, str(when))
            

        elif message.content.startswith("!users"):
            print("!users wurde abgefragt" + str(when))
            members = client.guilds[0].members
            for i in members:
                if i.status == discord.Status.offline:
                    members.remove(i)

            for i in members:
                print("Online Member: " + str(i))

            message.author.send("Online Members:" + members)
            logging.info("[!users]", message.author, str(when))

        elif message.content.startswith("!time"):
            print("!time wurde abgefragt" + str(when))
            message.channel.send("Es ist " + time.ctime())
            message.channel.send("Es ist " + (time.strftime("%d.%m.%Y %H:%M:%S")))
            logging.info("[!time]", message.author, str(when))
        elif message.content.startswith("!emoji"):
            print("!emoji wurde abgefragt" + str(when))
            emojis = [":)", ";)", ":]", " ༼ ༎ຶ ෴ ༎ຶ༽", "(˚Õ˚)ر ~~~~╚╩╩╝", "(✿◠‿◠)"]
            def selectRandom(emojis):
                return random.choice(emojis)

            await message.channel.send(selectRandom(emojis))
          
            logging.info("[!emoji]", message.author, str(when))
        elif message.content.startswith("!dev109283741098234091872ß568732ß5967ß098254"):
            print("Achtung Bot wird gleich gestoppt" + str(when))
            k = input("Bot beenden ? : J/N")
            if k == ("J"):
                quit()

            elif k == ("N"):
                print("Bot läuft weiter")
        
            logging.info("[!dev]", message.author, str(when))
        elif message.content.startswith("!happyhype"):
            print("!happyhype wurde aufgeruft" + str(when))
            happy = message.content.split(' ')[1]
            for i in range(10):
                time.sleep(0.5)
                await message.channel.send("Happy Birthday " + happy + "!!!", delete_after=15.1)

            logging.info("[!happyhype]", message.author, str(when))

        elif message.content.startswith("!develop"):
            await message.channel.send("Dieser Bot wurde von  programmiert, wenn du Infos über die Werkzeuge haben möchtest siehe unten")
            time.sleep(3)
            await message.channel.send("Der Server: https://www.raspberrypi.org/products/raspberry-pi-4-model-b/ ")
            await message.channel.send("Der aktuelle Computer: https://www.tuxedocomputers.com/de/Linux-Hardware/Linux-Notebooks/15-16-Zoll/TUXEDO-Aura-15-Gen1.tuxedo")
            await message.channel.send("Meine Programme sind: Pycharm Community, Vim und das Terminal Tilix")
            time.sleep(7)
            await message.channel.send("Die Aktuelle Version ist: 5.2 mit aktuell 219 Zeilen Code")
            await message.channel.send("Ja das ist jetzt auch genug Text")
            

        elif message.content.startswith("!Münzwurf"):
            f = randint(0, 1)
            if f == 0:
                results = "Kopf"

            elif f == 1:
                results = "Zahl"

            await message.channel.send("Das Ergebnis ist:" + results)




        #nachricht = message.content.split()
        #for i in nachricht:
            #if i in no_words:
                #await message.channel.send("Dies ist eine Verwahrung, bitte sei nett im Chat ansonsten gibt es ein Bann", delete_after=60.1)
                #await client.delete_message(message)
                #print(str(user) + "schrieb" + message.content)

        elif message.content.startswith("!meetings"):
            
            meet = message.content.split(' ')[1]
            meet2 = message.content.split('-')[2]
            await message.channel.send(author ," hat ein Meeting festgelegt, es findet um " ,meet ,"statt. Thema: ", meet2)
            await message.pin()
           

        else:
            print("Fehler oder kein Befehl" + str(when))

        print("Nachricht von " + str(message.author) + ":" + str(message.content) + str(when))



          # zeigt im Chat wer auf was reagiert mit einem emoji hat
    async def on_reaction_add(self, reaction, user):
           await reaction.message.channel.send(str(user) + " reacted on " + reaction.message.content + " with " + reaction.emoji)
           await reaction.message.channel.send("Gezählt: " + str(reaction.count))
           await print(reaction.message.channel.send(str(user) + " reacted on " + reaction.message.content + " with " + reaction.emoji))
           await print(reaction.message.channel.send("Gezählt: " + str(reaction.count)))



# Server Clock
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    async def on_message_delete(self, message, when, user):
        print("~Gelöschte Nachricht " + "von" + str(user) + "Nachricht: " + message.content + "wurde geschrieben um: "  + str(when) + "~")
       

        # ende
        #   zeigt bearbeitete Nachrichten an
    async def on_message_edit(self, before, after):
        print("~Changed message " + before.content + " to " + after.content + "~")
        # ende
        
        # ende
        
 # Wird alles in der Console angezeigt
    async def on_member_join(self, member, when, before, after):                ## diese funktion zeigt dir Infos über spieler an die gerade gejoined sind
        print("~Member has joinded at (" + str(when) + ")~")
        infoinput = input("Für Infos über denn User schreibe J")
        if infoinput == ("J"):
            print(str(before.joined_at))
            print(str(before.activites))
            print(str(before.guild))
            print(str(before.nick))
            print(str(before.mobile_status))
            print(str(before.desktop_status))
            print(str(before.web_status))
            print(str(before.roles))
        
#   wenn jemand dem server joined wird diese Nachricht geschickt
        await message.channel.send(str(member) + "ist dem Server beigetreten.")
        await member.send("Willkommen auf dem Server derschreibe !help in denn Chat  um heraus zufinden was es für Befehle  gibt.")
        await member.send(" MFG Bot ")
        

# wenn jemand denn server verlässt wird diese Nachricht gesendet
    async def on_member_remove(self, member, when):
        print(member + " hat denn Server verlassen!" + str(when))
        await message.channel.send(member + "hat denn Server verlassen")
        
        

# wenn user sich updatet wird das alles angezeigt
    async def on_member_update(self, before, after):
        print(str(before.joined_at) + "~Uhrzeit wann der Member gejoined ist~")
        print(str(before.activities) + "~Seine Aktivitäten~")
        print(str(before.guild) + "~Der Server~")
        print(str(before.nick) + "~Nicknames~")
        print(str(before.mobile_status) + "~der Mobile Status~")
        print(str(before.desktop_status) + "~der Deskop Status~")
        print(str(before.web_status) + "~Der Web Status~")
        print(str(before.roles) + "~Die Rolle~")
        


# Clock ende
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
client = MyClient()
client.run("") # Token hier einfügen
