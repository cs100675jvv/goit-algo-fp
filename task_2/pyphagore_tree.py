import turtle
import math

def draw_pythagoras_tree(t, length, depth):
    if depth == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    t.left(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)
    t.right(90)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)
    t.left(45)
    t.backward(length)

def main():
    # Запитати у користувача рівень рекурсії
    depth = int(input("Введіть рівень рекурсії: "))

    # Ініціалізація вікна turtle
    screen = turtle.Screen()
    screen.title("Фрактал 'дерево Піфагора'")
    t = turtle.Turtle()
    t.speed(0)

    # Початкове положення і орієнтація
    t.up()
    t.goto(0, -200)
    t.down()
    t.left(90)

    # Малюємо дерево Піфагора
    draw_pythagoras_tree(t, 100, depth)

    # Завершення
    turtle.done()

if __name__ == "__main__":
    main()
