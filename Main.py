
import tkinter as tk
import sys
import time
import random

secondes = time.time()
secondes = int(secondes)
print("Seconds =", secondes)
pos_rect_x = 125
pos_rect_y = 75
matrix_x = 1
matrix_y = 0
orientation_memory = 0
snake = []
fruit = 0

def fruit_generation():
    fruit = [random.randint(0, 39), random.randint(0, 27)]
    print(fruit[0], fruit[1])
    return fruit

fruit_pos = fruit_generation()

def key_pressed(event):
    global matrix_x
    global matrix_y
    global orientation_memory # 0: Serpent Tête a droite, 1: Serpent tête en bas, 2 : Serpent tête a gauche, 3 : Serpent tête en haut
    global fruit_pos
    global fruit
    global fruit_draw
    size_snake = len(snake)
    if (event.keycode == 111): #UP 3
        canvas.move(snake[0], 0, -25)
        for i in range (1, size_snake):
            if orientation_memory == 0:
                canvas.move(snake[i], 25, 0)
                orientation_memory = 3
                matrix_y -= 1
            elif orientation_memory == 1:
                print("Perdu")
                sys.exit(0)
            elif orientation_memory == 2:
                canvas.move(snake[i], -25, 0)
                orientation_memory = 3
                matrix_y -= 1
            elif orientation_memory == 3 :
                canvas.move(snake[i], 0, -25)
                matrix_y -= 1

    elif (event.keycode == 114): #Right 0
        canvas.move(snake[0], 25, 0)
        for i in range(1, size_snake):
            if orientation_memory == 0:
                canvas.move(snake[i], 25, 0)
                matrix_x += 1
            elif orientation_memory == 1 :
                canvas.move(snake[i], 0, 25)
                orientation_memory = 0
                matrix_x += 1
            elif orientation_memory == 2:
                print("Perdu")
                sys.exit(0)
            elif orientation_memory == 3:
                canvas.move(snake[i], 0, -25)
                orientation_memory = 0
                matrix_x += 1

    elif (event.keycode == 116): #DOWN 1
        canvas.move(snake[0], 0, 25)
        for i in range (1, size_snake):
            if orientation_memory == 0:
                canvas.move(snake[i], 25, 0)
                orientation_memory = 1
                matrix_y += 1
            elif orientation_memory == 1:
                canvas.move(snake[i], 0, 25)
                matrix_y += 1
            elif orientation_memory == 2:
                canvas.move(snake[i], -25, 0)
                orientation_memory = 1
                matrix_y += 1
            elif orientation_memory == 3:
                print ("Perdu")
                sys.exit(0)

    elif (event.keycode == 113): #LEFT 2
        canvas.move(snake[0], -25, 0)
        for i in range(1, size_snake):
            if orientation_memory == 0:
                print("Perdu")
                sys.exit(0)
            elif orientation_memory == 1:
                canvas.move(snake[i], 0, 25)
                orientation_memory = 2
                matrix_x -= 1
            elif orientation_memory == 2:
                canvas.move(snake[i], -25, 0)
                matrix_x -= 1
            elif orientation_memory == 3:
                canvas.move(snake[i], 0, -25)
                orientation_memory = 2
                matrix_x -= 1


    if (matrix_y == -1) or (matrix_y == 28):
        print(matrix_y)
        print("Perdu")
        sys.exit(0)

    elif (matrix_x == -1) or (matrix_x == 40):
        print(matrix_x)
        print("Perdu")
        sys.exit(0)

    if (matrix_x == fruit_pos[0]) and (matrix_y == fruit_pos[1]):
        print ("TUTUTUTU")
        canvas.delete(fruit_draw)
        fruit_pos = fruit_generation()
        fruit_draw = canvas.create_rectangle(25 * fruit_pos[0], (25 + 25 * fruit_pos[1]), (25 + 25 * fruit_pos[0]),
                                             25 * fruit_pos[1],
                                             outline='yellow')


window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=700, bg = 'black')
canvas.pack()
snake.append(canvas.create_rectangle(25, 0, 50, 25, outline = 'red'))
snake.append(canvas.create_rectangle(0, 0, 25, 25, outline = 'red'))
fruit_draw = canvas.create_rectangle(25*fruit_pos[0], (25+25*fruit_pos[1]), (25+25*fruit_pos[0]), 25*fruit_pos[1],
                                     outline = 'yellow')

canvas.bind_all("<KeyPress>", key_pressed)
canvas.mainloop()
