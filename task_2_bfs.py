from collections import deque

# Граф метро Санкт-Петербурга (представлен в виде словаря)
metro_graph_spb = {
    "Площадь Восстания": ["Маяковская", "Владимирская", "Чернышевская"],
    "Маяковская": ["Гостиный двор", "Площадь АН.1"],
    "Владимирская": ["Достоевская", "Пушкинская"],
    "Гостиный двор": ["Невский проспект", "Василеостровская"],
    "Площадь АН.1": ["Елизаровская", "Площадь АН.2"],
    "Достоевская": ["Спаская", "Лиговский проспект", "Владимирская"],
    "Пушкинская": ["ТИ.1", "Звенигородская"],
    "Невский проспект": ["Гостиный двор", "Сенная площадь", "Горьковская"],
    "Площадь АН.2": ["Площадь АН.1", "Лиговский проспект", "Новочеркасская"],
    "Лиговский проспект": ["Площадь АН.2", "Достоевская"],
    "Спаская": ["Садовая", "Сенная площадь", "Достоевская"],
    "Сенная площадь": ["Спасская", "Невский проспект", "Садовая"],
    "Садовая": ["Спаская", "Сенная площадь", "Адмиралтейская", "Звенигородская"],
    "ТИ.1": ["ТИ.2", "Балтийская"],
    "ТИ.2": ["ТИ.1", "Сенная площадь", "Фрунзенская"],
    "Звенигородская": ["Садовая", "Обводный канал", "Пушкинская"]
}


def shortest_path_bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_station, path = queue.popleft()
        visited.add(current_station)

        if current_station == goal:
            return path

        for neighbor_station in graph.get(current_station, []):
            if neighbor_station not in visited:
                queue.append((neighbor_station, path + [neighbor_station]))

    return None


start_station = "Площадь Восстания"
goal_station = "Обводный канал"

shortest_path = shortest_path_bfs(metro_graph_spb, start_station, goal_station)

if shortest_path:
    print(f"Кратчайший маршрут от станции {start_station} до станции {goal_station}:")
    print(" -> ".join(shortest_path))
else:
    print(f"Маршрут между станциями {start_station} и {goal_station} не найден.")
