def hb2u():
    return "Happy Birthday to you!\n"

def verseFor(name):
    lyrics = hb2u() * 2 + "Happy Birthday, dear " + name + ".\n" + hb2u()
    return lyrics

def main():
    outfile = open("HappyBirthday.txt", "w")
    person = input("What is the birthday person's name? ")
    print(verseFor(person), file=outfile)
    outfile.close()
main()