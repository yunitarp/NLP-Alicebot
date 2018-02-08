import re

answer = raw_input("Alice\t>> Halo, Namaku Alice nama kamu siapa?\n\nKamu\t>> ")
while True:
	patternlist = [
		re.match(".* +.*",answer),
		re.match("([Hh]ai )?([nN]amaku |[nN]ama saya )(\w+)",answer)
	]
	if patternlist[1]:
		nama = str(patternlist[1].group(3))
		answer = raw_input("Alice\t>> Hi "+nama+", Ada apa?\n\nKamu\t>> ")
		break
	elif patternlist[0]:
		answer = raw_input("Alice\t>> Nama panggilan ajaa jangan panjang-panjang, apa itu bukan nama kamu?\nAku gamau ngobrol kalau belum kenalan :(\n\nKamu\t>> ")
	else:
		nama = answer
		answer = raw_input("Alice\t>> Hi "+nama+", Ada apa?\n\nKamu\t>> ")
		break

before = ""
while True:
	patternlist = [
		re.match("^([A-Za-z0-9.,?]*)$",answer), #0
		re.match("(.* )*(.+)(nya| yang) enak.*\?$",answer), #1
		re.match("(.* )*(.+)(nya| yang) enak.*[^?]$",answer), #2
		re.match(".*kamu.*laper.*\?$",answer), #3
		re.match("(.*laper.*[^?]$|.*laper)",answer), #4
		re.match("([Ii]ya.*|ya.*|[yY])",answer), #5
		re.match("([Ee]ngga.*|[Gg]ak.*|Tidak.*)",answer), #6
		re.match(".*(harga|murah|mahal).*\?$",answer), #7
		re.match(".*([Ee]ngga|[Tt]idak|[Gg]ak).*enak.*",answer), #8
		re.match("(.*enak.*[^?]$|.*enak)",answer), #9
		re.match(".*enak.*\?$",answer), #10
		re.match(".* ?(banyak|sedikit) ?.* ?porsi ?.*\?$",answer), #11
		re.match(".* ?porsi ?.* ?(banyak|sedikit) ?.*\?$",answer), #12
		re.match(".* ?(banyak|sedikit) ?.* ?porsi ?.*[^?]$",answer), #13
		re.match(".* ?porsi ?.* ?(banyak|sedikit) ?.*[^?]$",answer), #14
		re.match(".* ?(makan)?.*(dimana|apa).*\?$",answer), #15
		re.match(".*(dimana|apa).* ?(makan)?.*\?$",answer), #16
		re.match(".*suka.*\?$",answer), #17
		re.match("(.*suka.*[^?]$|.*suka)",answer) #18
	]
	if patternlist[5] or patternlist[4]:
		if before == "laper" or patternlist[4]	:
			string = "Yuk makan bareng"
		else:
			string = "Iya apa? aku belum nanya apa-apa kok -_-"
	elif patternlist[6]:
		if before == "laper":
			before = "kenyang"
			string = "Kenyang makan apa?"
		else:
			string = "Engga apa? aku belum nanya apa-apa kok -_-"
	elif patternlist[17]:
		string = "aku suka makan apa aja, hobiku kan makan hehe, kamu suka makan apa?"
	elif patternlist[18]:
		string = "haha aku juga suka itu, enak soalnya, kamu biasanya makan dimana?"
	elif patternlist[1]:
		makanan = str(patternlist[1].group(2)).lower()
		if makanan == 'bakso':
			string = 'Bakso boedjangan tuh enak, tempatnya di jl.soekarno hatta'
		elif makanan == 'sate':
			string = 'Sate sukapura tuh enak, tempatnya di jl.sukapura looh'
		else:
			string = "hmm, kayanya di bakso amin enak"
	elif patternlist[2]:
		string = "Iya tau, disana "+patternlist[2].group(2)+"nya enak, aku suka makan disana"
	elif patternlist[3]:
		string = "Engga terlalu, aku udah makan tadi. Kamu laper?"
		before = "laper"
	elif patternlist[7]:
		string = "Wah gatau kalau sekarang, harganya berubah-ubah"
	elif patternlist[8]:
		before = "gak enak"
		string = "Oh iya? Kamu emang biasanya makan dimana kasih tau dong"
	elif patternlist[11] or patternlist[12]:
		string = "Hmm.. Makan di hanamasa sanah, mahal sih, tapi All you can eat looh"
	elif patternlist[13] or patternlist[14]:
		string = "Beneran? wah ikut ikut aku suka makan banyak"
	elif patternlist[15] or patternlist[16]:
		string = "Gak tau banyak si aku, tpi di seblak deket kos ku tuuh, 7rban banyak enak lagi, lumayan bisa buat makan gede juga hehe"
	elif patternlist[10]:
		string = "Gak tau tuh sekarang masih enak apa engga"
	elif patternlist[9]:
		string = "beneran? kapan-kapan aku dibawain dong :D"
	elif patternlist[0]:
		string = answer+"? itu enak ngga?"
	else:
		if before == "gak enak":
			string = "Ohh, oke nanti aku coba cari terus cicipin :D"
		else:
			string = "Hmm.. kayanya aku mulai lapar nih jadi ngga nyambung, kamu laper ngga?"
	string = "Alice\t>> "+string+"\n\nKamu\t>> "
	answer = raw_input(string)