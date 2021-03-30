print(""" 
  /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  
 / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
/ __  / (_| | | | | (_| | | | | | | (_| | | | |
\/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                               
""")
name = input("Adınızı giriniz :")
print("hangman oyununa hoş geldin", name)
print("\n"
      "  +---+\n"
      "  |   |\n"
      "  O   |\n"
      " /|\  |\n"
      " / \  |\n"
      "      |\n"
     "=========''']\n")
my_string = "leon"
sayi=len(my_string)
giris_hakki =sayi+1

while giris_hakki >0:
    new_list = []
    my_string = "leon"
    for element in my_string:
        new_list.append(element)
    harfgiris = input("bir harf giriniz")
    if harfgiris in new_list:
        print("bu harf var",harfgiris)
        print(new_list.index(harfgiris))
        print(f"{giris_hakki} giriş hakkınız var")
        new_list.remove(harfgiris)
    elif harfgiris == my_string:
        print("kazandınız ")
        break
    else:
        giris_hakki -= 1
        print(f"{giris_hakki} giriş hakkınız var")

        print("false")
        if giris_hakki==0:
            print("öldün")
