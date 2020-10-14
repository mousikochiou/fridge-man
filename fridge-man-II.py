# Αρχικοποιήσεις
moment_closed = 0
moment_opened = 0
open_door = False
# Πόσα sec έμεινε ανοικτή η πόρτα
time_open = 0
# Πόσα sec συνολικά έχει ανοίξει η πόρτα
total_time_open = 0
# Στα πόσα δευτερόλεπτα θέλουμε να αρχίζει ο ήχος (με την πόρτα ανοικτή)
noise_start_sec = 10
# Στα πόσα λεπτά θεωρούμε ότι το ψυγείο έχει "συνέλθει" από τα ανοίγματα (θα γίνεται reset).
reset_minutes = 3
# Στα πόσα λεπτά (πριν από το reset) να θεωρούμε ότι το ψυγείο στεναχωριέται που έχει ανοίξει τόσο πολύ/συχνά.
unhappy_mood_min = 1
# Παράμετροι για τον ήχο
music.set_tempo(100)
music.set_volume(70)

# Καταμέτρηση χρόνων, εμφάνιση εικονιδίων, ρύθμιση παραμέτρων ήχου
def on_forever():
    global time_open, total_time_open
    if open_door == True:
        time_open = Math.round((moment_opened - moment_closed) / 1000)
        # Στα πρώτα __ sec απλά εμφανίζουμε ένα εικονίδιο (ένα μικρό διαμάντι).
        # Έπειτα εμφανίζουμε το εικονίδιο Χ και αναπαράγεται ένας ήχος.
        if time_open < noise_start_sec:
            basic.show_icon(IconNames.SMALL_DIAMOND)
        else:
            basic.show_icon(IconNames.NO)
            music.set_volume(250)
            music.set_tempo(200)
    else:
        # Όταν κλείνει η πόρτα, προσθέτουμε το χρόνο που έμεινε ανοικτή στον συνολικό,
        # μηδενίζουμε τον χρόνο ανοίγματος και χαμηλώνουμε ξανά την ένταση του ήχου.
        total_time_open += time_open
        time_open = 0
        music.set_volume(70)
        music.set_tempo(100)
        # Αν ο συνολικός χρόνος που έμεινε ανοικτή η πόρτα αυξηθεί, εμφανίζουμε τη στεναχωρημένη φατσούλα.
        if total_time_open > unhappy_mood_min * 60:
            basic.show_icon(IconNames.SAD)
        else:
            basic.clear_screen()
    basic.pause(100)
basic.forever(on_forever)

# Ανίχνευση της κατάστασης της πόρτας, καταγραφή στιγμών συμβάντων
def on_forever2():
    global moment_opened, open_door, moment_closed
    if input.pin_is_pressed(TouchPin.P1):
        moment_opened = input.running_time()
        open_door = True
    else:
        open_door = False
        moment_closed = input.running_time()
    basic.pause(100)
basic.forever(on_forever2)

# Αναπαραγωγή ήχου και επιλογή τόνου/μελωδίας
def on_forever3():
    if open_door == True:
        music.play_tone(587, music.beat(BeatFraction.HALF))
basic.forever(on_forever3)

# Επαναφορά σε κατάσταση "ηρεμίας" μετά από κάποιο χρόνο (μηδενισμός συνολικού χρόνου)
def on_forever4():
    global total_time_open
    # Μηδενίζουμε τον συνολικό χρόνο, θεωρώντας ότι το ψυγείο επανήλθε σε κανονική λειτουργία κάθε ___ ώρες 
    if Math.round(input.running_time() / 1000) % (reset_minutes * 60) < 2:
        total_time_open = 0
    basic.pause(1000)
basic.forever(on_forever4)
