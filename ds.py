import random

nameees = ["Анна", "Сергей", "Ваня", "Ваня2", "Маша", "Кирилл", "Паша", "Ivan", "Жора", "Костя"]
stats1= ["Активчик", "Не актив"]


users = []

for _ in range(10):
    name = random.choice(nameees)
    age = random.randint(18, 60)
    email = f"{name.lower()}@example.com"
    status = random.choice(stats1)
    
    user = {
        "Имя": name,
        "Возраст": age,
        "Почта имейл": email,
        "Статус": status
    }
    users.append(user)


for user in users:
    print(user)
