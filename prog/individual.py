import os

print("Имя текущего пользователя: ", os.getlogin())
print("Текущая дериктория: ", os.getcwd())
print("СОдержимое дериктории: ", os.listdir())