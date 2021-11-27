"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    main()





daily_sales_by_SKUs = [
{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def total_sales_volume_for_SKU (items_sold_per_day_per_SKU):
    items_sold_sum = 0
    for item in items_sold_per_day_per_SKU:
        items_sold_sum += item
    return items_sold_sum

for sku in daily_sales_by_SKUs:
    total_sales_vol_per_SKU = total_sales_volume_for_SKU(sku['items_sold'])
    print (f"Cуммарное количество продаж {sku['product']} равно {total_sales_vol_per_SKU}") 


print("___________________")


def average_sales_volume_for_SKU (items_sold_average_SKU):
    items_sold_sum = 0
    for item in items_sold_average_SKU:
        items_sold_sum += item
    items_sold_aver = items_sold_sum / len(items_sold_average_SKU)
    return items_sold_aver

for sku in daily_sales_by_SKUs:
    aver_sales_vol_per_SKU = average_sales_volume_for_SKU(sku['items_sold'])
    print (f"Cреднее количество продаж {sku['product']} равно {aver_sales_vol_per_SKU}")


print("___________________")


def total_sales_volume_for_SKU (items_sold_per_day_per_SKU):
    items_sold_sum = 0
    for item in items_sold_per_day_per_SKU:
        items_sold_sum += item
    return items_sold_sum

def total_sales_vol (list_skus):
    tot_sales_vol=0
    for sku in daily_sales_by_SKUs:
        total_sales_vol_per_SKU = total_sales_volume_for_SKU(sku['items_sold'])
        tot_sales_vol += total_sales_vol_per_SKU
    return tot_sales_vol

    
result_total_sales = total_sales_vol (daily_sales_by_SKUs)
print (f"Cуммарное количество продаж равно {result_total_sales}")


print("___________________")


def average_sales_volume_for_SKU (items_sold_average_SKU):
    items_sold_sum = 0
    for item in items_sold_average_SKU:
        items_sold_sum += item
    items_sold_aver = items_sold_sum / len(items_sold_average_SKU)
    return items_sold_aver

def average_sales_vol (sales):
    aver_sales_vol=0
    for sku in daily_sales_by_SKUs:
        aver_sales_vol_per_SKU = average_sales_volume_for_SKU(sku['items_sold'])
        aver_sales_vol += aver_sales_vol_per_SKU
    av_sales_vol = aver_sales_vol/len(daily_sales_by_SKUs)
    return av_sales_vol


result_average_sales = average_sales_vol (daily_sales_by_SKUs)
print (f"Cреднее количество продаж равно {result_average_sales}") 

#Не поняла для чего в задании часть с def main() и ниже