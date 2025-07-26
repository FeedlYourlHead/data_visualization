import matplotlib.pyplot as plt

# Переменные
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Назначение стиля \/
plt.style.use('bmh')

fig, ax = plt.subplots()
# Построение графика
ax.plot(input_values, squares, linewidth=3)

# Назначение загаловка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', labelsize=14)

plt.show()
