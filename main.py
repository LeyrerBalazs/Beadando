import writes, os, ship

def main():
        while True:
                writes.Menu()
                writes.Behuzas()
                valasz = input("A választás száma: ")
                length = 100
                elso = True
                if valasz == "1":
                        while length > 9:
                                if elso:
                                        elso =  False
                                else:
                                        writes.Behuzas()
                                        print("Túl hosszú név!")
                                writes.Behuzas()
                                name = input("Add meg a neved!: ")
                                length = len(name)
                        ship.Game(name)
                elif valasz == "2":
                        writes.Stats()
                elif valasz == "3":
                        os.system("clear")

if __name__ == "__main__":
        main()
