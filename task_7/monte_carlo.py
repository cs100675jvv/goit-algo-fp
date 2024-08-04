import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Ініціалізація підрахунку кожної можливої суми
    sums_count = {sum_val: 0 for sum_val in range(2, 13)}
    
    # Виконання симуляції
    for _ in range(num_rolls):
        # Кидок двох кубиків
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        
        # Збільшення підрахунку для відповідної суми
        sums_count[roll_sum] += 1

    return sums_count

def calculate_probabilities(sums_count, num_rolls):
    probabilities = {}
    for sum_val, count in sums_count.items():
        # Обчислення ймовірності кожної суми
        probabilities[sum_val] = (count / num_rolls) * 100
    return probabilities

def plot_probabilities(probabilities):
    # Створення графіка ймовірностей
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, color='blue', alpha=0.7)
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірність кожної суми при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    num_rolls = 1000000  # Кількість симуляцій
    sums_count = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(sums_count, num_rolls)

    # Виведення результатів
    print("Результати симуляції:")
    for sum_val in range(2, 13):
        print(f"{sum_val} - {probabilities[sum_val]:.2f}%")

    # Порівняння з аналітичними значеннями
    analytical_probabilities = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    print("\nАналітичні ймовірності:")
    for sum_val, prob in analytical_probabilities.items():
        print(f"{sum_val} - {prob:.2f}%")

    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
