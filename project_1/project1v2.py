import random

def main():
    user_score = 0
    computer_score = 0

    choices = {
        "taş": ["makas", "kertenkele"],
        "kağıt": ["taş", "spock"],
        "makas": ["kağıt", "kertenkele"],
        "kertenkele": ["spock", "kağıt"],
        "spock": ["makas", "taş"]
    }

    while user_score < 10 and computer_score < 10:
        print("taş, kağıt, makas, kertenkele, spock birini seçiniz: ")
        user_role = input().lower()

        if user_role in choices:
            computer_role = random.choice(list(choices.keys()))  # Bilgisayarın rastgele seçimi
            if computer_role in choices[user_role]:
                print(f"Kazandın, bilgisayar {computer_role}")
                user_score += 1
            else:
                print(f"Bilgisayar kazandı. {computer_role}")
                computer_score += 1
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

        print(f"Puan durumu, Oyuncu: {user_score} Bilgisayar: {computer_score}")

if __name__ == "__main__":
    main()
