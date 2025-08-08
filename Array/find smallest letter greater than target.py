def next_greatest_letter(letters, target):
    for i in range(len(letters)):
        if target not in letters[i]:
            return letters[0]
        else:
            return letters[i+1]