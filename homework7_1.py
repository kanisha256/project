import time

time_to_start = int(input("Введите количество секунд до старта ракеты: "))
while time_to_start:
    print(f"До старта осталось: {time_to_start}       ", end="\r")
    time.sleep(1) 
    time_to_start = time_to_start - 1
print("\nСТАРТ!!!")
