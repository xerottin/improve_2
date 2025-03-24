from sqlalchemy import create_engine, MetaData, select, func

# Подключение к БД
DATABASE_URL = "postgresql:"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

# Определение таблиц
smart_camera = metadata.tables["smart_camera"]
identity_smart_camera = metadata.tables["identity_smart_camera"]


# Функция для разбиения списка
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


# Создание соединения
with engine.connect() as connection:
    # Получаем id и device_id только активных камер
    query_smart_camera = (
        select(smart_camera.c.id, smart_camera.c.device_id)
        .where(smart_camera.c.is_active == True)  # Фильтрация по is_active=True
    )
    result_smart_camera = connection.execute(query_smart_camera)

    smart_camera_info = {row.id: row.device_id for row in result_smart_camera.fetchall()}
    smart_camera_ids = list(smart_camera_info.keys())

    if smart_camera_ids:
        all_results = {}

        # Разбиваем ID на части (например, по 200)
        for chunk in chunk_list(smart_camera_ids, 200):
            query_count = (
                select(
                    identity_smart_camera.c.smart_camera_id,
                    func.count().label("count")
                )
                .where(identity_smart_camera.c.smart_camera_id.in_(chunk))
                .group_by(identity_smart_camera.c.smart_camera_id)
            )
            result_count = connection.execute(query_count)

            for row in result_count:
                all_results[row.smart_camera_id] = row.count

        # Вывод всех данных (device_id + count)
        for smart_camera_id in smart_camera_ids:
            device_id = smart_camera_info.get(smart_camera_id, "Нет данных")
            count = all_results.get(smart_camera_id, 0)  # Если нет записей в identity_smart_camera, count = 0
            print(f"smart_camera_id: {smart_camera_id}, device_id: {device_id}, count: {count}")

    else:
        print("Нет данных в smart_camera")
