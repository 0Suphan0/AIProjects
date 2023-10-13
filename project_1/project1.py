import random

def main():
    user_score = 0
    computer_score = 0

    while user_score < 10 and computer_score < 10:
        roles = ["taş", "kağıt", "makas", "kertenkele", "spock"]
        sayi = random.randint(0, 4)

        print("taş,kağıt,makas,kertenkele,spock birini seçiniz: ")
        user_role = input().lower()
        computer_role = roles[sayi]

        if user_role == computer_role:
            print("Beraberlik.. (0 puan)")
        elif user_role == "makas":
            if computer_role == "kağıt" or computer_role == "kertenkele":
                print(f"Kazandın, bilgisayar {computer_role}")
                user_score += 1
            else:
                print(f"Bilgisayar kazandı. {computer_role}")
                computer_score += 1
        elif user_role == "kağıt":
            if computer_role == "taş" or computer_role == "spock":
                print(f"Kazandın, bilgisayar {computer_role}")
                user_score += 1
            else:
                print(f"Bilgisayar kazandı. {computer_role}")
                computer_score += 1
        elif user_role == "taş":
            if computer_role == "kertenkele" or computer_role == "makas":
                print(f"Kazandın, bilgisayar {computer_role}")
                user_score += 1
            else:
                print(f"Bilgisayar kazandı. {computer_role}")
                computer_score += 1
        elif user_role == "kertenkele":
            if computer_role == "spock" or computer_role == "kağıt":
                print(f"Kazandın, bilgisayar {computer_role}")
                user_score += 1
            else:
                print(f"Bilgisayar kazandı. {computer_role}")
                computer_score += 1
        elif user_role == "spock":
            if computer_role == "makas" or computer_role == "taş":
                print(f"Kazandın, bilgisayar {computer_role}")
                user_score += 1
            else:
                print(f"Bilgisayar kazandı. {computer_role}")
                computer_score += 1

        print(f"Puan durumu, Oyuncu: {user_score} Bilgisayar: {computer_score}")

if __name__ == "__main__":
    main()
