import numpy
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

#Функция Y=cos(3*x-15)*(x-1) вид экстремума Минимум интервал [-10 10]
#Чтобы было проще искать минимум функции cos(3*x-15)*(x-1) мы преобразуем ее
#в функцию с минусом Y=-(cos(3*x-15)*(x-1)) и будем искать ее максимум.


#Задание функции Y=(x-1)*cos(3x+15)
def Myfunction(x):
    y = -(numpy.cos(3*x - 15)*(x - 1))
    return y

#Вычисление соответствующего вещественного числа (Перевод из 2 в 10 систему)
def converter(my_mass):
    num=(int((''.join(map(str, my_mass))),2))
    real= -10 + num * ((10 - (-10)) / ((2**15) - 1))
    return real

#Получение массива Значнеий функции
def mass_function(population):
    #print(f"\nПопуляция для фитнес функции =\n{population}\n")
    FF = list(map(converter, population))
    s = list(map(Myfunction, FF))
    return s

#Вычисление особей для промежуточных популяций (Рулетка)
def comulata(mass):
    mass = mass - mass.min() + 1
    # massa = []
    # for i in mass:
    #     massa.append(i - min(mass) + 1)
    # mass = massa
    delit=mass.sum()
    prob=(mass/delit)
    # prob = []
    # for i in mass:
    #     prob.append(i/delit)
    print("_____________________________________________________" )
    print("Вероятности=",prob)
    print("Cумма вероятностей=",prob.sum())
    cumulata = [0, prob[0], ]
    for i in range(1, len(prob)):
        cumulata.append(prob[i] + cumulata[-1])
    print(f"\nКамулята=\n{cumulata}\n")
    print(f"Мощность популяции={num_parents_mating}")
    col_vo = numpy.zeros(len(prob))
    i=0
    while i<num_parents_mating:
        chislo = random.uniform(0,1)  
        proverka:bool = False
        e = 0
        end = len(cumulata)-1
        while not proverka:
            while e != end:
                if cumulata[e] <= chislo < cumulata[e+1]:
                    col_vo[e] += 1
                    e = end
                    proverka = True
                    i += 1
                else:
                    e += 1
    print(f"\nМассив попаданий=\n{col_vo}\n")
    print("_____________________________________________________" )
    return col_vo

#Оператор Репордуции
def reproductio(pool,camulata):
    i = 0
    intere_pool = []
    #print(f"\nПоступивший пул в репродукцию =\n{pool}\n Камулята=\n{camulata}\n")
    while i < len(camulata):
        while camulata[i] > 0: 
          intere_pool.append(pool[i])
          camulata[i]-=1
        i+=1
    # intere_pool=numpy.array(intere_pool) 
    # intere_pool=intere_pool.tolist()
    #print(f"\nПромежуточный пул после репродукции \n{intere_pool}\n") 
    return intere_pool

# Оператор Кросинговера с вероятностью 0.5
def crossingover(pool):
    shans=random.random()
    if shans<0.35:
         return pool
    else:
        size = (num_parents_mating) - 1
        proverka = False
        while proverka == False:
            xx=random.randint(0, size)
            xy=(int)(random.uniform(0,size))
            if xx == xy:
                proverka = False
            else:
                proverka = True
        k = random.randint(0,num_gen-1)
        pool[xx][k], pool[xy][k] = pool[xy][k], pool[xx][k]
        # num=pool[xx][k]
        # pool[xx][k]= pool[xy][k]
        # pool[xy][k]=num
        return pool

#Оператор Мутации с вероятность 0,001
def mutation(pool):
    lep = 0
    while lep < (len(pool) - 1):
        k = random.randint(0,100)
        if k <= 1:
            k = random.randint(0,num_gen-1)
            if pool[lep][k] == 1:
                pool[lep][k] = 0
                lep += 1
            else:
                pool[lep][k] = 1
                lep += 1   
        else:
             lep += 1
    return pool


 
#Функция построения графика по значениям x и y
def grafic(x_mass,y_mass,num_gen):
    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (1024 / dpi, 640 / dpi) )
    mpl.rcParams.update({'font.size': 10})
    plt.axis([-10, 10, -12, 12])#Координатная плоскость
    plt.title(f'Популяция {num_gen}')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    xs = []
    cos_vals = []
    x = -10.0
    while x < 20.0:
        cos_vals += [ (numpy.cos(3*x - 15)*(x - 1)) ]
        xs += [x]
        x += 0.01
    plt.plot(xs, cos_vals, color = 'blue', linestyle = 'solid',label = 'F(x) = (x-1)cos(3x-15)')
    size=len(x_mass)
    for i in range(size):
        plt.scatter(x_mass[i], y_mass[i], color ='green', s = 60, marker = '*')
    fig.savefig(f'Популяция {num_gen}.png')


# Количество генов
num_gen = 15
#Количество поколений
num_generations = 60

#Размер (мощность) популяции 
num_parents_mating =30

#РАЗМЕР матрицы для хранения Хромосом Мощность x Кол-во Генов
pop_size = (num_parents_mating, num_gen)

#Интервал (левая и правая границы X)
left = -10
right = 10

#Генерируем поколение
#Случайно  с установленной размерностью (двумерная матрица из 1 и 0)
first_population = numpy.random.randint(2, size=(pop_size ), dtype=numpy.uint8)


#Повторяется заданное кол-во раз (Установите кол-во поколений)
for generation in range(num_generations):
    print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nПоколение №{generation+1}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f'\n Текущая популяция=\n')
    for x in first_population: print(x)
    #Фитнес функции 
    re=mass_function(first_population)
    print(f"\nФитнес Функция =\n")
    for x in re: print(x)


    #Генерация графика
    y_graf=re
    y_graf = [i*-1 for i in y_graf]
     #for x in y_graf: print(x)
    x_graf = list(map(converter, first_population))
    grafic(x_graf,y_graf,generation+1)
    #################################
    re = numpy.array(re)
    #Кол-во попаданий в из родителсткого в промежуточный
    camulata=comulata(re)

    #ОР(Промежуточная популяция)
    intere_pool=reproductio(first_population,camulata)

    #Кроссинговер
    child_pool=crossingover(intere_pool)
    print(f"\nПул после кросинговера =\n ")
    for x in child_pool: print(x)

    #Мутация
    child_pool=mutation(intere_pool)
    print(f"\nПул после мутации =\n")
    for x in child_pool: print(x)

    #Потомки стали родителями
    first_population = numpy.array(child_pool, dtype=numpy.uint8)
    re=mass_function(first_population)
    #make_image(image(numpy.array(first_population) * -1, generation), generation)
    y_graf=re
    y_graf = [i*-1 for i in y_graf]
    print(f"\nФитнес Функции  =\n{y_graf}\n")
    print(f"\nНаилучшее значение фитнес функций =\n{min(y_graf)}\n")

    
    print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


