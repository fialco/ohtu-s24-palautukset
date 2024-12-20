from luoja import luo_peli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        tyyppi = input()
        peli = luo_peli(tyyppi)

        if peli:
            peli.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
