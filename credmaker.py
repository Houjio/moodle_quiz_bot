n = input("C'est quoi ton identifiant moodle (ex: sedasb):")
p = input("C'est quoi ton mot de passe moodle (il reste sur ton ordinateur locale):")

with open("creds.txt", 'w') as f:
    f.write(n)
    f.write('\n')
    f.write(p)
    print("Le bot est pres pour toi.")
