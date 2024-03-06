import random

print("Taş, Kağıt, Makas oyununa hoş geldin!")

choices = ["taş", "kağıt", "makas"]

while True:
    pc = random.choice(choices)
    player = input("Taş, Kağıt, Makas hangisi? ").lower()

    print(f"Bilgisayar: {pc} seçti")
    print(f"Senin seçtiğin ise: {player}")

    if pc == player:
        print("Durum berabere!")

    elif pc == "makas" and player == "kağıt":
        print("Bilgisayar kazandı!")

    elif pc == "taş" and player == "kağıt":
        print("Tebrikler, sen kazandın!")

    elif pc == "kağıt" and player == "taş":
        print("Bilgisayar kazandı!")

    elif pc == "makas" and player == "taş":
        print("Tebrikler, sen kazandın!")

    elif pc == "kağıt" and player == "makas":
        print("Tebrikler, sen kazandın!")

    elif pc == "taş" and player == "makas":
        print("Bilgisayar kazandı!")

    play_again = input("Başka bir oyun oynamak ister misin? (Evet/Hayır): ").lower()
    if play_again != "evet":
        break