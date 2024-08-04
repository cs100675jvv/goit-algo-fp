# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Обчислення співвідношення калорій до вартості для кожної страви
    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, info in items_sorted:
        cost = info['cost']
        calories = info['calories']
        
        if budget >= cost:
            selected_items.append(item)
            total_calories += calories
            budget -= cost
    
    return selected_items, total_calories

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    # Ініціалізація масиву dp для зберігання максимальних калорій
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    item_list = list(items.keys())

    # Заповнення масиву dp
    for i in range(1, len(items) + 1):
        item = item_list[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]

    # Відновлення вибору страв
    total_calories = dp[len(items)][budget]
    selected_items = []
    w = budget

    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item = item_list[i-1]
            selected_items.append(item)
            w -= items[item]['cost']

    return selected_items, total_calories

# Функція для запуску та порівняння алгоритмів
def compare_algorithms(items, budget):
    # Запуск жадібного алгоритму
    selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    print("Жадібний алгоритм: ", selected_items_greedy, "Загальна калорійність:", total_calories_greedy)

    # Запуск алгоритму динамічного програмування
    selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
    print("Динамічне програмування: ", selected_items_dp, "Загальна калорійність:", total_calories_dp)

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
compare_algorithms(items, budget)
