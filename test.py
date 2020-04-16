import time
water=0
fish=0
picture=0
battery=0
glue=1
def thirdlevel():
    def printt(x):
        print(x)
        time.sleep(0.5)
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
                if(shelf==2):
                    printt("You take the water.")
                    donewater=2
                    water=1
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
                        if(pull==2):
                            printt("You took out the batteries!")
                            battery=+1
                            donetoy=1
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
                table = int(input())
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
            printt("A model train. Always fancied a set. Cute.")
        if(doneplant+doneshelf+donefish==3):
            printt("The sweet fruity aroma in this room starts getting intoxicating. The pink turns into red, the floor gets hotter")
            printt("The single door in the room seems to be your only option, answers elude you as you continue further and open the door.")
            printt("_________________________")
thirdlevel()