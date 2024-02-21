import re

def funct_convertitoreIPA(testo_da_convertire):


    regex_parentesi = r"\<(.*?)\>|\((.*?)\)"  # provo ad eliminare dalla conversione il trascritto dell'adulto tra parentesi tonde e angolari

    if re.search(regex_parentesi, testo_da_convertire):
        testo_da_convertire = re.sub(regex_parentesi, "", testo_da_convertire)



    # VOCALI
    testo_da_convertire = testo_da_convertire.lower()
    testo_da_convertire = re.sub(r'\d+.', '', testo_da_convertire) # eliminazione di tutti i numeri più spazio
    testo_da_convertire = re.sub("c'ha", "ʧa", testo_da_convertire)
    testo_da_convertire = re.sub('\s\s+', ' ', testo_da_convertire) # rimozioni tripli e + spazi

    testo_da_convertire = testo_da_convertire.replace("’", "'")
    testo_da_convertire = testo_da_convertire.replace("un'", "un' ")
    testo_da_convertire = testo_da_convertire.replace("l'", "l' ")
    testo_da_convertire = testo_da_convertire.replace("'", "")


    testo_da_convertire = testo_da_convertire.replace("ò", "ɔ")
    testo_da_convertire = testo_da_convertire.replace("è", "ɛ")
    testo_da_convertire = testo_da_convertire.replace("ù", "u")
    testo_da_convertire = testo_da_convertire.replace("à", "a")
    testo_da_convertire = re.sub("peluche", "peluʃ", testo_da_convertire)
    testo_da_convertire = re.sub("fat:orja", "fat:o:ri:a", testo_da_convertire)
    testo_da_convertire = re.sub("hamburger", "amburger", testo_da_convertire)
    testo_da_convertire = re.sub(" jo", " i:o", testo_da_convertire)

    # GEMINATE
    testo_da_convertire = testo_da_convertire.replace("bb", "b:")
    testo_da_convertire = testo_da_convertire.replace("cce", "t:ʃe")
    testo_da_convertire = testo_da_convertire.replace("ccɛ", "t:ʃɛ")
    testo_da_convertire = testo_da_convertire.replace("gge", "d:ʒe")
    testo_da_convertire = testo_da_convertire.replace("ggɛ", "d:ʒɛ")
    testo_da_convertire = testo_da_convertire.replace("q", "c")

    # Allofoni
    testo_da_convertire = testo_da_convertire.replace("s[", "θ")
    testo_da_convertire = testo_da_convertire.replace("r[", "ʀ")

    testo_da_convertire = testo_da_convertire.replace(" /", "/")

    # cambio della precedente regola delle distorsioni con il simbolo dell'articolazione debole
    simbolo_articolazione_debole = chr(841)
    testo_da_convertire = testo_da_convertire.replace("^", simbolo_articolazione_debole)

    lista_fonemi = ["c", "g"]

    for fonema_target in lista_fonemi:
        rx = f"({fonema_target}{fonema_target})(i)([aeɛoɔu])"

        # parole come cacciavite aggiustare
        if fonema_target == "c":
            testo_da_convertire = re.sub(rx, r"t:ʃ\3", testo_da_convertire)
        elif fonema_target == 'g':
            testo_da_convertire = re.sub(rx, r"d:ʒ\3", testo_da_convertire)

        # esempi: pecche, pecca, , accordare, accòllo, accudire

        # Provo ad utilizzare un capturing group, per poi modificare solo questo e non la vocale
        rx = f"({fonema_target}{fonema_target})([haoɔu])"

        # Utilizzando $2 viene lasciato invariato il secondo gruppo, quindi le vocali
        if fonema_target == "c":
            testo_da_convertire = re.sub(rx, r"k:\2", testo_da_convertire)
        elif fonema_target == 'g':
            testo_da_convertire = re.sub(rx, r"g:\2", testo_da_convertire)
        



    for fonema_target in lista_fonemi:
        rx1 = f'({fonema_target})([haoɔu])'
        if fonema_target == 'c':
            testo_da_convertire = re.sub(rx1, r'k\2', testo_da_convertire)
        elif fonema_target == 'g':
            testo_da_convertire = re.sub(rx1, r'g\2', testo_da_convertire)

        rx1 = '([^s])(ci)([eɛaoɔu])'
        testo_da_convertire = re.sub(rx1, r'\1ʧ\3', testo_da_convertire)

        rx1 = '(c)(i)([haoɔu])'
        testo_da_convertire = re.sub(rx1, r'ʧ\3', testo_da_convertire)

        rx1 = '(g)(i)([haoɔu])'
        testo_da_convertire = re.sub(rx1, r'ʤ\3', testo_da_convertire)

        # rx1 = '(g)([ieɛ])'
        # testo_da_convertire = re.sub(rx1, r'ʤ\2', testo_da_convertire)

        rx1 = '(c)([^imeɛaoɔu])'
        testo_da_convertire = re.sub(rx1, r'k\2', testo_da_convertire)

        #_____________________________________________________________
        #REGOLE MANUALI DA MANTENERE
        testo_da_convertire = testo_da_convertire.replace('ci', 'ʧi')
        testo_da_convertire = testo_da_convertire.replace('ce', 'ʧe')
        testo_da_convertire = testo_da_convertire.replace('cɛ', 'ʧɛ')
        testo_da_convertire = testo_da_convertire.replace("c'e", "ʧe")
        testo_da_convertire = testo_da_convertire.replace("c'ɛ", "ʧɛ")

        #testo_da_convertire = testo_da_convertire.replace("gi", "ʤi")
        #testo_da_convertire = testo_da_convertire.replace("ge", "ʤe")
        #testo_da_convertire = testo_da_convertire.replace("gɛ", "ʤɛ")

        testo_da_convertire = testo_da_convertire.replace("sʧe", "ʃe")
        testo_da_convertire = testo_da_convertire.replace("sʧɛ", "ʃɛ")
        testo_da_convertire = testo_da_convertire.replace("sʧi", "ʃi")
        testo_da_convertire = testo_da_convertire.replace("sʧa", "ʃa")
        testo_da_convertire = testo_da_convertire.replace("sʧe", "ʃe")
        testo_da_convertire = testo_da_convertire.replace("sʧo", "ʃo")
        testo_da_convertire = testo_da_convertire.replace("sʧu", "ʃu")
        testo_da_convertire = testo_da_convertire.replace("sʧɛ", "ʃɛ")
        testo_da_convertire = testo_da_convertire.replace("sʧɔ", "ʃɔ")

        #_____________________________________________________________

        testo_da_convertire = testo_da_convertire.replace("dd", "d:")
        testo_da_convertire = testo_da_convertire.replace("ff", "f:")
        testo_da_convertire = testo_da_convertire.replace("gg", "g:")
        testo_da_convertire = testo_da_convertire.replace("ll", "l:")
        testo_da_convertire = testo_da_convertire.replace("mm", "m:")
        testo_da_convertire = testo_da_convertire.replace("nn", "n:")
        testo_da_convertire = testo_da_convertire.replace("pp", "p:")
        testo_da_convertire = testo_da_convertire.replace("rr", "r:")
        testo_da_convertire = testo_da_convertire.replace("ss", "s:")
        testo_da_convertire = testo_da_convertire.replace("tt", "t:")
        testo_da_convertire = testo_da_convertire.replace("vv", "v:")

        # testo_da_convertire = testo_da_convertire.replace("sc", "ʃ")
        rx1 = "([s])(ci)([eɛaoɔu])"
        testo_da_convertire = re.sub(rx1, r"ʃ\3", testo_da_convertire)

        rx1 = "([s])(c)([eɛ])"
        testo_da_convertire = re.sub(rx1, r"ʃ\3", testo_da_convertire)

        testo_da_convertire = testo_da_convertire.replace("zz", "ʦ")
        testo_da_convertire = testo_da_convertire.replace("z", "ʣ")
        testo_da_convertire = testo_da_convertire.replace("ì", "i")

        # NASALI
        # testo_da_convertire = testo_da_convertire.replace("nf", "ɱf")
        # testo_da_convertire = testo_da_convertire.replace("nf", "ɱv")
        # testo_da_convertire = testo_da_convertire.replace("mf", "ɱf")
        # testo_da_convertire = testo_da_convertire.replace("mv", "ɱv")
        testo_da_convertire = testo_da_convertire.replace("gn", "ɲ")
        testo_da_convertire = re.sub("gli ", "ʎi ", testo_da_convertire)
        testo_da_convertire = testo_da_convertire.replace("gli", "ʎ")


        # DITTONGHI E SEMIVOCALI
        testo_da_convertire = testo_da_convertire.replace("ia", "ja")
        testo_da_convertire = testo_da_convertire.replace("ie", "je")
        testo_da_convertire = testo_da_convertire.replace("iu", "ju")
        testo_da_convertire = testo_da_convertire.replace("ia", "ja")
        testo_da_convertire = testo_da_convertire.replace("io", "jo")

        testo_da_convertire = testo_da_convertire.replace("ua", "wa")
        testo_da_convertire = testo_da_convertire.replace("uo", "wo")
        testo_da_convertire = testo_da_convertire.replace("uɔ", "wɔ")
        testo_da_convertire = testo_da_convertire.replace("ue", "we")
        testo_da_convertire = testo_da_convertire.replace("uè", "wɛ")
        testo_da_convertire = testo_da_convertire.replace("ui", "wi")

        # CORREZIONI
        testo_da_convertire = testo_da_convertire.replace("ʃja", "ʃa")
        testo_da_convertire = testo_da_convertire.replace("ʃje", "ʃe")
        testo_da_convertire = testo_da_convertire.replace("ʃjo", "ʃo")
        testo_da_convertire = testo_da_convertire.replace("ʃju", "ʃu")

        testo_da_convertire = testo_da_convertire.replace("nʣj", "nʦj")
        testo_da_convertire = testo_da_convertire.replace("dʣi:", "ʣi:")

        # ECCEZIONI
        testo_da_convertire = testo_da_convertire.replace("anʣi", "anʦi")
        testo_da_convertire = testo_da_convertire.replace("anʣi", "anʦi")
        testo_da_convertire = testo_da_convertire.replace("lʣ", "lʦ")
        testo_da_convertire = testo_da_convertire.replace("aʣj", "aʦj")
        testo_da_convertire = testo_da_convertire.replace("ʤje", "ʤe")

        testo_da_convertire = testo_da_convertire.replace("ns", "nʦ")

        testo_da_convertire = testo_da_convertire.replace("d:ʒj", "d:ʒ")
        # testo_da_convertire = testo_da_convertire.replace("nc", "nk")

        testo_da_convertire = testo_da_convertire.replace(" ʣja ", " ʣi:a ")
        testo_da_convertire = testo_da_convertire.replace(" ʣjo ", " ʣi:o ")
        testo_da_convertire = testo_da_convertire.replace(" mja ", " mi:a ")
        testo_da_convertire = testo_da_convertire.replace(" twa ", " tu:a ")
        testo_da_convertire = testo_da_convertire.replace(" swa ", " su:a ")
        testo_da_convertire = testo_da_convertire.replace(" swo ", " su:o ")
        testo_da_convertire = testo_da_convertire.replace(" dwe ", " du:e ")
        testo_da_convertire = testo_da_convertire.replace(" lwi ", " lu:i ")

        testo_da_convertire = testo_da_convertire.replace("tS", "ʧ")
        testo_da_convertire = testo_da_convertire.replace("dG", "ʤ")
        testo_da_convertire = testo_da_convertire.replace("h", "")

        testo_da_convertire = testo_da_convertire.replace("'", "") # prima ELIMINATO PER CONSENTIRE LA SEGNALAZIONE DEGLI ACCENTI
        testo_da_convertire = testo_da_convertire.replace(",", "/")
        testo_da_convertire = testo_da_convertire.replace(".", "/")
        testo_da_convertire = testo_da_convertire.replace(" jo ", " io ")

        #Geminate intrinseche: i fonemi /ʃ/, /ɲ/, /ʎ/, /ʦ/ e /ʣ/ in posizione intervocalica e /ʦ/ tra una vocale e una semiconsonante
        #sono sempre realizzati concretamente come geminati.

        lista_fonemi = ["ʃ", "ɲ", "ʎ"]

        for fonema_target in lista_fonemi:
            rx = f'([aeɛijwoɔu]){fonema_target}([aeɛijwoɔu])'
            if fonema_target not in ["ʦ", "ʣ"]:
                testo_da_convertire = re.sub(rx, r'\1' + f'{fonema_target}' + r':\2', testo_da_convertire)

        fonemi_affr = ["ʦ", "ʣ"]

        for fonema_target in fonemi_affr:
            rx = f'([aeɛijwoɔu]){fonema_target}([aeɛijwoɔu])'
            if fonema_target == "ʦ":
                testo_da_convertire = re.sub(rx, r'\1t:s\2', testo_da_convertire)
            elif fonema_target == "ʣ":
                testo_da_convertire = re.sub(rx, r'\1d:z\2', testo_da_convertire)
        

        testo_da_convertire = testo_da_convertire.replace("ʧ", "ʧ")
        testo_da_convertire = testo_da_convertire.replace("dg", "ʤ")
        testo_da_convertire = testo_da_convertire.replace("ʣ", "ʣ")
        testo_da_convertire = testo_da_convertire.replace("ʦ", "ʦ")
        testo_da_convertire = testo_da_convertire.replace("à", "a")
        testo_da_convertire = testo_da_convertire.replace("à", "a")
        testo_da_convertire = testo_da_convertire.replace("ò", "o")
        testo_da_convertire = testo_da_convertire.replace("è", "e")
        testo_da_convertire = testo_da_convertire.replace("é", "e")
        testo_da_convertire = testo_da_convertire.replace("ì", "i")
        testo_da_convertire = testo_da_convertire.replace("ts", "ʦ")

    testo_da_convertire = testo_da_convertire.replace("$", "z")


    return testo_da_convertire
