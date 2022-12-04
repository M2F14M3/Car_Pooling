############################ - Import
import mysql.connector as db
import datetime as dt


############################ - Management Code
def menu(messaggio, min, max):
    print(messaggio)
    scelta = int(input("Inserire la scelta: "))
    while (scelta < min or scelta > max):
        scelta = int(
            input("La scelta inserita non è valida" + "\n" + messaggio +
                  "\nInserire la scelta: "))
    return scelta


def checkLen(messaggio, max_len, messaggio_err):
    value = input(messaggio)
    while (len(value) > max_len):
        value = input(messaggio_err + "\n" + messaggio)
    return value


def checkData(messaggio, format, messaggio_err):
    controllo = False
    value = input(messaggio)
    while (True):
        try:
            value = dt.datetime.strptime(value, format)
            return value
        except:
            value = input(messaggio_err + "\n" + messaggio)


def checkTime(messaggio, format, messaggio_err):
    controllo = False
    value = input(messaggio)
    while (True):
        try:
            value = dt.datetime.strptime(value, format).strftime(format)
            return value
        except:
            value = input(messaggio_err + "\n" + messaggio)


def checkFloat(messaggio, messaggio_err):
    controllo = False
    value = input(messaggio)
    while (True):
        try:
            value = float(value)
            return value
        except:
            value = input(messaggio_err + "\n" + messaggio)


############################ - Database Management
def dbConnection():
    try:
        cnx = db.connect(host="127.0.0.1",
                         port="3306",
                         user="root",
                         password="",
                         database="car_pooling")
        print("Connessione effettuata")
        return cnx
    except:
        print("Connessione fallita")
    return None


def dbClose(cnx):
    cnx.close()


############################ - Insert Data
def inserimento_db(cnx, cur, scelta):
    if (scelta == 1):
        InsertDatiViaggio(cnx, cur)
    elif (scelta == 2):
        InsertDatiAutista(cnx, cur)
    elif (scelta == 3):
        InsertDatiAuto(cnx, cur)
    elif (scelta == 4):
        InsertDatiPasseggero(cnx, cur)
    elif (scelta == 5):
        InsertDatiPrenotazione(cnx, cur)
    elif (scelta == 6):
        InsertDatiFeedbackPasseggero(cnx, cur)
    else:
        InsertDatiFeedbackAutista(cnx, cur)


def InsertDatiViaggio(cnx, cur):
    id_autista = input("Inserire id autista: ")
    citta_partenza = checkLen("Inserire citta di partenza(max 20 chars): ", 20,
                              "La lunghezza massima è stata superata")
    data_partenza = checkData("Inserire data di partenza(yyyy-mm-dd): ",
                              "%Y-%m-%d", "Il formato inserito non è valido")
    ora_partenza = checkTime("Inserire orario di partenza(HH:MM): ", "%H:%M",
                             "Il formato inserito non è valido")
    citta_destinazione = checkLen(
        "Inserire citta di destinazione(max 20 chars): ", 20,
        "La lunghezza massima è stata superata")
    durata_viaggio = checkTime("Inserire durate del viaggio(HH:MM): ", "%H:%M",
                               "Il formato inserito non è valido")
    prezzo_pass = checkFloat(
        "Inserire prezzo per ogni passeggero(euro.centesimi o euro): ",
        "Il formato inserito non è valido")
    sql_query = "INSERT INTO viaggio (id_viaggio, id_autista, data_partenza, ora_partenza, citta_partenza, citta_destinazione, durata_viaggio, prezzo_passeggero, prenotazione) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, DEFAULT)"
    val = (id_autista, data_partenza, ora_partenza, citta_partenza,
           citta_destinazione, durata_viaggio, prezzo_pass)
    cur.execute(sql_query, val)
    cnx.commit()


def InsertDatiAutista(cnx, cur):
    nome = checkLen("Inserire il nome(max 20 chars): ", 20,
                    "La lunghezza massima è stata superata")
    cognome = checkLen("Inserire il cognome(max 20 chars): ", 20,
                       "La lunghezza massima è stata superata")
    data_nascita = checkData("Inserire data di nascita(yyyy-mm-dd): ",
                             "%Y-%m-%d", "Il formato inserito non è valido")
    sesso = checkLen("Inserire il sesso(max 10 chars): ", 10,
                     "La lunghezza massima è stata superata")
    num_patente = checkLen("Inserire il codice della patente(max 10 chars): ",
                           10, "La lunghezza massima è stata superata")
    scad_patente = checkData(
        "Inserire data della scadenza della patente(yyyy-mm-dd): ", "%Y-%m-%d",
        "Il formato inserito non è valido")
    num_tel = checkLen("Inserire il numero di telefono: ", 15,
                       "La lunghezza massima è stata superata")
    email = checkLen("Inserire l'indirizzo mail: ", 40,
                     "La lunghezza massima è stata superata")
    sql_insert = "INSERT INTO autista (id_autista, nome, cognome, data_nascita, sesso, num_patente, scad_patente, num_telefono, dati_auto, email) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, NULL, %s)"
    val = (nome, cognome, data_nascita, sesso, num_patente, scad_patente,
           num_tel, email)
    cur.execute(sql_insert, val)
    cnx.commit()


def InsertDatiAuto(cnx, cur):
    codice_auto = checkLen("Inserire codice auto(max 10 chars): ", 10,
                           "La lunghezza massima è stata superata")
    marca = checkLen("Inserire la marca(max 15 chars): ", 15,
                     "La lunghezza massima è stata superata")
    modello = checkLen("Inserire il modello(max 15 chars): ", 15,
                       "La lunghezza massima è stata superata")
    num_posti = input("Inserire numero posti: ")
    targa = checkLen("Inserire la targa(max 10 chars): ", 10,
                     "La lunghezza massima è stata superata")
    colore = checkLen("Inserire il colore(max 15 chars): ", 15,
                      "La lunghezza massima è stata superata")
    sql_insert = "INSERT INTO automobile (codice_auto, targa, num_posti, marca, modello, colore) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (codice_auto, targa, num_posti, marca, modello, colore)
    cur.execute(sql_insert, val)
    cnx.commit()


def InsertDatiPasseggero(cnx, cur):
    cf = checkLen("Inserire il codice fiscale(max 16 chars): ", 16,
                  "La lunghezza massima è stata superata")
    nome = checkLen("Inserire nome(max 20 chars): ", 20,
                    "La lunghezza massima è stata superata")
    cognome = checkLen("Inserire il cognome(max 20 chars): ", 20,
                       "La lunghezza massima è stata superata")
    num_tel = checkLen("Inserire il numero di telefono(max 15 chars): ", 15,
                       "La lunghezza massima è stata superata")
    codice_documento = checkLen(
        "Inserire il codice del documento(max 10 chars): ", 10,
        "La lunghezza massima è stata superata")
    mail = checkLen("Inserire indirizzo mail(max 40 chars): ", 40,
                    "La lunghezza massima è stata superata")
    sql_insert = "INSERT INTO passeggero (cf, nome, cognome, num_telefono, codice_documento, email) VALUE (%s, %s, %s, %s, %s, %s)"
    val = (cf, nome, cognome, num_tel, codice_documento, mail)
    cur.execute(sql_insert, val)
    cnx.commit()


def InsertDatiPrenotazione(cnx, cur):
    id_viaggio = input("Inserire l'ide viaggio")
    cf = checkLen("Inserire il codice fiscale(max 16 chars): ", 16,
                  "La lunghezza massima è stata superata")
    sql_insert = "INSERT INTO prenotazione (codice, id_viaggio, cf, risposta) VALUES (NULL, %s, %s, NULL)"
    val = (id_viaggio, cf)
    cur.execute(sql_insert, val)


def InsertDatiFeedbackPasseggero(cnx, cur):
    id_autista = input("Inserire l'id autista: ")
    cf = checkLen("Inserire il proprio codice fiscale(max 16 chars): ", 16,
                  "La lunghezza massima è stata superata")
    valutazione = checkFloat(
        "Inserire la valutazione(numeri interi o con .5): ",
        "Il valore inserito non è valido: ")
    while (valutazione % 0.5 == False and valutazione > 5 or valutazione < 0):
        valutazione = checkFloat(
            "Inserire la valutazione(numeri interi o con .5): ",
            "Il valore inserito non è valido: ")
    feedback = checkLen("Inserire la valutazione(da 0 a 100 chars): ", 100,
                        "la lunghezza massima è stata superata")
    sql_insert = "INSERT INTO feedback_passeggero (id_feedback, id_autista, cf, valutazione, feedback) VALUES (NULL, %s, %s, %s, %s)"
    val = (id_autista, cf, valutazione, feedback)
    cur.execute(sql_insert, val)
    cnx.commit()


def InsertDatiFeedbackAutista(cnx, cur):
    cf = checkLen("Inserire il proprio codice fiscale(max 16 chars): ", 16,
                  "La lunghezza massima è stata superata")
    id_autista = input("Inserire l'id autista: ")
    valutazione = checkFloat(
        "Inserire la valutazione(numeri interi o con .5): ",
        "Il valore inserito non è valido: ")
    while (valutazione % 0.5 == False and valutazione > 5 or valutazione < 0):
        valutazione = checkFloat(
            "Inserire la valutazione(numeri interi o con .5): ",
            "Il valore inserito non è valido: ")
    feedback = checkLen("Inserire la valutazione(da 0 a 100 chars): ", 100,
                        "la lunghezza massima è stata superata")
    sql_insert = "INSERT INTO feedback_passeggero (id_feedback, cf, id_autista, valutazione, feedback) VALUES (NULL, %s, %s, %s, %s)"
    val = (cf, id_autista, valutazione, feedback)
    cur.execute(sql_insert, val)
    cnx.commit()


############################ - Read Data
def visualizzazione_db(cur, scelta_ins):
    if (scelta_ins == 1):
        printDatiViaggio(cur)
    elif (scelta_ins == 2):
        printDatiAutista(cur)
    elif (scelta_ins == 3):
        printDatiAuto(cur)
    elif (scelta_ins == 4):
        printDatiPasseggero(cur)
    elif (scelta_ins == 5):
        printDatiPrenotazioni(cur)
    elif (scelta_ins == 6):
        printDatiFeedbackPasseggero(cur)
    else:
        printDatiFeedbackAutista(cur)


def printDatiViaggio(cur):
    sql_query = "SELECT * FROM viaggio"
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Id viaggio: " + str(dato[0]) + " Id autista: " +
                  str(dato[1]) + " Citta partenza: " + str(dato[4]) +
                  " Data partenza: " + str(dato[2]) + " Ora partenza: " +
                  str(dato[3]) + " Citta destinazione: " + str(dato[5]) +
                  " Durata viaggio: " + str(dato[6]) +
                  " Prezzo per passeggero: " + str(dato[7]) +
                  " € Prenotazione disponibile(0 = No, 1 = Sì): " +
                  str(dato[8]))
    else:
        print("Non sono presenti viaggi nel db")


def printDatiAutista(cur):
    sql_query = "SELECT * FROM autista"
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Id autista: " + str(dato[0]) + " Nome: " + str(dato[1]) +
                  " Cognome: " + str(dato[2]) + " Data nascita: " +
                  str(dato[3]) + " Sesso: " + str(dato[4]) + " Num patente: " +
                  str(dato[5]) + " Scadenza patente: " + str(dato[6]) +
                  " Num tel: " + str(dato[7]) + " Mail: " + str(dato[9]))
    else:
        print("Non sono presenti autisti nel db")


def printDatiAuto(cur):
    sql_query = "SELECT * FROM automobile"
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Codice auto: " + str(dato[0]) + " Marca: " + str(dato[3]) +
                  " Modello: " + str(dato[4]) + " Numero posti: " +
                  str(dato[2]) + " Targa: " + str(dato[1]) + "Colore: " +
                  str(dato[5]))
    else:
        print("Non sono presenti autisti nel db")


def printDatiPasseggero(cur):
    sql_query = "SELECT * FROM passeggero"
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Codice fiscale: " + str(dato[0]) + " Nome: " +
                  str(dato[1]) + " Cognome: " + str(dato[2]) +
                  " Numero telefono: " + str(dato[3]) + " Codice documento: " +
                  str(dato[4]) + " Mail: " + str(dato[5]))
    else:
        print("Non sono presenti passeggeri nel db")


def printDatiPrenotazioni(cur):
    sql_query = "SELECT * FROM prenotazione"
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Codice prenotazione: " + str(dato[0]) + " Id viaggio: " +
                  str(dato[1]) + " Codice fiscale passeggero: " +
                  str(dato[2]) + " Risposta prenotazione: " + str(dato[3]))
    else:
        print("Non sono presenti prenotazioni nel db")


def printDatiFeedbackPasseggero(cur):
    sql_query = "SELECT * FROM feedback_passeggero"
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Id feedback: " + str(dato[0]) +
                  " Autista che ha dato il feedback: " + str(dato[1]) +
                  " Utente verso il quale è stato dato il feedback: " +
                  str(dato[2]) + " Valutazione: " + str(dato[3]) +
                  " Descrizione: " + str(dato[4]))
    else:
        print("Non sono presenti feedback fatti dagli autisti nel db")


def printDatiFeedbackAutista(cur):
    sql_query = "SELECT * FROM feedback_autista"
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Id feedback: " + str(dato[0]) +
                  " Utente che ha dato il feedback: " + str(dato[1]) +
                  " Autista verso il quale è stato dato il feedback: " +
                  str(dato[2]) + " Valutazione: " + str(dato[3]) +
                  " Descrizione: " + str(dato[4]))
    else:
        print("Non sono presenti feedback fatti dagli utenti nel db")


############################ - Update Data
def update_db(cnx, cur, scelta):
    if (scelta == 1):
        scelta_viaggio = input("Inserire l'id del viaggio dal modificare: ")
        sql_check = "SELECT * FROM viaggio WHERE id_viaggio=%s" % (
            scelta_viaggio)
        cur.execute(sql_check)
        if (len(cur.fetchall()) != 0):
            scelta = menu(
                "1 - Modificare la data di partenza" +
                "\n2 - Modificare l'orario di partenza" +
                "\n3 - Modificare la citta di partenza" +
                "\n4 - Modificare la citta di destinazione" +
                "\n5 - Modificare durata viaggio" +
                "\n6 - Modificare prezzo per passeggero" + "\n7 - Exit", 1, 7)
            UpdateDatiViaggio(cnx, cur, scelta, id)
        else:
            print("L'id inserito non è valido")
    elif (scelta == 2):
        scelta_autista = input("Inserire l'id dell'autista dal modificare: ")
        sql_check = "SELECT * FROM autista WHERE id_autista=%s" % (
            scelta_autista)
        cur.execute(sql_check)
        if (len(cur.fetchall()) != 0):
            scelta = menu(
                "1 - Modificare la data di scandenza della patente" +
                "\n2 - Modificare il numero di telefono" + "\n3 - Exit", 1, 3)
            UpdateDatiAutista(cnx, cur, scelta, id)
        else:
            print("L'id inserito non è valido")
    elif (scelta == 3):
        scelta_auto = input("Inserire codice auto dal modificare: ")
        sql_check = "SELECT * FROM automobile WHERE codice_auto=%s" % (
            scelta_auto)
        cur.execute(sql_check)
        if (len(cur.fetchall()) != 0):
            scelta = menu(
                "1 - Modificare la targa" + "\n2 - Modificare il colore" +
                "\n3 - Exit", 1, 3)
            UpdateDatiAuto(cnx, cur, scelta, id)
        else:
            print("L'id inserito non è valido")
    elif (scelta == 4):
        scelta_passeggero = input("Inserire codice fiscale dal modificare: ")
        sql_check = "SELECT * FROM passeggero WHERE cf=%s" % (
            scelta_passeggero)
        cur.execute(sql_check)
        if (len(cur.fetchall()) != 0):
            scelta = menu(
                "1 - Modificare il numero di telefono" +
                "\n2 - Modificare il codice del documento" + "\n3 - Exit", 1,
                3)
            UpdateDatiPasseggero(cnx, cur, scelta, id)
        else:
            print("L'id inserito non è valido")
    elif (scelta == 5):
        scelta_prenotazione = input(
            "Inserire codice prenotazione da modificare: ")
        sql_check = "SELECT * FROM prenotazione WHERE codice=%s" % (
            scelta_passeggero)
        cur.execute(sql_check)
        if (len(cur.fetchall()) != 0):
            scelta = menu(
                "1 - Modificare il passeggero" +
                "\n2 - Modificare la risposta" + "\n3 - Exit", 1, 3)
            UpdateDatiPrenotazione(cnx, cur, scelta, id)
        else:
            print("L'id inserito non è valido")
    elif (scelta == 6):
        scelta_feedback = input("Inserire l'id feedback da modificare: ")
        sql_check = "SELECT * FROM feedback_passeggero WHERE id_feedback=%s" % (
            scelta_feedback)
        cur.execute(sql_check)
        if (len(cur.fetchall()) != 0):
            scelta = menu(
                "1 - Modificare la valutazione" +
                "\n2 - Modificare il feedback" + "\n3 - Exit", 1, 3)
            UpdateDatiFeedbackPasseggero(cnx, cur, scelta, id)
        else:
            print("L'id inserito non è valido")
    else:
        scelta_feedback = input("Inserire l'id feedback da modificare: ")
        sql_check = "SELECT * FROM feedback_autista WHERE id_feedback=%s" % (
            scelta_feedback)
        cur.execute(sql_check)
        if (len(cur.fetchall()) != 0):
            scelta = menu(
                "1 - Modificare la valutazione" +
                "\n2 - Modificare il feedback" + "\n3 - Exit", 1, 3)
            UpdateDatiFeedbackAutista(cnx, cur, scelta, id)
        else:
            print("L'id inserito non è valido")


def modificaDataPartenza(cnx, cur, id):
    data_partenza = checkData("Inserire data di partenza(yyyy-mm-dd): ",
                              "%Y-%m-%d", "Il formato inserito non è valido")
    sql_update = "UPDATE viaggio SET data_partenza=%s WHERE id_viaggio=%s"
    val = (data_partenza, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaOrarioPartenza(cnx, cur, id):
    orario_partenza = checkTime("Inserire orario di partenza(HH:MM): ",
                                "%H:%M", "Il formato inserito non è valido")
    sql_update = "UPDATE viaggio SET ora_partenza=%s WHERE id_viaggio=%s"
    val = (orario_partenza, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaCittaPartenza(cnx, cur, id):
    citta_partenza = checkLen("Inserire citta di partenza(max 20 chars): ", 20,
                              "La lunghezza massima è stata superata")
    sql_update = "UPDATE viaggio SET citta_partenza=%s WHERE id_viaggio=%s"
    val = (citta_partenza, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaCittaDestinazione(cnx, cur, id):
    citta_destinazione = checkLen(
        "Inserire citta di destinazione(max 20 chars): ", 20,
        "La lunghezza massima è stata superata")
    sql_update = "UPDATE viaggio SET citta_destinazione=%s WHERE id_viaggio=%s"
    val = (citta_destinazione, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaDurataViaggio(cnx, cur, id):
    durata_viaggio = checkTime("Inserire durata del viaggio(HH:MM): ", "%H:%M",
                               "Il formato inserito non è valido")
    sql_update = "UPDATE viaggio SET durata_viaggio=%s WHERE id_viaggio=%s"
    val = (durata_viaggio, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaPrezzoPasseggero(cnx, cur, id):
    prezzo_passeggero = checkFloat(
        "Inserire prezzo per ogni passeggero(euro.centesimi o euro): ",
        "Il formato inserito non è valido")
    sql_update = "UPDATE viaggio SET prezzo_passeggero=%s WHERE id_viaggio=%s"
    val = (prezzo_passeggero, id)
    cur.execute(sql_update, val)
    cnx.commit()


def UpdateDatiViaggio(cnx, cur, scelta, id):
    if (scelta == 1):
        modificaDataPartenza(cnx, cur, id)
    elif (scelta == 2):
        modificaOrarioPartenza(cnx, cur, id)
    elif (scelta == 3):
        modificaCittaPartenza(cnx, cur, id)
    elif (scelta == 4):
        modificaCittaDestinazione(cur, cnx, id)
    elif (scelta == 5):
        modificaDurataViaggio(cnx, cur, id)
    else:
        modificaPrezzoPasseggero(cnx, cur, id)


def modificaScadenzaPatente(cnx, cur, id):
    scad_patente = checkData("Inserire data scadenza patente(yyyy-mm-dd): ",
                             "%Y-%m-%d", "Il formato inserito non è valido")
    sql_update = "UPDATE autista SET scad_patente=%s WHERE id_autista=%s"
    val = (scad_patente, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaNumTelefonoAutista(cnx, cur, id):
    num_telefono = checkLen("Inserire il numero di telefono: ", 15,
                            "La lunghezza massima è stata superata")
    sql_update = "UPDATE autista SET num_telefono=%s WHERE id_autista=%s"
    val = (num_telefono, id)
    cur.execute(sql_update, val)
    cnx.commit()


def UpdateDatiAutista(cnx, cur, scelta, id):
    if (scelta == 1):
        modificaScadenzaPatente(cnx, cur, id)
    else:
        modificaNumTelefonoAutista(cnx, cur, id)


def modificaTarga(cnx, cur, id):
    targa = checkLen("Inserire la targa(max 10 chars): ", 10,
                     "La lunghezza massima è stata superata")
    sql_update = "UPDATE automobile SET targa=%s WHERE codice_auto=%s"
    val = (targa, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaColore(cnx, cur, id):
    colore = checkLen("Inserire il colore(max 15 chars): ", 15,
                      "La lunghezza massima è stata superata")
    sql_update = "UPDATE automobile SET colore=%s WHERE codice_auto=%s"
    val = (colore, id)
    cur.execute(sql_update, val)
    cnx.commit()


def UpdateDatiAuto(cnx, cur, scelta, id):
    if (scelta == 1):
        modificaTarga(cnx, cur, id)
    else:
        modificaColore(cnx, cur, id)


def modificaNumTelefonoPasseggero(cnx, cur, id):
    num_telefono = checkLen("Inserire il numero di telefono: ", 15,
                            "La lunghezza massima è stata superata")
    sql_update = "UPDATE passeggero SET num_telefono=%s WHERE cf=%s"
    val = (num_telefono, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaCodiceDocumento(cnx, cur, id):
    codice_documento = checkLen("Inserire il codice del documento: ", 10,
                                "La lunghezza massima è stata superata")
    sql_update = "UPDATE passeggero SET codice_documento=%s WHERE cf=%s"
    val = (codice_documento, id)
    cur.execute(sql_update, val)
    cnx.commit()


def UpdateDatiPasseggero(cnx, cur, scelta, id):
    if (scelta == 1):
        modificaNumTelefonoPasseggero(cnx, cur, id)
    else:
        modificaCodiceDocumento(cnx, cur, id)


def modificaPasseggero(cnx, cur, id):
    cf = checkLen("Inserire la targa(max 10 chars): ", 10,
                  "La lunghezza massima è stata superata")
    sql_update = "UPDATE prenotazione SET cf=%s WHERE codice=%s"
    val = (cf, id)
    cur.execute(sql_update, val)
    cnx.commit()


def UpdateDatiPrenotazione(cnx, cur, scelta, id):
    modificaPasseggero(cnx, cur, id)


def modificaValutazionePasseggero(cnx, cur, id):
    valutazione = checkFloat(
        "Inserire la valutazione(numeri interi o con .5): ",
        "Il valore inserito non è valido: ")
    while (valutazione % 0.5 == False and valutazione > 5 or valutazione < 0):
        valutazione = checkFloat(
            "Inserire la valutazione(numeri interi o con .5): ",
            "Il valore inserito non è valido: ")
    sql_update = "UPDATE feedback_passeggero SET valutazione=%s WHERE id_feedback=%s"
    val = (valutazione, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaFeedbackPasseggero(cnx, cur, id):
    feedback = checkLen("Inserire la valutazione(da 0 a 100 chars): ", 100,
                        "la lunghezza massima è stata superata")
    sql_update = "UPDATE feedback_passeggero SET feedback=%s WHERE id_feedback=%s"
    val = (feedback, id)
    cur.execute(sql_update, val)
    cnx.commit()


def UpdateDatiFeedbackPasseggero(cnx, cur, scelta, id):
    if (scelta == 1):
        modificaValutazionePasseggero(cnx, cur, id)
    else:
        modificaFeedbackPasseggero(cnx, cur, id)


def modificaValutazioneAutista(cnx, cur, id):
    valutazione = checkFloat(
        "Inserire la valutazione(numeri interi o con .5): ",
        "Il valore inserito non è valido: ")
    while (valutazione % 0.5 == False and valutazione > 5 or valutazione < 0):
        valutazione = checkFloat(
            "Inserire la valutazione(numeri interi o con .5): ",
            "Il valore inserito non è valido: ")
    sql_update = "UPDATE feedback_autista SET valutazione=%s WHERE id_feedback=%s"
    val = (valutazione, id)
    cur.execute(sql_update, val)
    cnx.commit()


def modificaFeedbackAutista(cnx, cur, id):
    feedback = checkLen("Inserire la valutazione(da 0 a 100 chars): ", 100,
                        "la lunghezza massima è stata superata")
    sql_update = "UPDATE feedback_autista SET feedback=%s WHERE id_feedback=%s"
    val = (feedback, id)
    cur.execute(sql_update, val)
    cnx.commit()


def UpdateDatiFeedbackAutista(cnx, cur, scelta, id):
    if (scelta == 1):
        modificaValutazioneAutista(cnx, cur, id)
    else:
        modificaFeedbackAutista(cnx, cur, id)


############################ - Delete Data
def delete_db(cnx, cur, scelta):
    if (scelta == 1):
        DeleteDatiViaggio(cnx, cur)
    elif (scelta == 2):
        DeleteDatiAutista(cnx, cur)
    elif (scelta == 3):
        DeleteDatiAuto(cnx, cur)
    elif (scelta == 4):
        DeleteDatiPasseggero(cnx, cur)
    elif (scelta == 5):
        DeleteDatiPrenotazione(cnx, cur)
    elif (scelta == 6):
        DeleteDatiFeedbackPasseggero
    else:
        DeleteDatiFeedbackAutista


def DeleteDatiViaggio(cnx, cur):
    printDatiViaggio(cur)
    scelta = int(input("Inserire l'id del viaggio da eliminare: "))
    sql_delete = "DELETE FROM viaggio WHERE id_viaggio=%s" % (scelta)
    try:
        cur.execute(sql_delete)
        cnx.commit()
    except:
        print("L'id scelto non è stato eliminato")


def DeleteDatiAutista(cnx, cur):
    printDatiAutista(cur)
    scelta = int(input("Inserire l'id dell'autista da eliminare: "))
    sql_delete = "DELETE FROM autista WHERE id_autista=%s" % (scelta)
    try:
        cur.execute(sql_delete)
        cnx.commit()
    except:
        print("L'id scelto non è stato eliminato")


def DeleteDatiAuto(cnx, cur):
    printDatiAuto(cur)
    scelta = int(input("Inserire il codice dell'auto da eliminare: "))
    sql_delete = "DELETE FROM automobile WHERE codice_auto=%s" % (scelta)
    try:
        cur.execute(sql_delete)
        cnx.commit()
    except:
        print("L'id scelto non è stato eliminato")


def DeleteDatiPasseggero(cnx, cur):
    printDatiPasseggero(cur)
    scelta = int(
        input("Inserire il codice fiscale del passeggero da eliminare: "))
    sql_delete = "DELETE FROM passeggero WHERE cf=%s" % (scelta)
    try:
        cur.execute(sql_delete)
        cnx.commit()
    except:
        print("L'id scelto non è stato eliminato")


def DeleteDatiPrenotazione(cnx, cur):
    printDatiPrenotazioni(cur)
    scelta = int(input("Inserire il codice della prenotazione da eliminare: "))
    sql_delete = "DELETE FROM prenotazione WHERE codice=%s" % (scelta)
    try:
        cur.execute(sql_delete)
        cnx.commit()
    except:
        print("L'id scelto non è stato eliminato")


def DeleteDatiFeedbackPasseggero(cnx, cur):
    printDatiFeedbackPasseggero(cur)
    scelta = int(input("Inserire l'id del feedback passeggero da eliminare: "))
    sql_delete = "DELETE FROM feedback_passeggero WHERE id_feedback=%s" % (
        scelta)
    try:
        cur.execute(sql_delete)
        cnx.commit()
    except:
        print("L'id scelto non è stato eliminato")


def DeleteDatiFeedbackAutista(cnx, cur):
    printDatiFeedbackAutista(cur)
    scelta = int(input("Inserire l'id del feedback autista da eliminare: "))
    sql_delete = "DELETE FROM feedback_autista WHERE id_feedback=%s" % (scelta)
    try:
        cur.execute(sql_delete)
        cnx.commit()
    except:
        print("L'id scelto non è stato eliminato")


############################ - Querying Data
def queries(cur, scelta):
    if (scelta == 1):
        myQuery1(cur)
    elif (scelta == 2):
        myQuery2(cur)
    else:
        myQuery3(cur)


def myQuery1(cur):
    citta_partenza = input("Inserire la citta di partenza: ")
    data_partenza = input("Inserire la data di partenza: ")
    citta_arrivo = input("Inserire citta di arrivo: ")
    sql_query = "SELECT autista.*,automobile.*,viaggio.prezzo_passeggero FROM viaggio JOIN autista ON viaggio.id_autista=autista.id_autista JOIN automobile ON autista.dati_auto=automobile.codice_auto WHERE viaggio.citta_partenza='%s' AND viaggio.data_partenza='%s' AND viaggio.citta_destinazione='%s' AND viaggio.prenotazione=1 ORDER BY viaggio.ora_partenza ASC" % (
        citta_partenza, data_partenza, citta_arrivo)
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Id autista:" + str(dato[0]) + "\nNome:" + str(dato[1]) +
                  "\nCognome:" + str(dato[2]) + "\nData nascita" +
                  str(dato[3]) + "\nSesso:" + str(dato[4]) + "\nNum patente:" +
                  str(dato[5]) + "\nScadenza patente:" + str(dato[6]) +
                  "\nNum tel:" + str(dato[7]) + "\nMail:" + str(dato[9]) +
                  "\nMarca auto:" + str(dato[13]) + "\nModello:" +
                  str(dato[14]) + "\nColore:" + str(dato[15]) +
                  "\nNum posti:" + str(dato[12]) + "\nTarga:" + str(dato[11]) +
                  "\nPrezzo per passeggero:" + str(dato[16]) + "€")
    else:
        print(
            "I dati inseriti per la ricerca non hanno portato ad un risultato")


def myQuery2(cur):
    codice = input("Inserire il codice di prenotazione: ")
    sql_query = "SELECT viaggio.*,autista.*,automobile.* FROM viaggio JOIN autista ON viaggio.id_autista=autista.id_autista JOIN automobile ON automobile.codice_auto=autista.dati_auto JOIN prenotazione ON prenotazione.id_viaggio=viaggio.id_viaggio WHERE prenotazione.codice='%s'" % (
        codice)
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Citta partenza:" + str(dato[4]) + "\nData partenza:" +
                  str(dato[2]) + "\nCitta destinazione:" + str(dato[5]) +
                  "\nDurata viaggio:" + str(dato[6]) + "\nId autista:" +
                  str(dato[1]) + "\nNome:" + str(dato[10]) + "\nCognome:" +
                  str(dato[11]) + "\nData nascita" + str(dato[12]) +
                  "\nSesso:" + str(dato[13]) + "\nNum patente:" +
                  str(dato[14]) + "\nScadenza patente:" + str(dato[15]) +
                  "\nNum tel:" + str(dato[16]) + "\nMail:" + str(dato[18]) +
                  "\nMarca auto:" + str(dato[22]) + "\nModello:" +
                  str(dato[23]) + "\nColore:" + str(dato[24]) +
                  "\nNum posti:" + str(dato[21]) + "\nTarga:" + str(dato[20]))
    else:
        print(
            "I dati inseriti per la ricerca non hanno portato ad un risultato")


def myQuery3(cur):
    id_viaggio = input("Inserire id viaggio: ")
    media = input("Inserire voto minimo per i passeggeri: ")
    sql_query = "SELECT passeggero.*,AVG(feedback_passeggero.valutazione) FROM passeggero JOIN prenotazione ON prenotazione.cf=passeggero.cf JOIN viaggio ON viaggio.id_viaggio=prenotazione.id_viaggio JOIN feedback_passeggero ON feedback_passeggero.cf=passeggero.cf WHERE viaggio.id_viaggio='%s' HAVING AVG(feedback_passeggero.valutazione)>='%s'" % (
        id_viaggio, media)
    cur.execute(sql_query)
    dati = cur.fetchall()
    if (len(dati) != 0):
        for dato in dati:
            print("Codice fiscale:" + str(dato[0]) + "\nNome:" + str(dato[1]) +
                  "\nCognome:" + str(dato[2]) + "\nNum telefono:" +
                  str(dato[3]) + "\nCodice documento:" + str(dato[4]) +
                  "\nMail:" + str(dato[5]) + "\nMedia valutazione:" +
                  str(dato[6]))
    else:
        print(
            "I dati inseriti per la ricerca non hanno portato ad un risultato")


############################ - Main
def mainProcess():
    cnx = dbConnection()
    cur = cnx.cursor()
    while True:
        scelta = menu(
            "1 - Inserire dati nel db\n" + "2 - Visualizzare dati del db\n" +
            "3 - Modificare dati del db\n" + "4 - Eliminare dati dal db\n" +
            "5 - Eseguire le query\n" + "6 - Exit", 1, 6)
        if (scelta == 1):
            scelta_ins = menu(
                "1 - Inserire dati viaggio\n" + "2 - Inserire dati autista\n" +
                "3 - Inserire dati auto\n" + "4 - Inserire dati passeggero\n" +
                "5 - Inserire dati prenotazione\n" +
                "6 - Inserire feedback ad un passeggero\n" +
                "7 - Inserire feedback ad un autista\n"
                "8 - Exit", 1, 8)
            if (scelta_ins != 8):
                inserimento_db(cnx, cur, scelta_ins)
        elif (scelta == 2):
            scelta_ins = menu(
                "1 - Visualizzare dati viaggio\n" +
                "2 - Visualizzare dati autista\n" +
                "3 - Visualizzare dati auto\n" +
                "4 - Visualizzare dati passeggero\n" +
                "5 - Visualizzare dati prenotazione\n" +
                "6 - Visualizzare feedback ad un passeggero\n" +
                "7 - Visualizzare feedback ad un autista\n"
                "8 - Exit", 1, 8)
            if (scelta_ins != 8):
                visualizzazione_db(cur, scelta_ins)
        elif (scelta == 3):
            scelta_ins = menu(
                "1 - Modificare dati viaggio\n" +
                "2 - Modificare dati autista\n" +
                "3 - Modificare dati auto\n" +
                "4 - Modificare dati passeggero\n" +
                "5 - Modificare dati prenotazione\n" +
                "6 - Modificare feedback ad un passeggero\n" +
                "7 - Modificare feedback ad un autista\n"
                "8 - Exit", 1, 8)
            if (scelta_ins != 8):
                update_db(cnx, cur, scelta_ins)
        elif (scelta == 4):
            scelta_ins = menu(
                "1 - Eliminare dati viaggio\n" +
                "2 - Eliminare dati autista\n" + "3 - Eliminare dati auto\n" +
                "4 - Eliminare dati passeggero\n" +
                "5 - Eliminare dati prenotazione\n" +
                "6 - Eliminare feedback ad un passeggero\n" +
                "7 - Eliminare feedback ad un autista\n"
                "8 - Exit", 1, 8)
            if (scelta_ins != 8):
                delete_db(cnx, cur, scelta_ins)
        elif (scelta == 5):
            scelta_ins = menu(
                "1 - Eseguire la query 1\n" + "2 - Eseguire la query 2\n" +
                "3 - Eseguire la query 3\n" + "4 - Exit", 1, 4)
            if (scelta_ins != 4):
                queries(cur, scelta_ins)
        elif (scelta == 6):
            print("Il programma è terminato")
            break
    dbClose(cnx)


if __name__ == '__main__':
    mainProcess()