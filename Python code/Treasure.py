print (''' 
      /^\      /^\
      |  \    /  |
      ||\ \../ /||
      )'        `(
     ,;`w,    ,w';,
     ;,  ) __ (  ,;
      ;  \(\/)/  ;;
     ;|  |vwwv|    ``-...
      ;  `lwwl'   ;      ```''-.
     ;| ; `""' ; ;              `.
      ;         ,   ,          , |
      '  ;      ;   l    .     | |
      ;    ,  ,    |,-,._|      \;
       ;  ; `' ;   '    \ `\     \;
       |  |    |  |     |   |    |;
       |  ;    ;  |      \   \   (;
       | |      | l       | | \  |
       | |      | |  pb   | |  ) |
       | |      | ;       | |  | |
       ; ,      : ,      ,_.'  | |
      :__'      | |           ,_.'
               `--'
       ''')
print("Welcome to the treasure island. ")
print("Your mission is to find out treasure. ")
choice1 = input('Which direction you want to go? "left" or "right"? ').lower()
if choice1 == "left":
    choice2 = input('You\have come to a lake. there is an island you will "wait" for a boat or "swin" across. ').lower()
    if choice2 == "wait":
        choice3 = input('You\ have a door to pass, Which door do you pass "Yellow", "RED", "Blue" .').lower()
        if choice3 == "yellow":
            print("You win the game. ")
        elif choice3 == "blue":
            print("You are eaten by beast, Game over.")
        elif choice3 == "red":
            print("You are burned,Game over. ")
        else:
            print("Game over")
    else:
       print("You are dead. ")
else:
    print("You are dead. ")


          