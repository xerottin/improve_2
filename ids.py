from sqlalchemy import create_engine, MetaData, select, func


DATABASE_URL="postgresql"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

# Определение таблицы smart_camera
smart_camera = metadata.tables["smart_camera"]

# IDs, которые нужны
smart_camera_ids=[42, 54, 4, 34, 46, 43, 63, 7, 9, 10, 35, 150, 12, 48, 19, 69, 21, 14, 47, 3, 28, 22, 33, 13, 1, 18, 2, 55, 148, 27, 149, 58, 11, 8]

# Создание соединения и выполнение запроса
with engine.connect() as connection:
    query = select(smart_camera.c.device_id, smart_camera.c.password).where(
        smart_camera.c.id.in_(smart_camera_ids)
    )
    result = connection.execute(query)

    # Вывод результатов
    for row in result:
        print(f"device_id: {row.device_id}, passport: {row.password}")
