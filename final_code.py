import sqlite3

con = sqlite3.connect("zoo_database.db")
cur = con.cursor()

print("Αυτή είναι η διεπαφή για τη βάση δεδομένων του Πατραϊκού Ζωολογικού κήπου.")
while True:

    print("Με τι σχετίζεται η τωρινή σας ανζήτηση; \n1 - Τα ζώα του κήπου\n2 - Τους εργαζομένους"\
            " του\n3 - Τους Προμηθευτές του και τις ζωοτροφές του\n"\
                "4 - Με κάποιο πρόγραμμα φροντίδας/σίτισης ζώου\n0 - Έξοδος από την εφαρμογή")
    answer1=input('Δώστε Επιλογή: ')
    print(" ")
    if answer1 == '0':
        break
    elif answer1 == '1':
        while True:
            print("Τι θέλετε να κάνετε; \n1 - Δείτε τη λίστα με τα ζώα \n2 - Επεξεργαστείτε τα "\
                "στοιχεία των ζώων\n3 - Αναζητήστε τις πληροφορίες για κάποιο ζώο\n4 - Προσθήκη"\
                    " νέου ζώου στη λίστα\n0 - Επιστροφή")
            answer2=input('Δώστε Επιλογή: ')
            print(" ")
            if answer2=='0':
                break
            elif answer2 == '1':
                hop=[b for b in cur.execute("SELECT Όνομα, Όνομα_Κατηγορίας FROM Ζώο")]
                for i in hop:
                    print(*i, sep=', ')
                print(" ")
            elif answer2 == '2':
                while True:
                    print("Επιλέξτε: \n 1 - Αλλαγή ονόματος ζώου\n 2 - Προσθήκη ημ/νίας θανάτου\n 0 - Επιστροφή")
                    answer3=input('Δώστε Επιλογή: ')
                    print(" ")
                    if answer3 == '0':
                        break
                    elif answer3 == '1':
                        curName=input('Δώστε το τρέχον όνομα του ζώου (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                        newName=input('Δώστε το νέο όνομα του ζώου (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                        cur.execute("UPDATE Ζώο SET Όνομα='{}' WHERE Όνομα='{}' ".format(newName,curName))
                        if cur.rowcount < 1:
                            print('Λανθασμένο όνομα ζώου\n')
                            continue
                        print("\n Επιτυχής Αλλαγή Ονόματος!")
                        con.commit()
                    elif answer3 == '2':
                        curName=input('Δώστε το όνομα του ζώου (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                        date=input('Δώστε την ημ/νία θανάτου του (yyyy-mm-dd): ')
                        cur.execute("UPDATE Ζώο SET Ημερομηνία_Θανάτου='{}' WHERE Όνομα='{}' ".format(date,curName))
                        if cur.rowcount < 1:
                            print('Λανθασμένο όνομα ζώου\n')
                            continue
                        print("\n Επιτυχής προσθήκη")
                        con.commit()
                    else:
                        print("Λανθασμένη Απάντηση, Προσπαθήστε Ξανά:")
                        continue
            elif answer2 == '3':
                while True:
                    print("Για ποιο ζώο θέλετε να δείτε τις πληροφορίες; Αν δεν ενδιαφέρεστε άλλο για αυτή τη λειτουργία, "\
                        "πατήστε Enter για να επιλέξετε μετά τον αριθμό 0")
                    name=input('Δώστε το Όνομά του(ελληνικά, 1ο γράμμα κεφαλαίο): ')
                    print("Τι θέλετε να γνωρίζετε για το ζώο;\n 1 - Πού ανήκει με βάση τη διατροφή του, ποιες τροφές τρώει\n "\
                    "2 - Πού βρίσκεται το κατάλυμά του, τι είδους είναι και ποιο το κλίμα του\n 0 - Επιστροφή")
                    answer3=input('Δώστε Επιλογή: ')
                    print(" ")
                    if answer3 == '0':
                        break
                    elif answer3 == '1':
                        hop1=[b for b in cur.execute("SELECT K.Διατροφή FROM Κατηγορία_Ζώου AS K, Ζώο AS Z WHERE Z.Όνομα='{}'"\
                            "AND Z.Όνομα_Κατηγορίας=K.Όνομα".format(name))]
                        if not hop1:
                            print('Λανθασμένο όνομα ζώου\n')
                            continue
                        print('Το ζώο είναι:')
                        for i in hop1:
                            print(*i, sep=', ')
                        print(" ")
                        hop2=[b for b in cur.execute("SELECT F.Όνομα FROM Τροφή AS F, Τρώει AS T, Ζώο AS Z WHERE Z.Όνομα='{}'"\
                            "AND Z.ID=T.ID_Ζώου AND T.ID_Τροφής=F.ID".format(name))]
                        print('Και τρώει: ')
                        for i in hop2:
                            print(*i, sep=', ')
                        print(" ")
                    elif answer3 == '2':
                        hop=[b for b in cur.execute("SELECT Z.Τοποθεσία_Καταλύματος, K.Είδος, K.Κλίμα FROM Κατάλυμα AS K, Ζώο AS Z "\
                        "WHERE Z.Όνομα='{}' AND Z.Τοποθεσία_Καταλύματος=K.Τοποθεσία".format(name))]
                        if not hop:
                            print('Λανθασμένο όνομα ζώου\n')
                            continue
                        for i in hop:
                            print(*i, sep=', ')
                        print(" ")
                    else:
                        print("Λανθασμένη Απάντηση, Προσπαθήστε Ξανά:")
                        continue
            elif answer2 == '4':
                name=input('Δώστε το Όνομά του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                dateofB=input('Δώστε ημ/νία γέννησης(yyyy-mm-dd): ')
                country=input('Δώστε χώρα προέλευσης: ')
                species=input('Δώστε κατηγορία ζώου: ')
                location=input('Δώστε την τοποθεσία του καταλύματός του (Διάδρομος Χ, Αρ. Υ ή στο Κτήριο Έκθεσης Ερπετών Αρ. Χ): ')
                cur.execute("INSERT INTO Ζώο (ID,Όνομα,Ημερομηνία_Γέννησης,Χώρα_Προέλευσης,Ημερομηνία_Θανάτου"\
                    ",Όνομα_Κατηγορίας,Τοποθεσία_Καταλύματος) VALUES(NULL,'{}','{}','{}',"\
                        "NULL,'{}','{}')".format(name,dateofB,country,species,location))
                print("\n Επιτυχής Προσθήκη Ζώου!")
                con.commit()
            else:
                print("Λανθασμένη Απάντηση, Προσπαθήστε Ξανά:")
                continue
    elif answer1 == '2':
        while True:
            print("Τι θέλετε να κάνετε; \n1 - Δείτε τη λίστα με τους τωρινούς εργαζόμενους \n2 - Προσθήκη"\
                    " νέου εργαζομένου στη λίστα\n3 - Αφαίρεση εργαζόμενου από τη λίστα\n4 - Εμφάνιση "\
                        "τηλεφώνων επικοινωνίας εργαζομένου\n0 - Επιστροφή")
            answer2=input('Δώστε Επιλογή: ')
            print(" ")
            if answer2=='0':
                break
            elif answer2 == '1':
                hop1=[b for b in cur.execute("SELECT ΑΦΜ,Όνομα,Επώνυμο FROM Εργαζόμενος NATURAL"\
                    " JOIN Επιμελητής_Ζώου")]
                print('Οι Επιμελητές:')
                for i in hop1:
                    print(*i, sep=', ')
                hop2=[b for b in cur.execute("SELECT ΑΦΜ,Όνομα,Επώνυμο FROM Εργαζόμενος NATURAL"\
                    " JOIN Καθαριστής")]
                print('Οι Καθαριστές:')
                for i in hop2:
                    print(*i, sep=', ')
                hop3=[b for b in cur.execute("SELECT ΑΦΜ,Όνομα,Επώνυμο FROM Εργαζόμενος NATURAL"\
                    " JOIN Κτηνίατρος")]
                print('Οι Κτηνίατροι:')
                for i in hop3:
                    print(*i, sep=', ')
                print(" ")
            elif answer2 == '2':
                afm=input('Δώστε το ΑΦΜ του (ακέραιος αριθμός 9 ψηφίων): ')
                if len(afm)!=9:
                    print('Λανθασμένο μήκος ΑΦΜ Εργαζομένου\n')
                    continue
                dateofS=input('Δώστε ημ/νία εναρξης εργασίας (yyyy-mm-dd): ')
                dateofB=input('Δώστε ημ/νία γέννησης (yyyy-mm-dd): ')
                Fname=input('Δώστε το Όνομά του: ')
                Lname=input('Δώστε το Επώνυμό του: ')
                special=input('Ποια η ειδικότητά του (Επιμελητής_Ζώου,Καθαριστής,Κτηνίατρος): ')
                if (special!='Κτηνίατρος' and special!='Επιμελητής_Ζώου' and special!='Καθαριστής'):
                    print('Λανθασμένη Ειδικότητα Εργαζομένου\n')
                    continue   
                cur.execute("INSERT INTO Εργαζόμενος (ΑΦΜ,Έναρξη_Εργασίας,Ημερομηνία_Γέννησης,Όνομα,Επώνυμο)"\
                    " VALUES('{}','{}','{}','{}','{}')".format(afm,dateofS,dateofB,Fname,Lname))
                cur.execute("INSERT INTO {} (ΑΦΜ) VALUES('{}')".format(special,afm))
                print("\n Επιτυχής Προσθήκη Εργαζόμενου!")
                con.commit()
            elif answer2 == '3':
                afm=input('Δώστε το ΑΦΜ του (9 ψηφία): ')
                cur.execute("DELETE FROM Εργαζόμενος WHERE ΑΦΜ={}".format(afm))
                if cur.rowcount < 1:
                    print('Λανθασμένο ΑΦΜ εργαζομένου\n')
                    continue
                print("\n Επιτυχής Αφαίρεση Εργαζόμενου")
                con.commit()
            elif answer2 == '4':
                Fname=input('Δώστε το όνομά του: ')
                Lname=input('Δώστε το επώνυμό του: ')
                hop=[b for b in cur.execute("SELECT T.Τηλέφωνο FROM Εργαζόμενος AS E, Τηλέφωνο_Εργαζομένου"\
                    " AS T WHERE E.Όνομα='{}' AND E.Επώνυμο='{}' AND E.ΑΦΜ=T.ΑΦΜ_Εργαζομένου".format(Fname,Lname))]
                if not hop:
                    print('Λανθασμένο όνομα ή/και επώνυμο εργαζομένου\n')
                    continue
                for i in hop:
                    print(*i, sep=', ')
                print(" ")
            else:
                print("Λανθασμένη Απάντηση, Προσπαθήστε Ξανά:")
                continue
    elif answer1 == '3':
        while True:
            print("Τι θέλετε να κάνετε; \n1 - Δείτε τη λίστα με τους τωρινούς προμηθευτές \n2 - Προσθήκη"\
                    " νέου προμηθευτή στη λίστα\n3 - Αφαίρεση προμηθευτή από τη λίστα\n4 - Εμφάνιση "\
                        "τηλεφώνων επικοινωνίας προμηθευτή\n5 - Ποιες παραδώσεις έχει πραγματοποιήσει  "\
                            "κάποιος συγκεκριμένος προμημευτής τις τελευταίες 20 μέρες\n0 - Επιστροφή")
            answer2=input('Δώστε Επιλογή: ')
            print(" ")
            if answer2=='0':
                break
            elif answer2 == '1':
                hop1=[b for b in cur.execute("SELECT ΑΦΜ,Όνομα,Επώνυμο FROM Προμηθευτής")]
                for i in hop1:
                    print(*i, sep=', ')
                print(" ")
            elif answer2 == '2':
                afm=input('Δώστε το ΑΦΜ του (9 ψηφία): ')
                if len(afm)!=9:
                    print('Λανθασμένο μήκος ΑΦΜ Προμηθευτή\n')
                    continue
                Fname=input('Δώστε το Όνομά του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                Lname=input('Δώστε το Επώνυμό του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                corpo=input('Δώστε την εταιρία στην οποία ανήκει: ')
                place=input('Δώστε τη διεύθυνσή του (οδός αριθμός, πόλη): ')
                cur.execute("INSERT INTO Προμηθευτής (ΑΦΜ,Όνομα,Επώνυμο,Εταιρία,Διεύθυνση)"\
                    " VALUES('{}','{}','{}','{}','{}')".format(afm,Fname,Lname,corpo,place))
                print("\n Επιτυχής Προσθήκη Προμηθευτή!")
                con.commit()
            elif answer2 == '3':
                afm=input('Δώστε το ΑΦΜ του (9 ψηφία): ')
                cur.execute("DELETE FROM Προμηθευτής WHERE ΑΦΜ={}".format(afm))
                if cur.rowcount < 1:
                    print('Λανθασμένο ΑΦΜ Προμηθευτή\n')
                    continue
                print("\n Επιτυχής Αφαίρεση Προμηθευτή")
                con.commit()
            elif answer2 == '4':
                Fname=input('Δώστε το όνομά του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                Lname=input('Δώστε το επώνυμό του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                hop=[b for b in cur.execute("SELECT T.Τηλέφωνο FROM Προμηθευτής AS E, Τηλέφωνο_Προμηθευτή"\
                    " AS T WHERE E.Όνομα='{}' AND E.Επώνυμο='{}' AND E.ΑΦΜ=T.ΑΦΜ_Προμηθευτή".format(Fname,Lname))]
                if not hop:
                    print('Λανθασμένο όνομα ή/και επώνυμο προμηθευτή\n')
                    continue
                for i in hop:
                    print(*i, sep=', ')
                print(" ")
            elif answer2 == '5':
                Fname=input('Δώστε το όνομά του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                Lname=input('Δώστε το επώνυμό του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                hop=[b for b in cur.execute("SELECT T.Όνομα,D.Ημερομηνία_Παράδοσης FROM Προμηθευτής AS P,"\
                    " Παραδίδει AS D, Τροφή AS T WHERE P.ΑΦΜ=D.ΑΦΜ_Προμηθευτή AND D.ID_Τροφής=T.ID AND "\
                        "D.Ημερομηνία_Παράδοσης<=date('now') AND D.Ημερομηνία_Παράδοσης>=date('now', '-20 days')"\
                            " AND P.Όνομα='{}' AND P.Επώνυμο='{}' ORDER BY D.Ημερομηνία_Παράδοσης DESC".format(Fname,Lname))]
                if not hop:
                    print('Λανθασμένο όνομα ή/και επώνυμο προμηθευτή\n')
                    continue
                for i in hop:
                    print(*i, sep=', ')
                print(" ")
            else:
                print("Λανθασμένη Απάντηση, Προσπαθήστε Ξανά:")
                continue
    elif answer1 == '4':
        while True:
            print("Επιλέξτε: \n 1 - Πρόγραμμα Σίτισης κάποιου ζώου τις τελευταίες Χ μέρες \n 2 - Πρόγραμμα Φροντίδας\n "\
                "3 - Ποιοι είναι υπεύθυνοι για τη σίτιση των καταλυμάτων σήμερα\n 4 - Για ποια προγράμματα φροντίδας "\
                    "είναι υπεύθυνος κάποιος εργαζόμενος \n 0 - Επιστροφή")
            answer2=input('Δώστε Απάντηση: ')
            if answer2 == '0':
                break
            elif answer2 == '1':
                print('Διαλέξτε για ποιο ζώο ενδιαφέρεστε')
                name=input('Δώστε το Όνομά του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                tempname=(name,)
                hop=[b for b in cur.execute("SELECT Όνομα FROM Ζώο")]
                if tempname not in hop:
                    print('Λανθασμένο όνομα ζώου\n')
                    continue
                givencount=input('Εισάγετε τον (ακέραιο) αριθμό των ημερών(1-15 μέρες): ')
                print(" ")
                try:
                    count=int(givencount)
                except:
                    print('Πρέπει να εισάγετε ακέραιο αριθμό')
                    continue
                while count>=0:
                    if count>15:
                        print("Η βάση έχει φτιαχτεί με περιορισμένο αριθμό δεδομένων, δεν υπάρχουν αποτελέσματα"\
                            " πέραν κάποιας ημερομηνίας")
                        continue
                    hop1=[b for b in cur.execute("SELECT S.Ημερομηνία, S.Ώρα_σίτισης FROM Σίτιση_Καταλύματος AS S,"\
                        " Ζώο AS Z WHERE Z.Όνομα='{}' AND Z.Τοποθεσία_Καταλύματος=S.Τοποθεσία_Καταλύματος AND "\
                            "S.Ημερομηνία=date('now', '-{} days')".format(name,count))]
                    hop2=[b for b in cur.execute("SELECT T.Όνομα FROM Σίτιση_Καταλύματος AS S, Ζώο AS Z, Τροφή AS T, "\
                        "Περιλαμβάνει AS P WHERE Z.Όνομα='{}' AND Z.Τοποθεσία_Καταλύματος=S.Τοποθεσία_Καταλύματος AND "\
                            " T.ID=P.ID_Τροφής AND P.ID_Σίτισης=S.ID AND S.Ημερομηνία=date('now', '-{} days')".format(name,count))]
                    for i in hop1:
                        print(*i, sep=', ')
                        print('Περιλαμβάνει τις τροφές:')
                        for j in hop2:
                            print(*j, sep=', ')
                        print(" ")
                    print(" ")
                    count-=1
            elif answer2 == '2':
                while True:
                    print("Επιλέξτε είδος φροντίδας:\n 1 - Έκτακτο Περιστατικό \n 2 - Καθαρισμός Ζώου \n "\
                        "3 - Γενική Περιποίηση \n 4 - Ψυχαγωγικές/Κοινωνικές Δραστηριότητες \n 5 - Αναπαραγωγική "\
                            "Φροντίδα \n 6 - Κτηνιατρικός Έλεγχος \n 7 - Εκπαίδευση/Διαχείριση Συμπεροφοράς\n"\
                                " 0 - Επιστροφή")
                    answer3=input('Δώστε Απάντηση: ')
                    if answer3 == '0':
                        break
                    elif answer3 == '1':
                        hop=[b for b in cur.execute("SELECT C.Ημερομηνία_Διεξαγωγής, Z.Όνομα, Z.Όνομα_Κατηγορίας "\
                            "FROM Δέχεται_Φροντίδα AS D, Φροντίδα_Ζώου AS C, Ζώο AS Z WHERE C.Περιγραφή='Έκτακτο Περιστατικό'"\
                            "AND D.ID_Φροντίδας_Ζώου=C.ID AND D.ID_Ζώου=Z.ID ORDER BY C.Ημερομηνία_Διεξαγωγής ASC")]
                        for i in hop:
                            print(*i, sep=', ')
                            print(" ")
                    elif answer3 == '2':
                        hop=[b for b in cur.execute("SELECT C.Ημερομηνία_Διεξαγωγής, Z.Όνομα, Z.Όνομα_Κατηγορίας "\
                            "FROM Δέχεται_Φροντίδα AS D, Φροντίδα_Ζώου AS C, Ζώο AS Z WHERE C.Περιγραφή='Καθαρισμός Ζώου'"\
                            "AND D.ID_Φροντίδας_Ζώου=C.ID AND D.ID_Ζώου=Z.ID ORDER BY C.Ημερομηνία_Διεξαγωγής ASC")]
                        for i in hop:
                            print(*i, sep=', ')
                            print(" ")
                    elif answer3 == '3':
                        hop=[b for b in cur.execute("SELECT C.Ημερομηνία_Διεξαγωγής, Z.Όνομα, Z.Όνομα_Κατηγορίας "\
                            "FROM Δέχεται_Φροντίδα AS D, Φροντίδα_Ζώου AS C, Ζώο AS Z WHERE C.Περιγραφή='Γενική Περιποίηση'"\
                            "AND D.ID_Φροντίδας_Ζώου=C.ID AND D.ID_Ζώου=Z.ID ORDER BY C.Ημερομηνία_Διεξαγωγής ASC")]
                        for i in hop:
                            print(*i, sep=', ')
                            print(" ")
                    elif answer3 == '4':
                        hop=[b for b in cur.execute("SELECT C.Ημερομηνία_Διεξαγωγής, Z.Όνομα, Z.Όνομα_Κατηγορίας "\
                            "FROM Δέχεται_Φροντίδα AS D, Φροντίδα_Ζώου AS C, Ζώο AS Z WHERE C.Περιγραφή='Ψυχαγωγικές/Κοινωνικές Δραστηριότητες'"\
                            "AND D.ID_Φροντίδας_Ζώου=C.ID AND D.ID_Ζώου=Z.ID ORDER BY C.Ημερομηνία_Διεξαγωγής ASC")]
                        for i in hop:
                            print(*i, sep=', ')
                            print(" ")
                    elif answer3 == '5':
                        hop=[b for b in cur.execute("SELECT C.Ημερομηνία_Διεξαγωγής, Z.Όνομα, Z.Όνομα_Κατηγορίας "\
                            "FROM Δέχεται_Φροντίδα AS D, Φροντίδα_Ζώου AS C, Ζώο AS Z WHERE C.Περιγραφή='Αναπαραγωγική Φροντίδα'"\
                            "AND D.ID_Φροντίδας_Ζώου=C.ID AND D.ID_Ζώου=Z.ID ORDER BY C.Ημερομηνία_Διεξαγωγής ASC")]
                        for i in hop:
                            print(*i, sep=', ')
                            print(" ")
                    elif answer3 == '6':
                        hop=[b for b in cur.execute("SELECT C.Ημερομηνία_Διεξαγωγής, Z.Όνομα, Z.Όνομα_Κατηγορίας "\
                            "FROM Δέχεται_Φροντίδα AS D, Φροντίδα_Ζώου AS C, Ζώο AS Z WHERE C.Περιγραφή='Κτηνιατρικός Έλεγχος'"\
                            "AND D.ID_Φροντίδας_Ζώου=C.ID AND D.ID_Ζώου=Z.ID ORDER BY C.Ημερομηνία_Διεξαγωγής ASC")]
                        for i in hop:
                            print(*i, sep=', ')
                            print(" ")
                    elif answer3 == '7':
                        hop=[b for b in cur.execute("SELECT C.Ημερομηνία_Διεξαγωγής, Z.Όνομα, Z.Όνομα_Κατηγορίας "\
                            "FROM Δέχεται_Φροντίδα AS D, Φροντίδα_Ζώου AS C, Ζώο AS Z WHERE C.Περιγραφή='Εκπαίδευση/Διαχείριση Συμπεροφοράς'"\
                            "AND D.ID_Φροντίδας_Ζώου=C.ID AND D.ID_Ζώου=Z.ID ORDER BY C.Ημερομηνία_Διεξαγωγής ASC")]
                        for i in hop:
                            print(*i, sep=', ')
                            print(" ")
                    else:
                        print("Λανθασμένη Απάντηση, Προσπαθήστε Ξανά:")
                        continue
            elif answer2 == '3':
                hop=[b for b in cur.execute("SELECT DISTINCT E.Όνομα,E.Επώνυμο,Z.Όνομα_Κατηγορίας FROM Εργαζόμενος AS E, "\
                    "Ευθύνεται AS Y, Σίτιση_Καταλύματος AS S, Ζώο AS Z WHERE E.ΑΦΜ=Y.ΑΦΜ_Επιμελητή AND Y.ID_Σίτισης=S.ID"\
                        " AND S.Ημερομηνία=date('now') AND Z.Τοποθεσία_Καταλύματος=S.Τοποθεσία_Καταλύματος "\
                            "ORDER BY S.Ημερομηνία DESC")]
                for i in hop:
                    print(*i, sep=', ')
                print(" ")
            elif answer2 == '4':
                Fname=input('Δώστε το Όνομα του εργαζομένου (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                Lname=input('Δώστε το Επώνυμό του (ελληνικά, 1ο γράμμα κεφαλαίο): ')
                hop1=[b for b in cur.execute("SELECT C.Περιγραφή,C.Ημερομηνία_Διεξαγωγής,Z.Όνομα,Z.Όνομα_Κατηγορίας"\
                    " FROM  Φροντίδα_Ζώου AS C, Εργαζόμενος AS E, Παρέχει_Ε AS P, Δέχεται_Φροντίδα AS D, Ζώο AS Z "\
                        "WHERE E.Όνομα='{}' AND E.Επώνυμο='{}' AND E.ΑΦΜ=P.ΑΦΜ_Επιμελητή AND P.ID_Φροντίδας_Ζώου=C.ID"\
                        " AND C.ID=D.ID_Φροντίδας_Ζώου AND D.ID_Ζώου=Z.ID UNION "\
                            "SELECT C.Περιγραφή,C.Ημερομηνία_Διεξαγωγής,Z.Όνομα,Z.Όνομα_Κατηγορίας"\
                                " FROM  Φροντίδα_Ζώου AS C, Εργαζόμενος AS E, Παρέχει_Κ AS P, Δέχεται_Φροντίδα AS D, Ζώο AS Z "\
                                    "WHERE E.Όνομα='{}' AND E.Επώνυμο='{}' AND E.ΑΦΜ=P.ΑΦΜ_Κτηνιάτρου AND P.ID_Φροντίδας_Ζώου=C.ID"\
                                    " AND C.ID=D.ID_Φροντίδας_Ζώου AND D.ID_Ζώου=Z.ID".format(Fname,Lname,Fname,Lname))]
                if not hop1:
                    print('Λανθασμένο όνομα ή/και επώνυμο εργαζομένου\n')
                    continue
                for i in hop1:
                    print(*i, sep=', ')
                print(" ")
            else:
                print("Λανθασμένη Απάντηση, Προσπαθήστε Ξανά:")
                continue
    else:
        print("Λανθασμένη Απάντηση, Προσπαθήστε Ξανά:")
        continue

con.close()