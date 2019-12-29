# Πορτιέρης ψυγείου
Με τη βοήθεια ενός micro:bit θα προτρέπουμε τον χρήστη του ψυγείου να ελαχιστοποιήσει το διάστημα που διατηρεί την πόρτα του ψυγείου ανοικτή, ώστε να εξοικονομείται ενέργεια. Συγκεκριμένα το έργο μας θα βρει άμεσα εφαρμογή στο ψυγείο του σχολείου μας, ωστόσο θα μπορεί άνετα να λειτουργήσει σε οποιοδήποτε ψυγείο, κάτι που θα διευκολυνθεί αφού η χρήση του πρωτότυπου μηχανισμού εντός του σχολείου (και η σχετική επίδειξη) θα λειτουργήσει πολλαπλασιαστικά για μαθητές και εκπαιδευτικούς.

## Υλικό
- 1x Micro:bit (20 €)
- 1x Μετασχηματιστής microUSB 5 Volt (5 €), αλλά αρκεί οποιοσδήποτε φορτιστής τηλεφώνου (-5 €)
- 1x Piezo Buzzer (2 €)
- 1x Magnetic Reed Switch (3 €)

**Ενδεικτικό συνολικό κόστος** : 25-30 €

## Αναλυτική περιγραφή
Όταν ανοίγει η πόρτα του ψυγείου και μετά από 5 sec* ακούγεται ένας αργός επαναλαμβανόμενος ήχος, ο οποίος γίνεται πιο γρήγορος μετά από 10 sec*, μέχρι να κλείσουμε την πόρτα του ψυγείου.<br />
Παράλληλα καταγράφεται ο συνολικός χρόνος που έμεινε ανοικτή η πόρτα, ο οποίος μηδενίζεται κάθε 1 ώρα*. Εαν ο χρόνος αυτός είναι μεγαλύτερος από 1 λεπτό*, τότε αναβοσβήνει ένα λυπημένο προσωπάκι στην οθόνη του microbit.<br />
*: οι χρόνοι είναι ενδεικτικοί - θα είναι παραμετροποιήσιμοι.

## Προαιρετική επέκταση
Θα επιχειρήσουμε, με τη βοήθεια ενός αισθητήρα μαγνητικού πεδίου (Hall Effect Sensor) ο οποίος θα τοποθετηθεί πολύ κοντά στον ηλεκτρομαγνήτη του μοτέρ του ψυγείου, να αντιλαμβανόμαστε πότε και για πόσο ενεργοποιείται το μοτέρ του ψυγείου και να καταμετράμε το συνολικό χρόνο λειτουργίας του ώστε να εμφανίζουμε στην οθόνη (κατά προσέγγιση) τη συνολική κατανάλωση ηλεκτρικής ενέργειας του ψυγείου.<br />Ενδεικτικό κόστος: +3 €.

