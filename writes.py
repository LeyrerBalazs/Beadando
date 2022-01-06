import os

def Behuzas():
	print("                  ", end="")

def Menu():
	os.system("clear")
	print("\n\n")
	Behuzas()
	print("\u001b[42m                               \u001b[0m")
	Behuzas()
	print("\u001b[42m  \u001b[0m                           \u001b[42m  \u001b[0m")
	Behuzas()
	print("\u001b[42m  \u001b[0m       \u001b[37m1. Jatek            \u001b[42m  \u001b[0m")
	Behuzas()
	print("\u001b[42m  \u001b[0m       \u001b[37m2. Pontok           \u001b[42m  \u001b[0m")
	Behuzas()
	print("\u001b[42m  \u001b[0m       \u001b[37m3. Kilépés          \u001b[42m  \u001b[0m")
	Behuzas()
	print("\u001b[42m  \u001b[0m                           \u001b[42m  \u001b[0m")
	Behuzas()
	print("\u001b[42m                               \u001b[0m")
	print("")
	
def Stats():
        os.system("clear")
        print("\n\n")
        Behuzas()
        print("\u001b[42m                               \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m\u001b[37mNév         \u001b[42m  \u001b[0m\u001b[37mPont         \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m                               \u001b[0m")
        with open("score.json", encoding="utf-8") as f:
                data = json.load(f)
        for element in data:
                Behuzas()
                print("\u001b[42m  \u001b[0m\u001b[31m " + element["nev"], end="")
                for i in range(11 - len(element["nev"])):
                        print("\u001b[0m \u001b[0m", end="")
                print("\u001b[42m  \u001b[0m\u001b[31m " + str(element["pontja"]), end="")
                for i in range(12 - len(str(element["pontja"]))):
                        print("\u001b[0m \u001b[0m", end="")
                print("\u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m                               \u001b[0m")
        print("")
        Behuzas()
        input("Tovább...")
        os.system("python3 main.py")
        exit()

def ShipEnd(pont:int, name:str):
        if pont < 10:
                kiirott = "000" + str(pont)
        elif pont < 100:
                kiirott = "00" + str(pont)
        elif pont < 1000:
                kiirott = "0" + str(pont)
        else:
                kiirott = str(pont)
        os.system("clear")
        print("\n\n")
        Behuzas()
        print("\u001b[42m                                                    \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m                                                \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m Gratulálok! " + kiirott + " pontot szereztél!             \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m Játék vége.                                    \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m                                                \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m                                                    \u001b[0m")
        Behuzas()
        input("Tovább...")
        van = False
        os.system("python3 main.py")
        with open("score.json", encoding="utf-8") as f:
                data = json.load(f)
        for i in range(len(data)):
                if data[i]["nev"] == name:
                        van = True
                        data[i]["pontja"] = pont
        if van == False:
                newuser = {"nev":name, "pontja": pont}
                data.append(newuser)
        with open("score.json", "w",  encoding="utf-8") as f:
    		json.dump(data, f)
        exit()
