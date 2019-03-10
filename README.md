# Ants-algorithm
1.Введем матрицу расстояний

2.Инициализируем параметры алгоритма n_ants alpha beta q,r

3.Инициализируем короткий путь как бесконечность

4.Для каждой итерации ,т.е для каждого муравья построим маршруты и рассчитаем вес по следующей формуле:

(![equation](https://latex.codecogs.com/gif.latex?P_%7Bij%7D%3D%5Cfrac%7B%5Ctau_%7Bij%7D%5E%7B%5Calpha%20%7D%28%5Cfrac%7B1%7D%7Bd_%7Bij%7D%7D%29%5E%7B%5Cbeta%20%7D%7D%7B%5Csum_%7Bj%5Cin%20allowed%20nodes%7D%5Ctau_%7Bij%7D%5E%7B%5Calpha%20%7D%28%5Cfrac%7B1%7D%7Bd_%7Bij%7D%7D%29%5E%7B%5Cbeta%20%7D%7D))

![equation](https://latex.codecogs.com/gif.latex?%5Ctau%20i%20j)- уровень феромона

![equation](https://latex.codecogs.com/gif.latex?d%20i%20j)- расстояния между i и j

![equation](https://latex.codecogs.com/gif.latex?%5Calpha%20%2C%5Cbeta)- константы

5.Проверяем все новые пути для выбора наикрайтчайшего 

  для каждого ребра обновляем уровень феромона по формуле:
 ![equation](https://latex.codecogs.com/gif.latex?%5Ctau%20_%7Bij%7D%28t&plus;1%29%3D%281-%5Crho%20%29%5Ctau%20_%7Bij%7D%28t%29&plus;%5Csum_%7Bk%5Cin%20colonyThatUsedEdge%28i%2Cj%29%7D%5Cfrac%7BQ%7D%7BL_%7Bk%7D%7D)
  
  ![equation](https://latex.codecogs.com/gif.latex?%5Crho)- скорость испарения феромона
  
  ![equation](https://latex.codecogs.com/gif.latex?L_%5Ek)- цена текущего решения для k-го муравья
  
  ![equation](https://latex.codecogs.com/gif.latex?Q)- значение ценового порядка оптимального решения
  
  ![equation](https://latex.codecogs.com/gif.latex?Q/L_%5Ek%28t%29)- феромон, осажденный k-м муравьем с помощью ребра (i, j)

6. напечатать вес крайтчайшего пути 
