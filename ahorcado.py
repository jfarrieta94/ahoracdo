"""
REVISIONES
X  Arreglar logica de progreso -> usar diccionario con index de key y letra de value y que se imprima los values, ordenandolos
X 
X  Comentar prints innecesarios
4) Arreglar visibilidad del juego
5) Hacer comentarios del funcionamiento del juego
"""
import random
import palabras as words

def letter_locations(ls, index):
    return [i for i in range(len(ls)) if ls[i] == index]

selected_letters = []

# lista de palabras a seleccionar


# seleccionando palabra dentro de la lista
selected_word = random.choice(words.words)
selected_word = selected_word.upper()

# convierte la palabra en un set para poder quitarle letras
selected_word_set = set(selected_word)
selected_word_list = list(selected_word)

lives = 6
start_progress = [' ' for i in selected_word_list]
progress = len(selected_word) * ' '
print(progress)
while lives != 0 and len(selected_word_set) != 0:
    selected_letter = input('¿Cual letra quisieras probar? \n' )
    selected_letter = selected_letter.upper()
    confirmation_message = f'Has seleccionado la letra {selected_letter}'
    print(confirmation_message)

    # seleccion de respuesta correcta o incorrecta, resta vidas y guarda las letras seleccionadas
    if(selected_letter in selected_word_set):
        selected_word_set.remove(selected_letter)
        #print(selected_word_set)
        #print(selected_word)
        selected_letters.append(selected_letter)
        right_letter_message = f'La palabra si tiene a la letra {selected_letter}'
        print(right_letter_message)
    elif(selected_letter in selected_letters):
        print('Ya has seleccionado esta letra')
    else:
        wrong_letter_message = f'La letra {selected_letter} no esta en la palabra'
        print(wrong_letter_message)
        lives = lives - 1
        selected_letters.append(selected_letter)
    
    # Condicional que muestra el progreso 

    response = letter_locations(selected_word_list, selected_letter)
    if selected_letter in selected_word:
        for element in response:
            start_progress.pop(element)
            start_progress.insert(element ,selected_letter)
            progress = "".join(start_progress)

    print('      ', len(selected_word) * '_' , '\n----->', progress,'<----- \n      ', len(selected_word) * '-')
        
    message = f'Te quedan {lives} vidas'
    print(message)

    def letter_locations(ls, index):
        return [i for i in range(len(ls)) if ls[i] == index]
    response = letter_locations(selected_word_list, selected_letter)
     
    if(lives == 1):
        print('    _____\n    |    O \n    |   /|\ \n    |   /  \n____|_______')
    elif(lives == 2):
        print('    _____\n    |    O \n    |   /|\ \n    |      \n____|_______')
    elif(lives == 3):
        print('    _____\n    |    O \n    |   /|  \n    |      \n____|_______')
    elif(lives == 4):
        print('    _____\n    |    O \n    |    |  \n    |      \n____|_______')
    elif(lives == 5):
        print('    _____\n    |    O \n    |       \n    |      \n____|_______')
    elif(lives == 6):
        print('    _____\n    |      \n    |       \n    |      \n____|_______')

    print('Has usado las siguientes letras \n', selected_letters)

tries =  7 - lives

if(lives == 6):
    final_message = f'Felicitaciones, haz ganado el juego en {tries} intento y la palabra era {selected_word}'
elif(lives > 0):
    final_message = f'Felicitaciones, haz ganado el juego en {tries} intentos, y la palabra era {selected_word}'
else:
    final_message = f'Haz perdido el juego, la palabra era {selected_word}'
    print('    _____\n    |    O \n    |   /|\ \n    |   / \ \n____|_______')

print(final_message)