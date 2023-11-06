#Hvis temperaturen er under 0 grader, skriv ut "Det er frysepunktet, kle deg varmt."

#Hvis temperaturen er mellom 0 og 15 grader, skriv ut "Det er kjølig, ta på en jakke."

#Hvis temperaturen er mellom 16 og 25 grader, skriv ut "Det er behagelig, nyt været."

#Hvis temperaturen er over 25 grader, skriv ut "Det er varmt, tid for shorts og T-skjorte."

temperaturen= 12

if temperaturen < 0:
    print('Det er frysepunktet, kle deg varmt.')


if temperaturen > 0 and temperaturen < 15:
    print("Det er kjørlig, ta på en jakke")

if temperaturen > 16 and temperaturen < 25:
    print("Det er behagelig, nyt været.")

if temperaturen > 25:
    print("Det er varmt, tidfor shorts og T-skjorte.")