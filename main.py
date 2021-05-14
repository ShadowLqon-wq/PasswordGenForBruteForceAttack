import secrets
def main():
    outfile = open("gen.txt", "a")
    outfile.write(str(pw) + "\n")
    outfile.close()
pw = ""
zeichen = "abcdefghijklmnopQrstUvWxyzABCDEFGHIJKLMNOPGQRSTUVWXYZ2143346689809ß_"
länge = 7
länge1 = 6
länge2 = 8
länge3 = 7
länge4 = 9
länge5 = 8
länge6= 7
länge7 = 8
länge8 = 9
länge9 = 12
länge10 = 11
länge11 = 10
länge12 = 14
länge13 = 13
länge14 = 16
länge15 = 15


#Must Do : While Schleife

#Gen _________________________________
while 1:
    for _ in range(länge):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge1):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge2):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge3):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge4):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge5):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge6):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge7):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge8):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge9):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge10):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge11):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge12):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge13):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge14):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""
    for _ in range(länge15):
        pw = pw + secrets.choice(zeichen)
    main()
    print(pw)
    pw = ""

#End ________________________________________

