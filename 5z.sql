-- логин, пароль всех покупателей 
SELECT login, password FROM users;

-- информация про товар "МЯЧ"
SELECT info AS info_ball FROM item WHERE name="мяч";

-- вывод к-во покупок по названию товара
SELECT SUM(amount) as "СУММА" FROM history 
where item_item = (SELECT id FROM item WHERE name = "сетка");

-- вывод имени товара, информации о нем и к-ва покупок
SELECT
name AS item_name,info,
(SELECT sum(amount) FROM history 
WHERE item_item = item.id )FROM item;

-- по логину и паролю вывести названия всех купленных товаров в обратном алфавитном порядке
SELECT name as  "result" FROM item 
WHERE id in (SELECT item_item  FROM history 
WHERE user_id = (SELECT id FROM users 
WHERE users.login = "anton.d" AND users.password = "abcd")) ORDER BY result DESC ;




