import time
import os

battery=0
water=0
peeped=0
glue=0
lighter=0
jess=0
fish=0
picture=0
mom=0



def game():
    firstlevel()
def firstlevel():
    def printt(x):
        print(x)
        time.sleep(1)


    printt("")
    printt("You awaken in a dimly lit room, head spinning, mouth dry. You have no recollection of how you got there or where you are.")
    printt("1. Familiarize Surroundings\n>")
    firstinput=int(input())
    if(firstinput==1):
        printt("You're lying in an unfamiliar bed in a dusty room. The only source of light is a moonbeam from the skylight which doesn't help much.\nThere's a table to your left with an empty glass of water")
    firstlevel=3
    key=0
    while(firstlevel!=1):
        printt("1. Examine Table")
        printt("2. Check Self")
        printt("3. Dart to the door\n>")
        sec=int(input())
        if(sec==1):
            printt(" At one point in its lifetime, the table looks to have been white but time and use has left only a shell of its former glory.")
            printt("1. Open Drawer\n>")
            table=int(input())
            if(table==1):
                printt("There's a Key, a torch with no batteries and a Bible inside. Huh, the Bible is, blank.")
                printt("1. Take the key and the torch\n>")
                yes=int(input())
                if(yes==1):
                    printt("You took the key and the torch")
                    firstlevel=2
                    key=1
                    global battery
                    battery=0
                    global water
                    water=0

                else:
                    firstlevel=3
        if(sec==2):
            printt("Shirt untucked, sleeves folded, red tie loosened, pockets empty. The only distinctive feature about you is the cigarette burn like scars on your arm.")
            checked=1


        if(sec==3 and key==0):
            printt("You dart to the door, not paying any attention to your peripheral vision, too scared of what might be around.")
            printt("The door seems to be locked. But, there's a peephole.")
            printt("1. Peep through peephole\n2. Examine Table\n3. Check Self\n>")
            peep=int(input())
            if(peep==1):
                printt("Flickering lights, stained wallpaper surround an elevator, one that may be seen in old hotels.")

                global peeped
                peeped=1
        if(sec==3 and key==1):
            printt("You unlock the door frantically, trying to get away from this cold, dark place as fast as you can. You step through the door, a flash of light blinds your eyes.")
            firstlevel=1
            secondlevel()

def secondlevel():
    def printt(x):
        print(x)
        time.sleep(1)
        global peeped
        global water
        global jess
        global lighter
        global water
        global glue

    printt("_____________________________________________________________")
    printt("You pick yourself back up as your vision recovers.")
    printt("You find yourself in some kind of an office floor. Lights still flickering; the floor, squeaky clean.")
    printt("The door behind you is locked.")
    if(peeped==1):
        printt("The 'Hotel Elevator' you saw is nowhere to be seen")

    look2=0
    while(look2!=1):
        printt("1. Look Around\n>")
        look2=int(input())

    printt("A typical office environment, a faceless organisation. Seems to be the kind of a place where thousands of hours have been wasted on everything pointless")
    printt("The room primarily consists of tables, counters and cubicles. An ajar door squeaks from the other end of the room")
    printt("You notice a bulletin board a little further away.")
    walk2=0
    while(walk2!=1):
        printt("1. Walk to bulletin board\n>")
        walk2=int(input())

    printt("****SOULSUCK INC****")
    printt("Gibberish documents, notices and pictures of strange yet familiar places crowd the board.")
    printt("A screeching sound pierces through the door at the other end of the room.")
    printt("Just listening to that shrieking leaves you scornful and agitated, making you reluctant to go anywhere near it.")
    cubic=0
    while(cubic not in (1,2)):
        printt("1. Go to the cubicles")
        printt("2. Open the door with the screeching anyway\n>")
        cubic=int(input())
    if(cubic==1):
        printt("You walk through lines of cubicles and offices, each with depressions on the chair indicating countless hours of stress.")

        printt("All but one are unlit.\n")

        printt("You walk towards the unlit cubicle. It feels welcoming yet repelling at the same time.\n")

        printt("The cubicle looks well maintained. Adorned with files, papers and everyday office accessories.\n")

        printt("Amongst all this, a few things stand out...")

        donedesk=0
        donediary=0
        donemed=0
        donegol=0
        lighter=0
        glue=0
        while(donedesk!=4):
            printt("1. Inspect journal")
            printt("2. Open desk Drawer")
            printt("3. Look at medal\n>")
            desk=int(input())
            if(desk==1):
                printt("An old brown leather diary, with pages falling out, held in place with a rubber band.")
                printt("1. Open the diary.\n>")
                diary=int(input())
                if(diary==1):
                    printt("akanvubquqbvghjfoasncyasx..LETMEL1VE..xnkasnxiacpknax..SAV3HER..xxncaspaspx..COMEB4CK..xpnqbxvxzyuqwb..7AKEMEBACK..")
                    printt("Huh, just some gibberish scramblings I guess.")
                    donediary=1

            if(desk==2 and glue==0 and lighter==0):
                print("You open the desk drawer.\n")
                print("There's some glue and a lighter inside")
                gol=0
                while(gol not in (1,2)):
                    printt("1. Take the Glue")
                    printt("2. Take the lighter\n>")
                    gol=int(input())
                if(gol==1):
                    printt("You took the glue.")
                    glue=1
                    donegol=1
                if(gol)==2:
                    printt("You took the lighter")
                    lighter=1
                    donegol=1
            if(desk==2 and(glue!=0 or lighter!=0)):
                printt("You already inspected the drawer!")
            if(desk==3):
                printt("It's an employee of the year medal.")
                print("This medal is given to", name, "for their exemplary ability performance and dedication to the numbers of SOULSUCK INC")
                donemed=1
            if(donediary==1 and donegol==1 and donemed==1):
                donedesk=4
        printt("As you scutter through the table, trying to find some meaning of what's going on, the Desktop Computer turns on. It's password protected.")
        printt("There's a screensaver")
        print("'**SOULSUCK INC**'")
        print("'We. Crunch. Numbers.'")
        password=0
        pc=0
        login=0
        while(login!=1):
            print("1. Enter Password")
            print("2. Look at screensaver")
            print("3. Read journal text")
            pc=int(input())
            if(pc==1):
                password=int(input("Enter password:"))
                if(password==1347):
                    login=1
                    printt("The Computer unlocked.")
                    printt("The wallpaper changed to that of a woman in her 30s, feeding a little girl of around 6 on a family dining table.")
                    printt("A contrastful sight to the outlook of the office.")
                    printt("You can't stop looking at the lady and the girl but some files on the computer catch your attention.")
                    files=0
                    donefiles=0
                    while(donefiles!=1):
                        print("1. MonthlyBudget.xls")
                        print("2. DailyTimes13/04/16.png")
                        print("3. An Email Client")
                        files=int(input())
                        if(files==1):
                            printt("A budget spreadsheet of homely expenses.")
                            printt("'Balance = $-429'")
                        if(files==2):
                            printt("A newspaper article from the 13th of April 2016")
                            printt("'---SUBURBAN HOUSE BURNS DOWN, KILLS 1---'\n")
                            printt("'A house in Underland went up in flames at around 22:53. By the time the fire department arrived, the fire already engulfed one, 7 year old.\n The fire seems to have been caused by an electric kettle, igniting the wallpaper.\n A statement from the parents is yet to be received.'")
                        if(files==3):
                            printt("An email client, overflown with spam and official emails.")
                            printt("A notification of 2 unsent emails pop-up, asking to be resent.")
                            print("1. 'Hey Jessica, gonna skip dinner tonight. I know you were planning it for a while, but I'm sorry, some work popped up.\n See you later.'",name)
                            print("2. 'Respected Sir, I'm going to have to decline the offer to host tonight's meeting.\n I know that it would've really catapulted my career and the promotion seems really sweet, but it might get hectic and I don't think I have\n any more time to give to my work. Thanks for the opportunity.'",name)
                            printt("Which one will you send?\n>")
                            send=int(input())
                            if(send==1):
                                jess=1
                            donefiles=1
                            printt("The monitor glows, brighter and brighter and brighter.")
                            printt("You lose consciousness and fall back on your chair")
                            print("___________________________________")
                            thirdlevel()

                if(password!=1347):
                    printt("Incorrect Password")

            if(pc==2):
                printt("**SOULSUCK INC**\n we. crunch. NUMBERS.")
            if(pc==3):
                printt("akanvubquqbvghjfoasncyasx..LETMEL1VE..xnkasnxiacpknax..SAV3HER..xxncaspaspx..COMEB4CK..xpnqbxvxzyuqwb..7AKEMEBACK..")



    if(cubic==2):
        printt("You walk inside the room with the shrieking noise anyway.")
        printt("The squealing was coming from a Kettle.")
        kettle=0
        while(kettle!=1):
            printt("1. Walk to Kettle\n>")
            kettle=int(input())
        printt("You walk to the screeching red kettle. Steam bellows through it as the kettle radiates heat all around. The paint on it indicates years of mindless usage.")
        kettleoff=0
        while(kettleoff!=1):
            printt("1. Try turning it off")
            kettleoff=int(input())
        print("The kettle doesn't seem to turn of despite multiple tries; its shrieking, neverending.")
        printt("1. Look around\n>")
        look3=int(input())
        if(look3==1):
            printt("It looks like an office kitchen. A fridge, riddled with drawings from employees' children and a microwave occupy the left of the room.")
            printt("Tens of identical dirty coffee mugs fill the sink to the brim")
            printt("A clock stationed near the frontmost wall makes a peculiar ticking sound.")
            printt("1. Inspect Clock\n")
            clock=int(input())
            if(clock==1):
                printt("The clock is ticking, yet stuck displaying the time 22:53.")
                printt("The clock has batteries you can use.\n1. Take them out")
                clock2=int(input())
                if(clock2==1):
                    printt("You took the batteries.")
                    battery=1
        printt("The kettle's shrieking at it's highest volume forces you to leave the room.")
        cubicrec=0
        while(cubicrec!=1):
            printt("1. Go to the cubicles")
            cubicrec=int(input())
        printt("You walk through lines of cubicles and offices, each with depressions on the chair indicating countless hours of stress.")

        printt("All but one are unlit.\n")

        printt("You walk towards the unlit cubicle. It feels welcoming yet repelling at the same time.\n")

        printt("The cubicle looks well maintained. Adorned with files, papers and everyday office accessories.\n")

        printt("Amongst all this, a few things stand out...")

        donedesk=0
        donediary=0
        donemed=0
        donegol=0
        lighter=0
        glue=0
        while(donedesk!=4):
            printt("1. Inspect journal")
            printt("2. Open desk Drawer")
            printt("3. Look at medal\n>")
            desk=int(input())
            if(desk==1):
                printt("An old brown leather diary, with pages falling out, held in place with a rubber band.")
                printt("1. Open the diary.\n>")
                diary=int(input())
                if(diary==1):
                    printt("akanvubquqbvghjfoasncyasx..LETMEL1VE..xnkasnxiacpknax..SAV3HER..xxncaspaspx..COMEB4CK..xpnqbxvxzyuqwb..7AKEMEBACK..")
                    printt("Huh, just some gibberish scramblings I guess.")
                    donediary=1

            if(desk==2 and glue==0 and lighter==0):
                print("You open the desk drawer.\n")
                print("There's some glue and a lighter inside")
                gol=0
                while(gol not in (1,2)):
                    printt("1. Take the Glue")
                    printt("2. Take the lighter\n>")
                    gol=int(input())
                if(gol==1):
                    printt("You took the glue.")
                    glue=1
                    donegol=1
                if(gol)==2:
                    printt("You took the lighter")
                    lighter=1
                    donegol=1
            elif(desk==2 and(glue!=0 or lighter!=0)):
                printt("You inspected the drawer!")
            if(desk==3):
                printt("It's an employee of the year medal.")
                print("This medal is given to", name, "for their exemplary ability performance and dedication to SOULSUCK INC")
                donemed=1
            if(donediary==1 and donegol==1 and donemed==1):
                donedesk=4
        printt("As you scutter through the table, trying to find some meaning of what's going on, the Desktop Computer turns on. It's password protected.")
        printt("There's a screensaver")
        print("'**SOULSUCK INC**'")
        print("'We. Crunch. Numbers.'")
        password=0
        pc=0
        login=0
        while(login!=1):
            print("1. Enter Password")
            print("2. Look at screensaver")
            print("3. Read journal text")
            pc=int(input())
            if(pc==1):
                password=int(input())
                if(password==1347):
                    login=1
                    printt("The Computer unlocked.")
                    printt("The wallpaper changed to that of a woman in her 30s, feeding a little girl of around 6 on a family dining table.")
                    printt("A contrastful sight to the outlook of the office.")
                    printt("You can't stop looking at the lady and the girl but some files on the computer catch your attention.")
                    files=0
                    donefiles=0
                    while(donefiles!=1):
                        print("1. MonthlyBudget.xls")
                        print("2. DailyTimes13/04/16.png")
                        print("3. An Email Client")
                        files=int(input())
                        if(files==1):
                            printt("A budget spreadsheet of homely expenses.")
                            printt("'Balance = $-429'")
                        if(files==2):
                            printt("A newspaper article from the 13th of April 2016")
                            printt("'---SUBURBAN HOUSE BURNS DOWN, KILLS 1---'\n")
                            printt("'A house in Underland went up in flames at around 22:53. By the time the fire department arrived, the fire already engulfed one, 7 year old.\n The fire seems to have been caused by an electric kettle, igniting the wallpaper.\n A statement from the parents is yet to be received.'")
                        if(files==3):
                            printt("An email client, overflown with spam and official emails.")
                            printt("A notification of 2 unsent emails pop-up, asking to be resent.")
                            print("1. 'Hey Jessica, gonna skip dinner tonight. I know you were planning it for a while, but I'm sorry, some work popped up. See you later.'", name)
                            print("2. 'Respected Sir, I'm going to have to decline the offer to host tonight's meeting.\n I know that it would've really catapulted my career and the promotion seems really sweet, but it might get hectic and I don't think I have any more time to give to my work.\n Thanks for the opportunity.'",name)
                            printt("Which one will you send?\n>")
                            send=int(input())
                            if(send==1):
                                jess=1
                            donefiles=1
                            printt("The monitor glows, brighter and brighter and brighter.")
                            printt("You lose consciousness and fall back on your chair")
                            print("___________________________________")
                            thirdlevel()

                if(password!=1347):
                    printt("Incorrect Password")

            if(pc==2):
                printt("**SOULSUCK INC**\n we. crunch. NUMBERS.")
            if(pc==3):
                printt("akanvubquqbvghjfoasncyasx..LETMEL1VE..xnkasnxiacpknax..SAV3HER..xxncaspaspx..COMEB4CK..xpnqbxvxzyuqwb..7AKEMEBACK..")

def thirdlevel():
    def printt(x):
        print(x)
        time.sleep(1)
    global water, fish, picture, battery
    printt("You regain consciousness as you gasp for air. You find yourself on a carpeted floor, with a sweet homely scent surrounding you. ")
    look=0
    while(look!=1):
        printt("1. Look Around")
        look=int(input())
    printt("You try to make sense of what's going on as you find yourself in what seems like a kid's room. Pink and purple decor all around.")
    printt("Posters and drawings on the wall reinstate the same.")
    printt("Toys on the ground, kids books stacked together.")
    printt("The room seems a little suffocating for some reason.\n")
    room=0
    while(room!=5):
        print("1. Go to bookshelf")
        printt("2. Inspect bedside table")
        printt("3. Go to the window")
        printt("4. Check out model train")
        room=int(input())
        doneplant=0
        doneshelf=0
        donefish=0
        if(room==1):
            printt("A rather posh looking teak bookshelf for a kids room, heaving with children's books.")
            printt("'Enid Blyton, Roald Dahl, Rudyard Kipling, hmm.'")
            shelf=0
            donepic=0
            donetoy=0
            donewater=0
            donebook=0
            while(shelf!=5):
                printt("1. Take out the half poking book")
                printt("2. Take half filled water bottle")
                printt("3. Inspect stuffed toy")
                printt("4. Look at Photo frame")
                shelf=int(input())
                if(shelf==1):
                    printt("'Through the Looking Glass' by Lewis Caroll, good book, really takes you back. ")
                    donebook=1
                if(shelf==2 and takenw==0):
                    printt("You take the water.")
                    takenw=1
                    donewater=2
                    water=1
                if(shelf==2 and takenw==1):
                    printt("You already took the water")
                if(shelf==3):
                    printt("A classic brown teddy bear, with a string coming out of the back")
                    printt("'Pull me' reads the sign.")
                    pull=0
                    while(pull!=2):
                        printt("1. Pull the string")
                        printt("2. Take out the batteries")
                        pull=int(input())
                        if(pull==1):
                            printt("In an almost painfully shrill pitch, the toy says:\n'Wake up! Rise and Shine! Wake Up!'\nEerie, never liked these dolls anyway.")

                        if(pull==2 and takenb==1):
                            printt("You took out the batteries!")
                            battery=+1
                            donetoy=1
                            takenb=1
                        if(pull==2 and takenb==1):
                            printt("You already took the batteries")
                if(shelf==4):
                    if(glue==1):
                        printt("A torn picture inside a photo frame.")
                        printt("You used your glue to fix it to what it may have been")
                        printt("A wedding picture. The groom dressed in a rather make-do tuxedo, while the bride couldn't look prettier.")
                        printt("Pretty picture; everyone in it, as joyous as can be.")
                        picture=1

                    donepic=1
                    if(glue==0):
                        printt("A torn picture inside a photo frame")
                        donepic=1
                if(donebook+donetoy+donewater+donepic==4):
                    shelf=5
                    doneshelf=1
        if(room==2):
            printt("A neat and squared bedside table, convenient for everyday use and stubbing toes on. The bed seems to be made as well, except, \n there's a depression on the pillow.")
            bed=0
            while(bed!=3):
                printt("1. Look at Goldfish Bowl")
                printt("2. Look at Card")
                table=0
                table=int(input())
                if(table==1):
                    printt("A goldfish in a bowl with no water. It seems to have gotten tired of gasping and is slowly fading away. Really morbid.")
                    bed=3
                    if(water>0):
                        printt("Do you want to refill the bowl with water?")
                        bowl=0
                        printt("1. Yes")
                        printt("2. No")
                        bowl=int(input())
                        if(bowl==1):
                            printt("You poured the water into the bowl. The fish, almost immediately moves into the liquid of life it was derived of as the life\nkicks back into it.")
                            printt("Phew. Feels good.")
                            fish=1
                            water=-1
                            bed=3
                            donefish=1
                        else:
                            printt("Bye fishy.")
                            bed=3
                    else:
                        printt("Some water would've really put the life back into it.")
                if(table==2):
                    printt("A get well soon card. Really shallow and low effort.")
        if(room==3):
            printt("A beautiful window with sunlight piercing through. Will really make your sundays lively.")

            look4=0
            while(look4!=1):
                printt("1. Look outside")
                look4=int(input())
            printt("Huh, there's a brick wall outside. How's the sunlight coming through?")
            printt("There's something on the window sill:")
            window=0
            while(window!=1):
                printt("1. Inspect plant.")
                window=int(input())

            printt("A withered plant. It's dead but still has a pleasant fragrance somehow. What remains of it indicate it might've been a daisy plant.")
            printt("Daisy, a pretty name for a flower.")
            doneplant=1
            if(water>0):
                printt("1. Pour water into it")
                printt("2. Back away")
                plant=0
                plant=int(input())

                if(plant==1):
                    printt("You poured the water into it.")
                    printt("Doesn't seem like much will happen, its too late to save it. Huh, what a waste.")
                    water=-1
                else:
                    window=1
        if(room==4):
            printt("A model train. Always fancied one, but from distance unfortunately.")
            printt("It requires a battery to function.")
            train=0
            while(train not in (1,2)):
                printt("1. Use a battery")
                printt("2. Leave it be")
                train=int(input())
            if(train==1 and battery>0):
                battery=-1
                printt("You used a battery and the train starts to move.")
                printt("Your current sense of consciousness finds it difficult to look away.")
                print("Chuga-Chug, Chuga-Chug, Chuga-Chug. It's whistles sound like shrill screams.")
                printt("In your hypnotic spectation, a vision appears before your eyes. You're dressed to your best, at a toy store, \n buying this exact train set.")
                printt("But, for whom?")
            if(train==1 and battery==0):
                printt("You don't have any batteries")
            if(train==2):
                printt("You back away.")

        if(doneplant+doneshelf+donefish==3):
            printt("The sweet fruity aroma in this room starts getting intoxicating. The pink turns into red, the floor gets hotter")
            printt("The single door in the room seems to be your only option, answers elude you as you continue further and open the door.")
            printt("_________________________")
            fourthlevel()


def fourthlevel():
    def printt(x):
        print(x)
        time.sleep(1)
    global battery, lighter, mom
    printt("You wake up on a homely couch, you acquaint yourself to your surroundings and realise that this is the home where you grew up")
    look3=0
    while(look3!=1):
        printt("1. Look around")
        look3=int(input())
    printt("You're back to your 11 year old self, at this point your brain has given up on trying to pace up.")
    printt("Next to you, sits your father on his recliner, watching the Television. Beer bottles surround him.")
    printt("You wonder what he could be watching, since all you see is static on the TV.")
    printt("There are some books and toys lying on a table in the centre.")
    printt("All of them are old, as if they have been passed down for generation.")
    printt(" ")
    printt("Your father never bothered to spend money on things he thought were useless.")
    printt(" ")
    printt("You hear a sound coming from somewhere. Almost sounds like, a woman is crying...")
    ins=0
    while(ins!=1):
        printt("1. Inspect where the sound is coming from")
        ins=int(input())
    printt("The sound is coming from the basement door The woman is crying in pain.\nIt seems like she may be hurt.")
    lookdad=0
    while(lookdad!=1):
        printt("1. Try to talk to father")
        lookdad=int(input())
    printt("Your father doesn't seem to know that you are there. In fact, he is quite motionless.\n You get up and walk to the door. Gently opening it, you see that it is pitch black inside.")
    printt("")
    printt("You need your torch to go inside.")
    havebat=0
    while(havebat!=1):
        printt("1. Use the torch")
        havebat=int(input())
    if(havebat==1 and battery==0):
        printt("You don't have any batteries.")
        printt("You look around frantically, to where you can find any batteries.")
        printt("")
        printt("The TV Remote!")
        gototv=0
        while(gototv!=1):
            printt("1. Go to the TV")
            gototv=int(input())
        printt("The TV, still throwing out nothing but static. Your father's lifeless eyes still glued to it.")
        printt("You find the TV remote on the table next to your dad's couch")
        printt("")
        take=0
        while(take!=1):
            printt("1. Take the batteries out of the remote")
            take=int(input())

        printt("You take the batteries out of the remote")
        battery=1
        printt("As you start walking away, your father jumps up in his seat, and catches hold of you.")
        printt("")
        printt("'Where are you going boy? Play around again?'")
        printt("")
        printt("'Ever done anything to make me proud, huh? Why can't you be like these smart kids on TV?!'")
        printt("")
        printt("'Wasting so much money on raising this kid when all he gotta do is bring me and his bitch of a mother shame.'")
        printt("")
        printt("")
        printt("'Now, do some good in your life and light my cigar or I swear to god I'll burn it into your skin.'")
        light=0
        while(light!=1):
            printt("1. Light the cigar")
            light=int(input())
        if(light==1 and lighter==1):
            printt("Your hands shake as you pull the lighter out of your pocket.")
            printt("You light the cigar as your father watches you intently")
            printt("")
            printt("'Now scram and do whatever the hell you want, waste of breath. As useless as your mother.'")
        if(light==1 and lighter==0):
            printt("You look for a lighter but you don't have one nor is one around")
            printt("Your father, annoyed with the delay, slaps you.")
            printt("'Here, use these matches or can your daft brain not do that either?!'")
            matches=0
            while(matches!=1):
                printt("1. Light the cigar with matches")
                matches=int(input())
            printt("You light the cigar")
            printt("The shaking of your hands cause you to make the cigar fall from your father's mouth")
            printt("'You disgrace! Can't do ONE THING CORRECTLY! Should've given you away to someone who'd give me even a dollar for your meat.'")
            printt("")
            printt("Your father proceeds to burn your arm with his cigar. The pain flows through your body but the numbness in there gives you the ability to not scream with agony.")
            printt("")
            printt("Tears in your eyes, you don't stop for a second as you race to the basement door")
    if(havebat==1 and battery>0):
        printt("You put the batteries in your torch and go forth. ")
    printt("As you climb down the stairs, throwing light all around, you see your mother.\nYour father has trapped her in the basement. ")
    printt("")
    printt("Images from this night come rushing back to you.")
    printt("")
    printt("This is the night your father killed your mother.")
    print("Run away", name, "please! If he sees you, he'll kill you. He's lost it! Please, just leave me.")
    printt("If you love me, you'll run away please! I'll be fine, don't worry.")
    run=0
    while(run not in (1,2)):
        printt("1. Go to your mother")
        printt("2. Run away as she told you to.")
    run=int(input())
    if(run==1):
        printt("You are fear stricken. It is as if your body is moving automatically.\nYou run into the living room, and past your father.")
        printt("'You sissy little boy! Run away! Your mum is gone anyway. No use of keeping you here.'")
        printt("You run out the door and into the street, when you hear a gunshot come from your house.")
        printt("")
        printt("You trip over and fall to the ground.")
    if(run==2):
        printt("You walk up to her and wrap your arms around her. It has been years since you have felt her embrace. ")
        printt("You hear your father coming down the stairs. He cocks his gun. This is it. He is going to kill her.")
        printt("")
        printt("But this time, you can save her. You run to your father and tackle the gun out of his hands.")
        printt("Picking it up, you point the gun at him. ")
        printt("'Oh, so you are going to shoot me?! HAHA.' He laughs at you.")
        printt("You hear your mother whimpering in fear behind you. Brimming with emotions.")
        shoot=0
        while(shoot not in (1,2)):
            printt("1. Shoot your father")
            printt("2. Drop the gun")
            shoot=int(input())
        if(shoot==2):
            printt("Your hands begin to shake, and your father grasps the gun out of your hand and shoots your mother in her head.\n You stumble backwards, in shock, and fall to the ground.")
            printt("Everything goes, silent.")
            printt('__________________________')
            final()
        if(shoot==1):
            printt("You shoot him in his chest. Once. Twice. Thrice. ")
            printt("You hear your mother scream. Your ears, ringing.")
            printt("You have killed him. You finally have. You look at your mother and rush to hug her.")
            printt("")
            printt("The ringing and spinning increases tenfold, images collide.")
            printt("")
            printt("Before you can reach her, you stumble backwards, in shock, and fall to the ground.")
            printt("Everything goes, silent.")
            printt("________________________________")
            mom=2
            final()

def final():
    global mom
    global jess
    global fish
    global picture
    alive=mom+jess+fish+picture
    def printt(x):
        print(x)
        time.sleep(1)
    def strike(text):
        result = ''
        for c in text:
            result = result + c + '\u0336'
        print(result)
    printt("You are back in the kid's bedroom now. There is a little girl playing with the train set on the table,\nand with her is her mother.")
    printt("She beams a smile at you and says, 'Come play with us, Papa.'")
    printt("Jessica, your wife. The wedding picture that rests on the shelf is yours. And Daisy. She is Daisy. Your Daisy.\nYour little daughter. This is her room, the one you and Jessica decorated with love. ")
    printt("")
    printt("'I, Jessica Newhart, take this man, to be my lawfully wedded husband,\nto have and to hold from this day forward, for better, for worse, for richer, for poorer, in sickness and in health,\nuntil death do us part.'")
    printt("You can almost hear her saying the vows, just like she did on the day you married her.\nThe promises you made to each other, the vows you were supposed to hold for the rest of your life. ")
    printt("")
    printt("You recall the day you got married. The church was beautifully lit with candles.\nYou chuckle as you remember the power failure that had happened all over the town on your wedding day.\n This may have thrown another person off, but Jessica had decided to make the evening wonderful by using hundreds of candles to light up the church.\nShe was indeed an extraordinary woman. To have and to hold. For better and for worse.\n For richer and for poorer. In sickness and in health.\nBut there are certain things in our life which are immutably out of our control.")
    printt("The goldfish you bought Daisy for her seventh birthday rests on the table.\nSomehow, you can't remember anything past that. You can remember everything from the day you first held her in your arms, till the day she jumped with joy all\naround the house upon seeing the goldfish. But, nothing beyond that.")
    printt("")
    printt("'Look at this train entering the station, Papa!' She calls you again.")
    printt("Your little girl. Something about all of it makes you feel sick. You wish to go hear them laugh,\nto hold them. But there is something you are missing.You take a step towards them,\n and almost immediately, they disappears. Puzzled, you turn around to see where they went,\n only to find yourself sitting in a chair.")
    printt("")
    printt("")
    printt("You hear a kettle bellowing in the distance. What is that sound? Where are you? ")
    printt("It takes you a few seconds to realise that you are sitting at your cubicle in the office. Soul Suck Incorporated.\n The computer displays endless emails from your clients.")
    printt("")
    printt("There are files stacked on your desk. Below all those files, is one which doesn't seem like it belongs.\n You pull it out from underneath, to see that those are divorce papers which you need to sign.")
    printt("Wait. Jessica is divorcing you. But why? What could go so wrong? You were happy, weren't you? ")
    printt("")
    printt("The screeching of the kettle. It's triggering a headache. ")
    printt("")
    printt("'Can someone just shut that thing off?' You shout out.")
    printt("Suddenly, it hits you. The kettle. It was the kettle. The kettle you forgot to turn off that started the fire. ")
    printt("You type in your password to the computer again, to glance at that article once more.")
    printt("")
    printt("It was your house that burnt down, along with your daughter in it. ")
    printt("Overwhelmed with emotions, you look at the 'Employee of the Month' medal lying on your desk.\nAfter your daughter died, you started working late, putting in more hours, anything to go back to the emptiness you felt.")
    printt("You left Jessica alone to deal with HER pain.")
    printt("")
    printt("Tears fill your eyes")
    printt("There is a door to your left, bright light radiating from inside whatever is in there. You are compelled to walk inside.")
    printt("")
    printt("")
    printt("You are in the room, the one where you began. This looks like a hotel room to you, now that you pay attention to it. ")
    printt("There is a bottle of sleeping pills in your hand, a glass of water in the other.")
    printt("Killing yourself in a hotel room seems very cold. But that is what you felt in your life.\nCold and distant from everyone. ")
    printt("")
    choose=0
    scream=0
    called=0
    while(choose not in (1,2,3)):
        printt("1. Scream")
        printt("2. Call out to Jessica")
        printt("3. Put down the pills")
        printt("4. Take the pills")
        choose=int(input())
    if(choose==1 and called==0):
        printt(strike("1. Scream"))
        printt("2. Call out to Jessica")
        printt("3. Put down the pills")
        printt("4. Take the pills")
    if(choose==1 and called==1):
        printt(strike("1. Scream"))
        printt(strike("2. Call out to Jessica"))
        printt("3. Put down the pills")
        printt("4. Take the pills")
    if(choose==2 and scream==0):
        printt("1. Scream")
        printt(strike("2. Call out to Jessica"))
        printt("3. Put down the pills")
        printt("4. Take the pills")
    if(choose==1 and scream==1):
        printt(strike("1. Scream"))
        printt(strike("2. Call out to Jessica"))
        printt("3. Put down the pills")
        printt("4. Take the pills")
    if(choose==3 and alive>=4):
        printt("You lie down straight on the bed and close your eyes. You can hear some machines beeping.\n There is also a strong smell of aseptic bombarding your nose. Almost like you are in a hospital.\nThe sound of the ventilator, attached to you, as you hand on to life.")
        printt("You open your eyes slowly. The light coming in through the window is almost too painful for you.\n A woman pulls the curtains for your comfort, and then walks up to you.'Are you okay? You had me so scared. How could you leave me alone?' It is Jessica.\n She holds your hand and smiles at you through her tears.")
    if(choose==3 and alive<=4):
        printt("You lie down straight on the bed and close your eyes. You can hear some machines beeping.\n There is also a strong smell of aseptic bombarding your nose. Almost like you are in a hospital.\nThe sound of the ventilator, attached to you, as you hand on to life.")
        printt("The pain is ending gradually. This is how it feels to die.\nAll those people who said that you see your life flash by were right.\n You are going to be with Daisy now. And there could be nothing better than it.")
    if(choose==4):
        printt(strike("1. Scream"))
        printt(strike("2. Call out to Jessica"))
        printt("3. Put down the pills")
        printt(strike("4. Take the pills"))




print(r"""  _      _           _
 | |    (_)         | |
 | |     _ _ __ ___ | |__   ___
 | |    | | '_ ` _ \| '_ \ / _ \
 | |____| | | | | | | |_) | (_) |
 |______|_|_| |_| |_|_.__/ \___/

                                 """)
print("Welcome to Limbo, a choose your own adventure game. Throughout the game, you'll get choices that will tailor the story and your experience.\nWe would encourage exploring to the fullest! You will be informed when the game is saved, after which you have the ability\n to go back and replay a segment of the game.")
print("To begin, enter your name: ")
name=input()
if(name!=''):
    game()

