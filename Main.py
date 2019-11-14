
import tkinter as tk
import sys
import time
import random

secondes = time.time()
print("Seconds =", secondes)
matrix_x = 1
matrix_y = 0
orientation_memory = 0
snake = []
fruit = 0
snake_queue = 0
check_queue = True
def fruit_generation():
    fruit = [random.randint(0, 39), random.randint(0, 27)]
    print(fruit[0], fruit[1])
    return fruit

fruit_pos = fruit_generation()

def moveUp(orientation_memory):
    global matrix_x
    global matrix_y
    global check_queue
    size_snake = len(snake)
    old_orientation = orientation_memory
    canvas.move(snake[0], 0, -25)
    if orientation_memory == 0:
        for i in range(1, size_snake):
            canvas.move(snake[i], 25, 0)
            orientation_memory = 3
        matrix_y -= 1
        return orientation_memory
    elif orientation_memory == 1:
        print("Perdu")
        sys.exit(0)
    elif orientation_memory == 2:
        for i in range(1, size_snake):
            canvas.move(snake[i], -25, 0)
            orientation_memory = 3
        matrix_y -= 1
        return orientation_memory
    elif orientation_memory == 3:
        for i in range(1, size_snake):
            canvas.move(snake[i], 0, -25)
        matrix_y -= 1
        return orientation_memory

def moveDown(orientation_memory):
    global matrix_x
    global matrix_y
    size_snake = len(snake)
    canvas.move(snake[0], 0, 25)
    if orientation_memory == 0:
        for i in range(1, size_snake):
            canvas.move(snake[i], 25, 0)
            orientation_memory = 1
        matrix_y += 1
        return orientation_memory
    elif orientation_memory == 1:
        for i in range(1, size_snake):
            canvas.move(snake[i], 0, 25)
        matrix_y += 1
        return orientation_memory
    elif orientation_memory == 2:
        for i in range(1, size_snake):
            canvas.move(snake[i], -25, 0)
            orientation_memory = 1
        matrix_y += 1
        return orientation_memory
    elif orientation_memory == 3:
        print("Perdu")
        sys.exit(0)

def moveRight(orientation_memory):
    global matrix_x
    global matrix_y
    size_snake = len(snake)
    canvas.move(snake[0], 25, 0)
    if orientation_memory == 0:
        for i in range (1, size_snake):
            print(i)
            canvas.move(snake[i], 25, 0)
        matrix_x += 1
        return orientation_memory
    elif orientation_memory == 1:
        for i in range(1, size_snake):
            canvas.move(snake[i], 0, 25)
            orientation_memory = 0
        matrix_x += 1
        return orientation_memory
    elif orientation_memory == 2:
        print("Perdu")
        sys.exit(0)
    elif orientation_memory == 3:
        for i in range (1, size_snake):
            canvas.move(snake[i], 0, -25)
            orientation_memory = 0
        matrix_x += 1
        return orientation_memory

def moveLeft(orientation_memory):
    global matrix_x
    global matrix_y
    size_snake = len(snake)
    canvas.move(snake[0], -25, 0)
    if orientation_memory == 0:
        print("Perdu")
        sys.exit(0)
    elif orientation_memory == 1:
        for i in range(1, size_snake):
            canvas.move(snake[i], 0, 25)
            orientation_memory = 2
        matrix_x -= 1
        return  orientation_memory
    elif orientation_memory == 2:
        for i in range(1, size_snake):
            canvas.move(snake[i], -25, 0)
        matrix_x -= 1
        return  orientation_memory
    elif orientation_memory == 3:
        for i in range(1, size_snake):
            canvas.move(snake[i], 0, -25)
            orientation_memory = 2
        matrix_x -= 1
        return orientation_memory

def automove(orientation_memory):
    seconds_3 = ""
    seconds_2 = time.time()
    seconds_2 = seconds_2 - secondes
    interrupt = True

    if seconds_2 < 10:
        seconds_3 = str(seconds_2)
        check_time = int(seconds_3[2])
        if (check_time % 5 == 0):
            print(check_time)
            if (orientation_memory == 0):
                moveRight(orientation_memory)
            elif (orientation_memory == 1):
                moveDown(orientation_memory)
            elif (orientation_memory == 2):
                moveLeft(orientation_memory)
            elif (orientation_memory == 3):
                moveUp(orientation_memory)
    elif (seconds_2 < 100) and (seconds_2 > 10):
        seconds_3 = str(seconds_2)
        check_time = int(seconds_3[3])
        if (check_time % 5 == 0):
            if (orientation_memory == 0):
                moveRight(orientation_memory)
            elif (orientation_memory == 1):
                moveDown(orientation_memory)
            elif (orientation_memory == 2):
                moveLeft(orientation_memory)
            elif (orientation_memory == 3):
                moveUp(orientation_memory)
        else:
            interrupt = False
    elif (seconds_2 < 1000) and (seconds_2 > 100):
        seconds_3 = str(seconds_2)
        check_time = int(seconds_3[4])
        if (check_time % 5 == 0):
            if (orientation_memory == 0):
                moveRight(orientation_memory)
            elif (orientation_memory == 1):
                moveDown(orientation_memory)
            elif (orientation_memory == 2):
                moveLeft(orientation_memory)
            elif (orientation_memory == 3):
                moveUp(orientation_memory)

def key_pressed(event):
    global matrix_x
    global matrix_y
    global fruit_pos
    global fruit
    global fruit_draw
    global orientation_memory
    size_snake = len(snake)
    if (event.keycode == 111): #UP 3  # 0: Serpent Tête a droite, 1: Serpent tête en bas, 2 : Serpent tête a gauche, 3 : Serpent tête en haut
        orientation_memory = moveUp(orientation_memory)
    elif (event.keycode == 114): #Right 0
        orientation_memory = moveRight(orientation_memory)
    elif (event.keycode == 116): #DOWN 1
        orientation_memory = moveDown(orientation_memory)
    elif (event.keycode == 113): #LEFT 2
        orientation_memory = moveLeft(orientation_memory)


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
                                             outline='yellow') # 0: Serpent Tête a droite, 1: Serpent tête en bas, 2 : Serpent tête a gauche, 3 : Serpent tête en haut
        if orientation_memory == 0:
            snake.append(canvas.create_rectangle(25 * matrix_x + (- 25 * size_snake), matrix_y * 25, 25 + 25 * matrix_x + (- 25 * size_snake),
                                             matrix_y * 25 + 25, outline='red'))
        elif orientation_memory == 1:
            snake.append(canvas.create_rectangle(25 * matrix_x , matrix_y * 25 -( 25 *size_snake),
                                                 25 * matrix_x +25,
                                                 matrix_y * 25 -(25 * size_snake) +25, outline='red'))
        elif orientation_memory == 2:
            snake.append(canvas.create_rectangle(25 * matrix_x + ( 25 * size_snake), matrix_y * 25,
                                                 25 + 25 * matrix_x + ( 25 * size_snake),
                                                 matrix_y * 25 + 25, outline='red'))
        elif orientation_memory == 3:
            snake.append(canvas.create_rectangle(25 * matrix_x , matrix_y * 25 + ( 25 *size_snake),
                                                 25 * matrix_x +25,
                                                 matrix_y * 25 +( 25 * size_snake) +25, outline='red'))

window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=700, bg = 'black')
canvas.pack()
snake.append(canvas.create_rectangle(25, 0, 50, 25, outline = 'red'))
snake.append(canvas.create_rectangle(0, 0, 25, 25, outline = 'red'))

fruit_draw = canvas.create_rectangle(25*fruit_pos[0], (25+25*fruit_pos[1]), (25+25*fruit_pos[0]), 25*fruit_pos[1],
                                     outline = 'yellow')

canvas.bind_all("<KeyPress>", key_pressed)
#automove()
canvas.mainloop()
