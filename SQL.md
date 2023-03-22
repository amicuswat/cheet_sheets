### 1.1

```sql
SELECT model, speed, hd
FROM pc
WHERE price < 500
```

### 2.1
группируем при помощи DISTINCT
```sql
SELECT DISTINCT maker
FROM product
WHERE type = 'Printer'
```

### 3.1
```sql
SELECT model, ram, screen
FROM laptop
WHERE price > 1000
```

### 4.1
```sql
SELECT *
FROM printer
WHERE color = 'y'
```

### 5.1
Фильтруем по нескольким условиям
```sql
SELECT model, speed, hd
FROM pc
WHERE (cd = '12x' or cd = '24x') and price < 600
```

### 6.2
Объединяем 2 таблицы
```sql
SELECT DISTINCT Product.maker, Laptop.speed
FROM Product
left join Laptop
on Product.model = Laptop.model
WHERE Laptop.hd >= 10
```

### 7.2
Предложение UNION приводит к появлению в результирующем наборе всех строк каждого из запросов. При этом, если определен параметр ALL, то сохраняются все дубликаты выходных строк, в противном случае в результирующем наборе присутствуют только уникальные строки. Заметим, что можно связывать вместе любое число запросов. Кроме того, с помощью скобок можно задавать порядок объединения.

Операция объединения может быть выполнена только при выполнении следующих условий:

 количество выходных столбцов каждого из запросов должно быть одинаковым;

 выходные столбцы каждого из запросов должны быть совместимы между собой (в порядке их следования) по типам данных;

 в результирующем наборе используются имена столбцов, заданные в первом запросе;

 предложение ORDER BY применяется к результату соединения, поэтому оно может быть указано только в конце всего составного запроса.
```sql
SELECT Product.model, price
FROM Product 
INNER JOIN PC
ON Product.model = PC.model
WHERE maker = 'B'
UNION
SELECT Product.model, price
FROM Product
INNER JOIN Laptop
ON Product.model = Laptop.model
WHERE maker = 'B'
UNION
SELECT Product.model, price
FROM Product
INNER JOIN Printer
ON Product.model = Printer.model
WHERE maker = 'B'
```

### 8.2
Выбираем все кроме
```sql
SELECT maker
FROM Product
WHERE type = 'PC'
EXCEPT
SELECT maker
FROM Product
WHERE type = 'Laptop'
```

### 9.1
```sql
SELECT DISTINCT maker
FROM Product
INNER JOIN PC
ON Product.model = PC.model
WHERE speed >= 450
```
