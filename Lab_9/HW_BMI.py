# PROBLEM
#Calculate your body mass index (BMI), given formula BMI = w/(h*h)

body_mass = 108
body_height = 1.91

BMI = (body_mass / (body_height**2))

bmi = round(BMI, 2)

print(BMI)
print(f'Evaluated BMI index of your body is : {bmi} [ kg / meters]')

# #### Body mass index  calculator

# print('Body mass index  calculator')

# mass = input('Моля въвведете масата на Вашето тяло в килограми:  ')
# height = input('Моля въвведете височината на Вашето тяло в метри:  ')

# # Тук трябва да конвентирам НИЗА в РАЦИОНАЛНИ числа
# m = mass.float
# h = height.float

# BMI_2 = (m / (h**2))

# bmi_2 = round(BMI_2, 2)

# print(BMI_2)
# print(f'Evaluated BMI index of your body is : {bmi} [ kg / meters]')