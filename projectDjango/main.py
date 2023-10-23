from btest.models import *

# Первые блюда
meal1 = Meal(name='Борщ', weight=250, calories=360)
meal1.save()
meal2 = Meal(name='Солянка', weight=300, calories=420)
meal2.save()
meal3 = Meal(name='Рассольник', weight=250, calories=150)
meal3.save()
meal4 = Meal(name='Уха', weight=300, calories=170)
meal4.save()
meal5 = Meal(name='Окрошка', weight=250, calories=200)
meal5.save()

# Вторые блюда
meal6 = Meal(name='Бефстроганов', weight=200, calories=420)
meal6.save()
meal7 = Meal(name='Котлета по-киевски', weight=150, calories=310)
meal7.save()
meal8 = Meal(name='Жаркое', weight=250, calories=610)
meal8.save()
meal9 = Meal(name='Плов', weight=300, calories=650)
meal9.save()
meal10 = Meal(name='Голубцы', weight=200, calories=340)
meal10.save()

# Закуски
meal11 = Meal(name='Салат "Оливье"', weight=150, calories=180)
meal11.save()
meal12 = Meal(name='Сельдь под шубой', weight=200, calories=240)
meal12.save()
meal13 = Meal(name='Винегрет', weight=150, calories=130)
meal13.save()
meal14 = Meal(name='Салат "Цезарь"', weight=200, calories=350)
meal14.save()
meal15 = Meal(name='Сырные шарики', weight=100, calories=250)
meal15.save()

# Напитки
meal16 = Meal(name='Чай', weight=200, calories=2)
meal16.save()
meal17 = Meal(name='Кофе', weight=200, calories=5)
meal17.save()
meal18 = Meal(name='Сок', weight=200, calories=120)
meal18.save()
meal19 = Meal(name='Компот', weight=200, calories=80)
meal19.save()
meal20 = Meal(name='Минеральная вода', weight=200, calories=0)
meal20.save()


# Комбинации обедов
lunch1 = Lunch(name='Завтрак Царя', description='Борщ, Котлета по-киевски, Салат "Оливье", Чай', price=450)
lunch1.save()
lunch2 = Lunch(name='Балтийский Бриз', description='Солянка, Бефстроганов, Винегрет, Кофе', price=500)
lunch2.save()
lunch3 = Lunch(name='Сибирская Симфония', description='Рассольник, Жаркое, Сельдь под шубой, Сок', price=550)
lunch3.save()
lunch4 = Lunch(name='Уральский Уют', description='Уха, Плов, Салат "Цезарь", Компот', price=600)
lunch4.save()
lunch5 = Lunch(name='Кавказская Каприз', description='Окрошка, Голубцы, Сырные шарики, Минеральная вода', price=400)
lunch5.save()
lunch6 = Lunch(name='Московский Микс', description='Борщ, Бефстроганов, Салат "Оливье", Чай', price=450)
lunch6.save()
lunch7 = Lunch(name='Киевский Коллаж', description='Солянка, Котлета по-киевски, Винегрет, Кофе', price=500)
lunch7.save()
lunch8 = Lunch(name='Санкт-Петербургский Пир', description='Рассольник, Жаркое, Сельдь под шубой, Сок', price=550)
lunch8.save()
lunch9 = Lunch(name='Татарский Тандем', description='Уха, Плов, Салат "Цезарь", Компот', price=600)
lunch9.save()
lunch10 = Lunch(name='Узбекский Удивитель', description='Окрошка, Голубцы, Сырные шарики, Минеральная вода', price=400)
lunch10.save()


