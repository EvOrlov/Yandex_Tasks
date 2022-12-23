CREATE TABLE IF NOT EXISTS Cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    population INTEGER,
    founded TEXT,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES Countries (id) ON DELETE CASCADE
);

INSERT INTO Cities (name, population, founded, country_id)
    VALUES
('Москва', 13010012, '1147', 1),
('Санкт-Петербург', 5351935, '1703', 1),
('Тюмень', 847488, '1586', 1),
('Владивосток', 603519, '1860', 1),
('Краснодар ', 899541, '1794', 1),
('Минск', 1996600, '1067', 2),
('Жодино', 65451, '1963', 2),
('Витебск', 360400, '974', 2),
('Дели', 9879172, '500 до нэ', 3),
('Мумбаи', 15414288, '1507', 3),
('Бангалор', 8443675, '1537', 3);

CREATE TABLE IF NOT EXISTS Countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    population INTEGER,
    gdp INTEGER
);

INSERT INTO Countries (name, population, gdp)
    VALUES
('Россия', 147182123, 1.82),
('Белоруссия', 9255524, 0.063),
('Индия', 1400000000, 3.535);

CREATE TABLE IF NOT EXISTS Companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city_id INTEGER,
    revenue INTEGER,
    labors INTEGER NOT NULL,
    FOREIGN KEY (city_id) REFERENCES Cities (id) ON DELETE CASCADE
);

INSERT INTO Companies (name, city_id, revenue, labors)
    VALUES
('Infosys', 11, 3.8, 335186),
('Сбербанк', 1, 53.7, 285600),
('Белвест', 8, 0.003, 2400),
('Магнит', 5, 19.59, 316000),
('Атлант', 6, 0.193, 7308),
('Белаз', 7, 1.1, 9927),
('Reliance Industries', 10, 86.85, 236200),
('Рога и Копыта', 4, 0, 1),
('NTPC Limited', 9, 17.1, 15786),
('Газпром', 2, 112.2, 479200),
('Бульба продакшн', 8, 0.2, 999);

SELECT cn.name AS Страна, COUNT(cm.name) AS Компаний
FROM Companies cm
    JOIN Cities ct ON ct.id = cm.city_id
    JOIN Countries cn ON cn.id = ct.country_id
WHERE labors >= 1000
GROUP BY cn.name
ORDER BY cn.name;
