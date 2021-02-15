try:
    with open('answerkey.txt', 'r') as f:
        awnser_key = [a.replace('\n', '') for a in f.readlines()]
except FileNotFoundError:
    print("Assure toi d'avoir une clef de reponse.")
    quit()

def answers(page):
    if page == 1:
        return page_un()
    else:
        return []

def page_un():
    return awnser_key[0:7]
