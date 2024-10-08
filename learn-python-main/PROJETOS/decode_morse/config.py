file_path = "decode_morse.csv"
# Dicionário Morse atualizado
dict_morse = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",  # Ponto final
    "--..--": ",",  # Vírgula
    "..--..": "?",  # Ponto de interrogação
    "-.-.--": "!",  # Ponto de exclamação
    "-....-": "-",  # Hífen
    ".-.-.": "É",   # Letra É
    "..-..": "Í",   # Letra Í
    "---.": "Ó",    # Letra Ó
    ".--.-.": "Á",  # Letra Á
    "--.--": "Õ",   # Letra Õ
    ".-.-": "Ç",    # Letra Ç
    "-.--.": "(",   # Abre parêntese
    "-.--.-": ")",  # Fecha parêntese
    "---...": ":",  # Dois pontos
    ".-..-.": "\"", # Aspas
    "-.-.-.": ";",  # Ponto e vírgula
    "-..-.": "/",   # Barra
}