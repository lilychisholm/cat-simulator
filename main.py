print("Welcome to the cat simulator! \nI have turned you into a cat :3 \nAnything you'd like to say?")
print("(This is you by the way)")
print('''              _                        
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   1
                        
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
               [you] .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        
''')
response1 = raw_input('Responses: 1: "Meow" , 2: "Why would you do this to me?" , 3: "How did you do that?" ')
if response1 == "1":
    print("Good! The spell worked completely. You are 100% cat now hehe. What would you like to do now?")
    print(''' mouse art ''')
    response2 = raw_input('Responses: 1: "Walk around!" , 2: "I\'m hungry..." , 3: "Can I take a nap?" ')
    if response2 == "1":
        print("OOoh you're walking, and you found a mouse! What do you do?")
        response3 = raw_input("Responses: 1: 'Kill!', 2: 'I'll leave it alone', 3: 'It's my friend now hehe'")
        if response3 == "1":
            print("Spoken like a true cat! But sounds a little bit too violent, not a fan of that. No violence allowed!"
                  "\n Game Over!! Try again :3")
        elif response3 == "2":
            print("Loser!! You don't have the cat spirit!! Either the spell didn't work or you're just stupid."
                  " Either way, game over!! Try again")
        elif response3 == "3":
            print("Awwwwwwww, that's so cute, hell yeah. Commendable, and so very catlike. \n Now you and your "
                  "little mouse friend are hanging out, and it's nighttime. What do you want to do?")
            response4 = raw_input("Responses: 1: 'I'm so tired now', 2: 'Oooh, what's that thing in the corner?',"
                                  "3: 'I'm tired of this!'")
            if response4 == "1":
                print("FINE!!!! Whatever!!! Go to bed, you're a boring cat anyways >:(. Game over for you!!!")
            elif response4 == "2":
                print("WHOA!! You found the catnip treasure! It's magical catnip! "
                      "Worth a lot of money; you're rich now!"" Hooray! \n You won the game! Congrats :33")
            elif response4 == "3":
                print("WHATEVER!! YOU'RE SO UNGRATEFUL!! I use my magic to turn you into something cool like a "
                      "cat and this is the treatment I get ugh! Game over!!!!" )

        else:
            print(
                "Either a typo, or you just straight up put in a response not on the list >:(")
            print("Not cool man smh, Game Over")

    elif response2 == "2":
        print("Oh ok, here, have some tuna. I think you should stop here and eat for now. Come back later "
              "and try again.")
    elif response2 == "3":
        print("Oh fine whatever! Go take a nap. Come back later when you feel more awake >:p")
    else:
        print("Either a typo, or you just straight up put in a response not on the list >:(")
        print("Not cool man smh, Game Over")


elif response1 == "2":
    print("For fun! Although it sounds like you don't want to be a cat so I'll turn you back I guess >:(")
    print("Game over, you got turned back into a boring little human.")
elif response1 == "3":
    print("What's it to you? >:(")
    print("Game Over; you ask too many questions.")
else:
    print("Either a typo, or you just straight up put in a response not on the list >:(")
    print("Not cool man smh, Game Over")
