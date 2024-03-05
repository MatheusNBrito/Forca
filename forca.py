import random 
import os
# from os import system, name

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def game():
    limpa_tela()
    
    print("\n Bem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:")
    
    palavras = ["banana", "abacate", "uva", "kiwi", "laranja"]
    palavra = random.choice(palavras)
    letras_descobertas = ['_' for letra in palavra]
    chances = 6
    letras_erradas = []
    
    while chances > 0:
        print(display_hangman(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        
        tentativa = input("\nDigite uma letra ").lower()
        
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era", palavra)
            break
                    
    if "_" in letras_descobertas:
        print("\nVoce perdeu, a palvra era:", palavra)
        
if __name__ == "__main__":
    game()
    print("\nFim de jogo")
            