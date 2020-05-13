def days_to_million(deposit_1, deposit_2):
    day_n_balance = deposit_1 + deposit_2
    day_n_take_1_balance = deposit_1
    days = 2

    while(day_n_balance < 1000000):
        days += 1
        new_balance = day_n_balance + day_n_take_1_balance
        day_n_take_1_balance = day_n_balance
        day_n_balance = new_balance

    return days


def balance_at_million(deposit_1, deposit_2):
    day_n_balance = deposit_1 + deposit_2
    day_n_take_1_balance = deposit_1
    days = 2

    while(day_n_balance < 1000000):
        days += 1
        new_balance = day_n_balance + day_n_take_1_balance
        day_n_take_1_balance = day_n_balance
        day_n_balance = new_balance

    return day_n_balance


max_days = 0

for x in range(1, 1000000):
    for y in range(1, 1000000):
        million_balance = balance_at_million(x, y)
        if(million_balance == 1000000):
            days_taken = days_to_million(x, y)
            if(days_taken > max_days):
                max_days = days_taken
                print(str(x) + " " + str(y) + " " + str(days_taken))
