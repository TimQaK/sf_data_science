import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число"""
    count = 0
    predict_number = 50  # переносим вне цикла, чтобы сохранялся прогресс

    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number < number:
            predict_number += 10
        elif predict_number > number:
            predict_number -= 1
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    
    score_game(random_predict)
