def decrypt_a1z26(x) -> str:
    """
    Decipher a text (A1Z26 cipher).
    """

    # loops for each item in the string
    # Convert array to words of the sentence (regardless if it is a sentence or not)
    numbers_list_with_hyphons = x.split(' ')
    #splits by space but doesn't regard which are words
    words_array = []
    for i in range(len(numbers_list_with_hyphons)):
        words_array.append(numbers_list_with_hyphons[i].split('-'))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    solution = ''
    for i in range(len(words_array)):
        for j in range(len(words_array[i])):
            solution = solution + str((alphabet[int(words_array[i][j])+1]))
        # make a space after each word
        solution = solution + " "

    print(solution)


decrypt_a1z26("22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1")
