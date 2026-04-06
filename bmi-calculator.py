weight = float(input("体重を入力してください: "))
height_cm = float(input("身長を入力してください(format-cm): "))
height_m = height_cm/100
#calculation(Expression)BMI = weight/(height*height)
bmi = weight/(height_m**2)
print(f"\nあなたの体重 BMI は　{bmi:.2f}　です。")
if bmi < 18.5:
    print("低体重です。")
elif 18.5<=bmi<25:
    print("普通体重です。")
elif 25<=bmi < 30:
    print("肥満度１です。")
else:
    print("肥満です。")

