'''
O Código Morse é um sistema de representação de letras, algarismos e sinais de pontuação através
de um sinal codificado enviado de modo intermitente. Foi desenvolvido por Samuel Morse em 1837, 
criador do telégrafo elétrico, dispositivo que utiliza correntes elétricas para controlar eletroímãs 
que atuam na emissão e na recepção de sinais. 
O script tem a finalidade de decifrar uma mensagem em código morse e salvá-la em texto claro..
'''

import sys
import datetime
import pandas as pd
import os
from config import file_path, dict_morse

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços e palavras por dois espaços
    output : frase escrita em letras e algarismos
    '''
    msg_words = msg.split("  ")  # Palavras são separadas por dois espaços
    decoded_words = []
    
    for word in msg_words:
        msg_lst = word.split(" ")  # Letras dentro de cada palavra são separadas por um espaço
        msg_claro = []
        for letter in msg_lst:
            if letter:  # Ignorar strings vazias
                msg_claro.append(dict_morse.get(letter, ""))  # Adiciona letra decodificada
        decoded_words.append("".join(msg_claro))  # Adiciona palavra decodificada
    
    return " ".join(decoded_words)  # Junta todas as palavras com um espaço entre elas

def save_clear_msg_csv_hdr(msg_claro):
    '''
    input : mensagem em texto claro
    output : palavra escrita em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode="a", index=False, header=hdr)

def main():
    # Se houver argumentos passados pela linha de comando, use-os
    if len(sys.argv) > 1:
        morse_texts = [sys.argv[1]]
    else:
        # Se não houver argumentos, use uma entrada padrão
        morse_texts = [
            "-... . --  ...- .. -. -.. ---  .- ---  -.-. ..- .-. ... ---  -.. .  .--. -.-- - .... --- -.",  # BEM-VINDO AO CURSO DE PYTHON
            ". ... - .- -- --- ...  .- .--. .-. . -. -.. . -. -.. ---  .-  -.. . -.-. --- -.. .. ..-. .. -.-. .- .-.  -- --- .-. ... .",  # ESTAMOS APRENDENDO A DECODIFICAR MORSE
            "---  .--. -.-- - .... --- -.  .-.-.  -- ..- .. - ---  ...- . .-. ... .- - .. .-..  .  .--. --- -.. . .-. --- ... ---"  # O PYTHON É MUITO VERSÁTIL E PODEROSO
        ]
    
    decoded_messages = [decode_morse(morse_text) for morse_text in morse_texts]
    final_message = "  ".join(decoded_messages)  # Junta todas as mensagens com dois espaços entre elas
    print("Mensagem decodificada: %s" % final_message)
    
    # Salvando a mensagem decodificada em um arquivo CSV
    save_clear_msg_csv_hdr(final_message)

if __name__ == "__main__":
    main()
