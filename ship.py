import os, time, termios, tty, os, sys, random, writes, keyboard

def CharIn(pos:int) -> int:
	"""
		Linux terminál bemenet vizsgálat
		Visszaad egy kh nevű változót ami az aktuálisan leütött karakter (str)-ben,
	"""
	kh = ""
	try:
		if keyboard.is_pressed("a"):
			pos -= 1
		elif keyboard.is_pressed("d"):
			pos += 1
		time.sleep(0.025)
	except:
		pos = pos
	return pos

def Makeline():
	"""
		Sor készítése és akadály generálása random.
		Visszaad egy (int)-et mint lehetséges hibát (akadály helyét)
		és
		Visszaad egy (str)-t ami a  pálya texturáját takarja
	"""
	fail = random.randint(5,44)
	liner = ""	# Sor frissités defaul-ra
	for j in range(50):
                if j < 5:
                        liner += "\u001b[32m\u001b[42mF\u001b[0m"
                elif j == fail:
                        liner += "\u001b[40m\u001b[30mR\u001b[0m"
                elif j > 44:
                        liner += "\u001b[32m\u001b[42mF\u001b[0m"
                else:
                        liner += "\u001b[34m\u001b[44mV\u001b[0m"
	return int(fail), str(liner)

def Test(pos:int, lines:dict, pont:int, name:str) -> int:
	"""
		Ez figyeli, hogy a játékos belmegy-e az akadálybam illetve, hogy kimegye a játékterületről.
		pos ("Pozició") (int) értékét kapja meg
		és
		pont ("Pontszám") (int) értéket kapja meg
		és
		lines ("Sorok") (dict) értékét kapja meg
		ellenőrzés céljából
		Visszaadja a műveletek elvégzését követően a pont változó értékét (int)-ben.
	"""
	if pos < 5 or pos > 44 or pos == lines["0f"]:
		time.sleep(1)
		writes.ShipEnd(pont, name)
	else:
                 pont += 1
	return pont

def Makeline2(pos:int, lines:dict, line):
	"""
		Létrehozza a sort amelyen a játékos mozog.
		pos (int), lines (dict), line (str) váltózók felhasználásával.
	"""
	for i in range(50):
                if i < 5:
                        line += "\u001b[32m\u001b[42mF\u001b[0m"
                elif i == pos:
                        line += "\u001b[41m\u001b[31mR\u001b[0m"
                elif i == lines["0f"]:
                        line += "\u001b[30m\u001b[40mO\u001b[0m"
                elif i > 44:
                        line += "\u001b[32m\u001b[42mF\u001b[0m"
                else:
                        line += "\u001b[34m\u001b[44mV\u001b[0m"
	print(line)

def ClearRows(liner:str) -> str:
	"""
		Legenerálja az akadálymentes sort
		liner (str) felhasználásával.
		Visszaadja a liner módosított változatát.
	"""
	for i in range(50):
		if i < 5:
			liner += "\u001b[32m\u001b[42mF\u001b[0m"
		elif i > 44:
			liner += "\u001b[32m\u001b[42mF\u001b[0m"
		else:
			liner += "\u001b[34m\u001b[44mV\u001b[0m"
	return str(liner)

def Game(name:str):
	"""
		A játékprogram MAIN része
		name (str) változót kapja meg.
	"""
	lines = {"0":"", "0f":"", "1":"", "1f":"", "2":"", "2f":"", "3":"", "3f":"", "4":"", "4f":"", "5":"", "5f":"", "6":"", "6f":"", "7":"", "7f":"", "8":"", "8f":"", "9":"", "9f":""}
	is_name = False
	pont = 0
	pos = 24
	first = True
	while True:
		line = ""
		os.system("clear")
		writes.Behuzas()
		print("\n\nJátékos: " + name + "   Pont:" + str(pont) + "\n")
		int(pont)
		pos = CharIn(pos)
		writes.Behuzas()
		Makeline2(pos, lines, line)
		if first == True:
			for i in range(10):
				liner = ""
				liner = ClearRows(liner)
				writes.Behuzas()
				print(liner)
				lines[str(i)] = liner
				int(i)
			first = False
		else:
			for i in range(9):
				lines[str(i)] = lines[str(i+1)]
				lines[str(i) + "f"] = lines[str(i+1) + "f"]
			lines[str(9) + "f"], lines[str(9)] = Makeline()
			for i in range(10):
				writes.Behuzas()
				print(lines[str(i)])
		pos = CharIn(pos)
		pont = Test(pos, lines, pont, name)
		for i in range(0,10):
			time.sleep(0.025)
			pos = CharIn(pos)
