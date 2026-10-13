import random

movies = [
    "AAVESHAM", "EMPURAAN", "DRISHYAM", "BANGALORE DAYS",
    "AANANDAM", "PREMAM", "LUCIFER", "MANJUMMEL BOYS",
    "PREMALU", "HRIDAYAM", "KUMBALANGI NIGHTS", "MINNAL MURALI",
    "PULIMURUGAN", "CHARLIE", "USTAD HOTEL", "ROMANCHAM",
    "THALLUMAALA", "KURUP", "BHEESHMA PARVAM", "HOME",
    "FALIMY", "RDX", "KANNUR SQUAD", "NERU", "JOSEPH",
    "VIRUS", "UYARE", "DRIVING LICENCE", "ANGAMALY DIARIES",
    "KAPPELA", "GODHA", "JUNE", "VELLIMOONGA",
    "NJAN PRAKASHAN", "OPPAM", "MEMORIES", "KALI", "MALIK",
    "KURUTHI", "AARATTU", "KING OF KOTHA", "TURBO", "GARUDAN",
    "PADMINI", "SUDANI FROM NIGERIA", "THATTATHIN MARAYATHU",
    "ENNU NINTE MOIDEEN", "ORU VADAKKAN SELFIE", "SALT N PEPPER",
    "ANNAYUM RASOOLUM", "KOODE", "MAYANADHI", "SUNDAY HOLIDAY",
    "ISHQ", "KETTYOL AANENTE MALAKHA", "ANDROID KUNJAPPAN",
    "JAN E MAN", "SUPER SHARANYA", "SACHIN", "KAMMATIPAADAM",
    "EE MA YAU", "NIZHAL", "PACHUVUM ATHBHUDHAVILAKKUM",
    "GURUVAYOOR AMBALANADAYIL", "AATTAM", "AADUJEEVITHAM",
    "BRAMAYUGAM", "KISHKINDHA KAANDAM", "VARSHANGALKKU SHESHAM",
    "NAYATTU", "ANJAAM PATHIRAA", "TRAFFIC", "CLASSMATES",
    "THANMATRA", "AADU", "LEFT RIGHT LEFT", "ACTION HERO BIJU",
    "TAKE OFF", "RANAM", "MAHESHINTE PRATHIKAARAM",
    "CHOTTA MUMBAI", "BIG B", "RAJAMANIKYAM", "SPADIKAM",
    "NARAN", "MEESA MADHAVAN", "CID MOOSA", "GODFATHER",
    "MANICHITRATHAZHU", "THENKASHIPATTANAM", "VIKRAMADITHYAN",
    "RUNWAY", "PAVADA", "TWO COUNTRIES",
    "KADAL KADANNU ORU MATHUKUTTY", "SALT MANGO TREE",
    "CHANDUPOTTU"
]

play = "yes"

while play == "yes":

    movie = random.choice(movies)
    guessed = []
    chances = 6

    print("\nMALAYALAM MOVIE HANGMAN")

    while chances > 0:

        for letter in movie:
            if letter == " " or letter in guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        print()
        print("\n1. Guess a letter")
        print("2. Guess the full movie")

        choice = input("Choose 1 or 2: ")

        if choice == "1":

            guess = input("Enter a letter: ").upper()

            if len(guess) != 1:
                print("Enter only one letter!")

            elif guess in guessed:
                print("Already guessed!")

            elif guess in movie:
                guessed.append(guess)
                print("Correct guess!")

            else:
                guessed.append(guess)
                chances = chances - 1
                print("Wrong guess!")

        elif choice == "2":

            answer = input("Enter the movie name: ").upper()

            if answer == movie:
                print("Congratulations! You won!")
                print("Movie:", movie)
                break

            else:
                chances = chances - 1
                print("Wrong movie name!")

        else:
            print("Choose only 1 or 2!")

        if all(letter == " " or letter in guessed for letter in movie):
            print("Congratulations! You won!")
            print("Movie:", movie)
            break

        print("Chances left:", chances)

    else:
        print("\nGame over!")
        print("The movie was:", movie)

    play = input("\nPlay again? (yes/no): ").lower()

print("Thank you for playing!")
