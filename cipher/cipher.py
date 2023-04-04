def caesarCipher(s, k):
    cipherStr = ''
    for a in s:
        start_position = ord(a)
        upper = (start_position >= 65 and start_position <= 90)
        lower = (start_position >= 97 and start_position <= 122)
        if not (upper or lower):
            cipherStr += chr(start_position)
            continue
        else:
            letter_position = start_position + k
            
            if upper:
                while letter_position > 90:
                    passos_extras = letter_position - 90
                    letter_position = 64 + passos_extras
            if lower:
                while letter_position > 122:
                    passos_extras = letter_position - 122
                    letter_position = 96 + passos_extras

        cipherStr += chr(letter_position)

    return cipherStr   
    
string= "Pz-/aI/J`EvfthGH"
print(caesarCipher(string,66))
