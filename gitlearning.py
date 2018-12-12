#caesor cifer

message = input("Write your message: ")

key = int(input("Choose key: "))

mode = input("Decrypt or encrypt: ")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

translated = ""

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == "encrypt":
            translatedIndex = symbolIndex + key
        elif mode == "decrypt":
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        translated = translated + symbol

print(translated)