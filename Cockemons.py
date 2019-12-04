
import time
import sys
import random
bohus = 0
dänischer_landhahn = 0
deutscherlachshahn = 0
def delay_print_fast(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0007)
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
import os
clear = lambda: os.system('clear') #on Linux System for Win change clear to cls
clear()
delay_print_fast("""
╔════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                        Elio Thalmann   ║
║                                ,~.                                                     ║
║                             ,-'__ `-,                                                  ║
║                            {,-'  `. }              ,')                                 ║
║                           ,( o )   `-.__         ,',')~,                               ║
║                          <=.) (         `-.__,==' ' ' '}                               ║
║                            (   )                      /                                ║
║                             `-'\   ,                  )                                ║
║                                 |  \        `~.      /                                 ║
║                                 \   `._        \    /                                  ║
║                                  \     `._____,'   /                                   ║
║                                   `-.            ,'                                    ║
║                                      `-.      ,-'                                      ║
║                                         `~~~~'                                         ║
║                                         //_||                                          ║
║                                      __//--'/`                                         ║
║                                    ,--'/`  '                                           ║
║                                       '                                                ║
║ ██████╗ ██████╗  ██████╗██╗  ██╗     ███████╗    ███╗   ███╗ ██████╗ ███╗   ██╗███████╗║
║██╔════╝██╔═══██╗██╔════╝██║ ██╔╝     ██╔════╝    ████╗ ████║██╔═══██╗████╗  ██║██╔════╝║
║██║     ██║   ██║██║     █████╔╝█████╗█████╗█████╗██╔████╔██║██║   ██║██╔██╗ ██║███████╗║
║██║     ██║   ██║██║     ██╔═██╗╚════╝██╔══╝╚════╝██║╚██╔╝██║██║   ██║██║╚██╗██║╚════██║║
║╚██████╗╚██████╔╝╚██████╗██║  ██╗     ███████╗    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████║║
║ ╚═════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝     ╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝║     
╚════════════════════════════════════════════════════════════════════════════════════════╝
version 1.0                                                                   27.11.2019

""")                                                                                        
time.sleep(1)
input("""
                            ╔═════════════════════════╗
                            ╟--press enter to start.--╢
                            ╚═════════════════════════╝
""")
def enter():
    input(""" 

                                 ╔═══════════════╗
                                 ╟--press enter--╢
                                 ╚═══════════════╝
    """)
clear()
food = 100
time.sleep(2)
print("""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                      .=""=.                                       ║
║                                     / _  _ \\                                      ║
║                                    |  o  o  |                                     ║
║                                    \   /\   /                                     ║
║                                   ,/'-=\/=-'\,                                    ║
║                                  / /        \ \\                                   ║
║                                 | /          \ |                                  ║
║                                 \/ \        / \/                                  ║
║                                     '.    .'                                      ║
║                                     _|`~~`|_                                      ║
║                                     /|\  /|\\                                      ║ 
║Hallo, mein Name ist Kiri das Küken und da ich nicht männlich bin,                 ║
║wurde ich noch nicht geschreddert.                                                 ║
║Ich werde dich durch diese Spielwelt begleiten.                                    ║
║Ich bin zu jung zum Kämpfen aber ich helfe dir gerne.                              ║
╚═══════════════════════════════════════════════════════════════════════════════════╝

""")
enter()
clear()
print("""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                      .=""=.                                       ║
║                                     / _  _ \\                                      ║
║                                    |  o  o  |                                     ║
║                                    \   /\   /                                     ║
║                                   ,/'-=\/=-'\,                                    ║
║                                  / /        \ \\                                   ║
║                                 | /          \ |                                  ║
║                                 \/ \        / \/                                  ║
║                                     '.    .'                                      ║
║                                     _|`~~`|_                                      ║
║                                     /|\  /|\\                                      ║ 
║Als erstes musst du ein Starter Cock-E-Mon auswählen. Du hast die Auswahl zwischen:║
╚═══════════════════════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════════════╗
║1   ║   Schwedischer Bohus-Dal Schwarzhahn                                         ║
║2   ║   Dänischer Landhahn                                                         ║
║3   ║   Deutscher Lachshahn                                                        ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")
wstarterpoke = 0

# Cocks
stats_bohus = {
    "ascii": """
     .".".".                             
   (`       `)               _.-=-.      
    '._.--.-;             .-`  -'  '.    
   .-'`.o )  \           /  .-_.--'  `\\ 
  `;---) \    ;         /  / ;' _-_.-' ` 
    `;"`  ;    \        ; .  .'   _-' \\ 
     (    )    |        |  / .-.-'    -` 
      '-.-'     \       | .' ` '.-'-\`   
       /_./\_.|\_\      ;  ' .'-'.-.     
      |         .-=-.;-._ \  -'-,        
      \        /      `";`-`,-"`)        
       \       \     '-- `\.\\           
        '.      '._ '-- '--'/            
          `-._     `'----'`;             
              `""'--.____,/              
                     \\\\  \\            
                     // /`               
                 ___// /__               
            (`(`(---"-`)                 
""",
    "health": 120,
    "atk1": ["Schwanzwedler", 1],
    "atk2": ["Kratzer", 1],
    "atk3": ["Schrei", 1]
}
stats_dänischer_landhahn = {
    "ascii": """
                         ~-.          
   ,,,;            ~-.~-.~-           
  (.../           ~-.~-.~-.~-.~-.     
  } o~`,         ~-.~-.~-.~-.~-.~-.   
  (/    \      ~-.~-.~-.~-.~-.~-.~-.  
   ;    \    ~-.~-.~-.~-.~-.~-.~-.    
  ;     {_.~-.~-.~-.~-.~-.~-.~        
 ;:  .-~`    ~-.~-.~-.~-.~-.          
;.: :'    ._   ~-.~-.~-.~-.~-         
 ;::`-.    '-._  ~-.~-.~-.~-          
  ;::. `-.    '-,~-.~-.~-.            
   ';::::.`''-.-'                     
     ';::;;:,:'                       
        '||"                          
        / |                           
      ~` ~"                           
    """,
    "health": 100,
    "atk1": ["Schwanzwedler", 1],
    "atk2": ["Kratzer", 1.5],
    "atk3": ["Schrei", 1]
}
stats_deutscher_lachshan = {
    "ascii": """
                  ,.
                 (\(\)
 ,_              ;  o >
  {`-.          /  (_) 
  `={\`-._____/`   |
   `-{ /    -=`\   |
    `={  -= = _/   /
       `\  .-'   /`
        {`-,__.'===,_
        //`        `\\\\
       //
      `\=
                       
    """,
    "health": 50,
    "atk1": ["Schwanzwedler", 1.5],
    "atk2": ["Kratzer", 1.75],
    "atk3": ["Schrei", 1.50]
}





while (wstarterpoke == 0):
    starterpokemoninput = input("""Wen Willst du?
    >  """)
    if starterpokemoninput == "1":
        bohus = 1
        wstarterpoke = 1
        print("Du hast nun ein Schwedischer Bohus-Dal Schwarzhahn")
        time.sleep(2)
        clear()
        print("""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║      .".".".                                                                      ║
║    (`       `)               _.-=-.                                               ║
║     '._.--.-;             .-`  -'  '.                                             ║
║    .-'`.o )  \           /  .-_.--'  `\\                                           ║
║   `;---) \    ;         /  / ;' _-_.-' `                                          ║
║     `;"`  ;    \        ; .  .'   _-' \\                                           ║
║      (    )    |        |  / .-.-'    -`                                          ║
║       '-.-'     \       | .' ` '.-'-\`                                            ║
║        /_./\_.|\_\      ;  ' .'-'.-.                                              ║
║       |         .-=-.;-._ \  -'-,                                                 ║
║       \        /      `";`-`,-"`)                                                 ║
║        \       \     '-- `\.\\                                                     ║
║         '.      '._ '-- '--'/                                                     ║
║           `-._     `'----'`;                                                      ║
║               `""'--.____,/                                                       ║
║                      \\\\  \\                                                        ║
║                      // /`                                                        ║
║                  ___// /__                                                        ║
║             (`(`(---"-`)                                                          ║
║                                                                                   ║ 
║Wie willst du deinen Schwedischen Bohus-Dal Schwarzhahn nennen?                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")    
        stats_bohus["name"] = input("> ")
        print(f"Dein Hahn heisst also {stats_bohus['name']}.")

    elif starterpokemoninput == "2":
        dänischer_landhahn = 1
        wstarterpoke = 1
        print("Du hast nun ein Dänischer Landhahn")
        time.sleep(2)
        clear()
        print("""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                    ~-.                            ║
║                              ,,,;            ~-.~-.~-                             ║
║                             (.../           ~-.~-.~-.~-.~-.                       ║
║                             } o~`,         ~-.~-.~-.~-.~-.~-.                     ║
║                             (/    \      ~-.~-.~-.~-.~-.~-.~-.                    ║
║                              ;    \    ~-.~-.~-.~-.~-.~-.~-.                      ║
║                             ;     {_.~-.~-.~-.~-.~-.~-.~                          ║
║                            ;:  .-~`    ~-.~-.~-.~-.~-.                            ║
║                           ;.: :'    ._   ~-.~-.~-.~-.~-                           ║
║                            ;::`-.    '-._  ~-.~-.~-.~-                            ║
║                             ;::. `-.    '-,~-.~-.~-.                              ║
║                              ';::::.`''-.-'                                       ║
║                                ';::;;:,:'                                         ║
║                                   '||"                                            ║
║                                   / |                                             ║
║                                 ~` ~"                                             ║
║                                                                                   ║ 
║Wie willst du dein Dänischer Landhahn nennen?                                      ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")
        stats_dänischer_landhahn["name"] = input("> ") 
        print(f"Dein Hahn heisst also {stats_dänischer_landhahn['name']}.") 


    elif starterpokemoninput == "3":
        deutscherlachshahn = 1
        wstarterpoke = 1
        print("Du hast nun einen Deutschen Lachshahn")
        time.sleep(2)
        clear()
        print("""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║           
║                                                                                   ║
║                  (\(\)                                                            ║
║ ,_              ;  o >                                                            ║
║  {`-.          /  (_)                                                             ║
║  `={\`-._____/`   |                                                               ║
║   `-{ /    -=`\   |                                                               ║
║    `={  -= = _/   /                                                               ║
║       `\  .-'   /`                                                                ║ 
║        {`-,__.'===,_                                                              ║
║        //`        `\\\\                                                             ║
║       //                                                                          ║
║      `\=                                                                          ║
║                                                                                   ║
║Wie willst du dein Deutschen Lachshahn nennen?                                     ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")
        stats_deutscher_lachshan["name"] = input("> ") 
        print(f"Dein Hahn heisst also {stats_deutscher_lachshan['name']}.") 


    else:
        print("Du hast etwas falsches eingegeben.")
        enter()
enter()
clear()
print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║Das war dir schon Abenteuer genug du gehst jetzt mit deinem neuen Hahn nach Hause. ║
║Deine Mutter erwartet dich schon mit einem Lächeln und fragt dich:                 ║
║                                                                                   ║
║                                   /////////////\\\\\\\\                               ║
║                                  (((((((((((((( \\\\\\\\                              ║
║                                  ))) ~~      ~~  (((                              ║
║                                  ((( (*)     (*) )))                              ║
║                                  )))     <       (((                              ║
║                                  ((( '\______/`  )))                              ║
║                                  )))\___________/(((                              ║
║                                         _) (_                                     ║
║                                        / \_/ \\                                    ║
║                                       /(     )\\                                   ║
║                                      // )___( \\                                   ║
║                                      \\\\(     )//                                  ║
║                                       (       )                                   ║
║                                        |  |  |                                    ║
║                                         | | |                                     ║
║                                         | | |                                     ║
║                                        _|_|_|_                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
╔═══════════════════════════════════════════════════════════════════════════════════╗
║"Was hast du heute gemacht?"                                                       ║
║                                                                                   ║
║1   |   Ich habe ein Huhn gezähmt                                                  ║
║2   |   Ich war draussen Spielen                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")
askmom = input("-> ")
if askmom == "1":
    clear()
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║Wow das ist Toll, wie hast du den das geschafft?                                   ║
║                                                                                   ║
║                                                                                   ║
║                                   /////////////\\\\\\\\                               ║
║                                  (((((((((((((( \\\\\\\\                              ║
║                                  ))) ~~      ~~  (((                              ║
║                                  ((( (*)     (*) )))                              ║
║                                  )))  ________   (((                              ║
║                                  ((( '\______/`  )))                              ║
║                                  )))\___________/(((                              ║
║                                         _) (_                                     ║
║                                        / \_/ \\                                    ║
║                                       /(     )\\                                   ║
║                                      // )___( \\                                   ║
║                                      \\\\(     )//                                  ║
║                                       (       )                                   ║
║                                        |  |  |                                    ║
║                                         | | |                                     ║
║                                         | | |                                     ║
║                                        _|_|_|_                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")
    time.sleep(2)
    print("Ich :      Ich weiss nicht, ich habe das Huhn einfach von einem Kükchen das reden konnte bekommen.")
    time.sleep(2)
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║Okay, das ist Toll aber geh jetzt schlafen                                         ║
║                                                                                   ║
║                                   /////////////\\\\\\\\                               ║
║                                  (((((((((((((( \\\\\\\\                              ║
║                                  ))) ~~      ~~  (((                              ║
║                                  ((( (*)     (*) )))                              ║
║                                  )))     <       (((                              ║
║                                  ((( '\______/`  )))                              ║
║                                  )))\___________/(((                              ║
║                                         _) (_                                     ║
║                                        / \_/ \\                                    ║
║                                       /(     )\\                                   ║
║                                      // )___( \\                                   ║
║                                      \\\\(     )//                                  ║
║                                       (       )                                   ║
║                                        |  |  |                                    ║
║                                         | | |                                     ║
║                                         | | |                                     ║
║                                        _|_|_|_                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝""")
    enter()
else:
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║Okay, das ist Toll aber geh jetzt schlafen                                         ║
║                                                                                   ║
║                                   /////////////\\\\\\\\                               ║
║                                  (((((((((((((( \\\\\\\\                              ║
║                                  ))) ~~      ~~  (((                              ║
║                                  ((( (*)     (*) )))                              ║
║                                  )))     <       (((                              ║
║                                  ((( '\______/`  )))                              ║
║                                  )))\___________/(((                              ║
║                                         _) (_                                     ║
║                                        / \_/ \\                                    ║
║                                       /(     )\\                                   ║
║                                      // )___( \\                                   ║
║                                      \\\\(     )//                                  ║
║                                       (       )                                   ║
║                                        |  |  |                                    ║
║                                         | | |                                     ║
║                                         | | |                                     ║
║                                        _|_|_|_                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝""")
clear()
print("""
Du gehst jetzt ins Bett.
            ___
        ,-""___""-.
       .;""'| |`"":.
       || | | | | ||
       ||_|_|_|_|_||
      //          /|
     /__         //|
 ,-""___""-.    //||
.;""'| |`"":.  //
||/| | | | || //
||_|_|_|_|_||//
||_________||/
||         ||
''         '' 
""")
enter()
clear()
print("Du wachst ganz ausgeschlafen auf und schaust auf deinen Kalender und siehst:")
print("""
╔════╗ 
║ 11 ║    
╚════╝
Jaaaaa, es ist der 11. Juni... Das heist ich kann mich voll und ganz auf die Hühner konzentrieren.
""")
enter()
clear()
print("Du läufst aus dem Haus und was siehst du??")
print("""Deinen Erzfeind Martin
      .--.
    ________
      |Oo|
      |()|
      | -}
 .----\\""/----.
 |     \/     |
 | |    .   | |
 | |    .   | |____/__
 \ \    .   (_____/_=
  \ \       \\
   \/\=[]===)
   (""\     |
   |   |_/  |
   |   |    |

Hallo ich habe gesehen, dass du Cock-E-Mons hast... Ich fordere dich zu einem Duell aus.
""")
enter()
clear()
if bohus == 1:
    print(f"""Du wählst dein {stats_bohus['name']}.""")
    print(f"Du:   Mein mächtiger Schwedischer Bohus-Dal Schwarzhahn wird dich vernichten!")
elif bohus == 2:
    print(f"""Du wählst dein {stats_dänischer_landhahn['name']}.""")
    print(f"D:   Mein mächtiger Dänischer Landhahn wird dich vernichten!")
else:
    print(f"""Du wählst dein {stats_deutscher_lachshan['name']}.""")
    print(f"Du:    Mein mächtiger Deutscher Lachshahn wird dich vernichten!")
print("""HAHAHA du kannst gar mit deinem Cock-E-Mon gar nichts gegen mein Cock-E-Mon ausrichten.
Ich wähle Indischer Mammut Hahn""")
health_me = 100
health_enemy = 100
time.sleep(2)
done = 0
while done == 0:
    print("""Was willst du für eine Attacke einsetzen?
    1   |   Kratzen
    2   |   Schnabel
    3   |   Schrei
    """)
    kampf = input("-> ")
    if kampf == "1":
        randkampf = random.randrange(1, 50)
        print("Du hast deinen Gegner gekratzt.")
        print(f"Er hat {randkampf} Schaden gemacht.")
        health_enemy = (health_enemy - randkampf)
        if health_enemy > 0:
            print(f"Der Gegner hat noch {health_enemy} Leben")
        else:
            print("Dein Gegner ist Tot.")
            print("""
      .--.
    _______
      |Oo|
      |()|
      | -}
 .----\\""/----.
 |     \/     |
 | |    .   | |
 | |    .   | |____/__
 \ \    .   (_____/_=
  \ \       \\
   \/\=[]===)
   (""\     |
   |   |_/  |
   |   |    |
Martin:   Ahh... dieses mal hast du mich besiegt
          Aber das nägste Mal werde ich dich zerstören

            """)
            done = 1
    elif kampf == "2":
        randkampf = random.randrange(1, 50)
        print("Du hast deinen Gegner gebissen.")
        print(f"Er hat {randkampf} Schaden gemacht.")
        health_enemy = (health_enemy - randkampf)
        if health_enemy > 0:
            print(f"Der Gegner hat noch {health_enemy} Leben")
        else:
            print("Dein Gegner ist Tot.")
            print("""
      .--.
    _______
      |Oo|
      |()|
      | -}
 .----\\""/----.
 |     \/     |
 | |    .   | |
 | |    .   | |____/__
 \ \    .   (_____/_=
  \ \       \\
   \/\=[]===)
   (""\     |
   |   |_/  |
   |   |    |
Martin:   Ahh... dieses mal hast du mich besiegt
          Aber das nägste Mal werde ich dich zerstören
          
            """)
            done = 1
    elif kampf == "3":
        randkampf = random.randrange(1, 20)
        print("Du hast deinen Gegner angebrüllt.")
        print(f"Er hat {randkampf} Schaden gemacht.")
        health_enemy = (health_enemy - randkampf)
        if health_enemy > 0:
            print(f"Der Gegner hat noch {health_enemy} Leben")
        else:
            print("Dein Gegner ist Tot.")
            print("""
      .--.
    _______
      |Oo|
      |()|
      | -}
 .----\\""/----.
 |     \/     |
 | |    .   | |
 | |    .   | |____/__
 \ \    .   (_____/_=
  \ \       \\
   \/\=[]===)
   (""\     |
   |   |_/  |
   |   |    |
Martin:   Ahh... dieses mal hast du mich besiegt
          Aber das nägste Mal werde ich dich zerstören
          
            """)
            done = 1
    else:
                print("Du hast verfehlt")
    if done == 0:
        kampf = random.randrange(1, 4)
        if kampf == 1:
            randkampf = random.randrange(1, 50)
            print("Der Gegner hat dich gekratzt.")
            print(f"Er hat {randkampf} Schaden gemacht.")
            health_me = (health_me - randkampf)
            if health_me > 0:
                print(f"Du hast noch {health_me} Leben")
            else:
                print("Dein Huhn ist Kampfunfähig.")
                print("""
          .--.
        _______
          |Oo|
          |()|
          | -}
     .----\\""/----.
     |     \/     |
     | |    .   | |
     | |    .   | |____/__
     \ \    .   (_____/_=
      \ \       \\
       \/\=[]===)
       (""\     |
       |   |_/  |
       |   |    |
    Martin:   Haha ich habe dich zerstört   

                """)
                done = 1
        elif kampf == 2:
            randkampf = random.randrange(1, 50)
            print("Dein Gegner hat dich gebissen.")
            print(f"Er hat {randkampf} Schaden gemacht.")
            health_me = (health_me - randkampf)
            if health_me > 0:
                print(f"Du hast noch {health_enemy} Leben")
            else:
                print("Du bist Kampfunfähig")
                print("""
          .--.
        _______
          |Oo|
          |()|
          | -}
     .----\\""/----.
     |     \/     |
     | |    .   | |
     | |    .   | |____/__
     \ \    .   (_____/_=
      \ \       \\
       \/\=[]===)
       (""\     |
       |   |_/  |
       |   |    |
    Martin:   Haha ich habe dich zerstört

                """)
                done = 1
        elif kampf == 3:
            randkampf = random.randrange(1, 10)
            print("Dein Gegner hat dich angebrüllt.")
            print(f"Er hat {randkampf} Schaden gemacht.")
            health_me = (health_me - randkampf)
            if health_me > 0:
                print(f"Du hast noch {health_me} Leben")
            else:
                print("Dein Gegner ist Tot.")
                print("""
          .--.
        _______
          |Oo|
          |()|
          | -}
     .----\\""/----.
     |     \/     |
     | |    .   | |
     | |    .   | |____/__
     \ \    .   (_____/_=
      \ \       \\
       \/\=[]===)
       (""\     |
       |   |_/  |
       |   |    |
    Martin:   Haha ich habe dich zerstört

                """)
                done = 1
        else:
                    print("Du hast verfehlt")
