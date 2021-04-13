def encrypter():
    inputStr = input('Enter string to be encrypted:')
    words = [char for char in inputStr]
    encrypter_key = {
        "a": '3441', "b": '5643', "c": '9345', "d": '7467', "e": '6459', "f": '1541', "g":
            '1343', "h": '1425', "i": '6371', "j": '1759', "k": '2421', "l": '2443', "m":
            '2535', "n": '2701', "o": '4329', "p": '3431', "q": '3443', "r": '3235', "s":
            '3447', "t": '2339', "u": '4341', "v": '4453', "w": '4675', "x": '4347', "y": '6449', "z": '0951',
        " ": '6751', ',': '8122', '.': '0457','/': '8345', '0': '4234', '1':'0493', '2': '9934', '3': '3420', '4': '9424', '5': '1493', '6': '8654',
        '7' : '4309', '8': '8023', '9': '0540', '?':'9504', '-': '4501', '=':'3931',':': '2985',"A": '3131', "B": '5645', "C": '6345', "D": '7437', "E": '6659', "F": '0541', "G":
            '1243', "H": '1426', "I": '6361', "J": '1729', "K": '2427', "L": '4443', "M":
            '3535', "N": '2101', "O": '2329', "P": '3435', "Q": '6443', "R": '3239', "S":
            '3442', "T": '2349', "U": '4345', "V": '4452', "W": '2675', "X": '5347', "Y": '6764', "Z": '2951',

    }
    encrypted_file = ""
    for ch in words:
        encrypted_file += encrypter_key.get(ch, ch) + ''
    return (encrypted_file)


def decrypter():
    de_inputStr = input('Enter string to be decrypted:')
    n = 4
    de_words = [(de_inputStr[i:i + n]) for i in range(0, len(de_inputStr), n)]
    decrypter_key = {
        '3441': "a", '5643': "b", '9345': "c", '7467': "d", '6459': "e", '1541': "f",
        '1343': "g", '1425': "h", '6371': "i", '1759': "j", '2421': "k", '2443':"l",
        '2535': "m", '2701': "n", '4329': "o", '3431': "p", '3443': "q", '3235': "r",
        '3447': "s", '2339': "t", '4341': "u", '4453': "v", '4675': "w", '4347': "x", '6449': "y", '0951': "z",
        '6751': " ",  '8122':',',  '0457':'.', '8345':'/',  '4234':'0', '0493':'1',  '9934':'2',  '3420':'3',  '9424':'4',  '1493':'5',  '8654':'6',
         '4309':'7',  '8023':'8',  '0540':'9', '9504':'?',  '4501':'-', '3931':'=', '2985':':',
         '3131': "A",  '5645':"B",  '6345':"C",  '7437':"D",  '6659':"E",  '0541':"F",
        '1243':"G",  '1426':"H",  '6361':"I",  '1729':"J",  '2427':"K",  '4443':"L",
        '3535':"M",  '2101':"N",  '2329':"O", '3435':"P" ,  '6443':"Q",  '3239':"R",
        '3442':"S",  '2349':"T", '4345':"U" ,  '4452':"V",  '2675':"W",  '5347':"X",  '6764':"Y",  '2951':"Z"
    }
    decrypted_file = ""
    for ch in de_words:
        decrypted_file += decrypter_key.get(ch, ch) + ''
    return (decrypted_file)




print("Type 'help' for more.")
while True:
    main_input = input('>').lower()
    if 'help' in main_input:
        print("""
Commands:
'encrypt' or 'en', encrypts a inputed string
'decrypt' or 'de', decrypts a inputed string
'quit', quits the program
""")

    if 'encrypt' in main_input:
        print(encrypter())
    elif 'decrypt' in main_input:
        print(decrypter())
    elif 'de' in main_input:
        print(decrypter())
    elif 'en' in main_input:
        print(encrypter())
    elif 'quit' in main_input:
        break
    else:
        print('Invalid command')
