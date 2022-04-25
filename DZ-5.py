# Задание №5

rating = [7, 5, 3, 3, 2]
while True:
    user_number = int(input('Введите число'))
    rating.append(user_number)
    rating = sorted(rating, reverse=True)
    print(rating)