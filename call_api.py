import requests
import base64

# Аутентификационные данные
USERNAME = "admin"
PASSWORD = "ping1234"


# Функция для получения списка устройств
def get_devices():
    url = "https:"
    response = requests.get(url, auth=(USERNAME, PASSWORD))

    if response.status_code == 200:
        devices = response.json().get("devices", [])
        print(f"✅ Получены устройства ({len(devices)}): {devices}")
        return devices
    else:
        print(f"❌ Ошибка при получении устройств: {response.status_code} | {response.text}")
        return []


# Функция для запроса user_num
def get_user_num(device_id, password):
    url = f"https://scamera-school.realsoft.ai/device/{device_id}/user_management/queryTheUserListInformation"
    payload = {"password": password, "start": 0, "length": 0}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("user_num", "Not found")
    else:
        print(f"❌ Ошибка для {device_id}: {response.status_code} | {response.text}")
        return None


# Список устройств с паролями
devices_with_passwords = [
    {"device_id": "H010001181A0100010436", "password": "123456"},
    {"device_id": "H010001181A0100011300", "password": "123456"},
    {"device_id": "H010001181A0100010641", "password": "FV9tckqZ"},
    {"device_id": "H010001180F0100010017", "password": "123456"},
    {"device_id": "H010001181A0100010949", "password": "123456"},
    {"device_id": "H010001181A0100011081", "password": "qZ5BGAnt"},
    {"device_id": "H010001181A0100010345", "password": "123456"},
    {"device_id": "H010001181A0100010907", "password": "123456"},
    {"device_id": "H010001181A0100010625", "password": "123456"},
    {"device_id": "H010001181A0100011232", "password": "123456"},
    {"device_id": "H010001181A0100010445", "password": "123456"},
    {"device_id": "H010001181A0100010926", "password": "0055f46ec"},
    {"device_id": "H010001181A0100010841", "password": "f1oJ6YVE"},
    {"device_id": "H010001181A0100010720", "password": "Ua3hgwti"},
    {"device_id": "H010001181A0100010465", "password": "9rxLW0Nh"},
    {"device_id": "H010001181A0100010662", "password": "94fb1887b"},
    {"device_id": "H010001181A0100010387", "password": "r8hbmHX2"},
    {"device_id": "H010001181A0100010781", "password": "nM8aEovh"},
    {"device_id": "H010001181A0100011206", "password": "3kUM3EHd"},
    {"device_id": "H010001181A0100011133", "password": "vHebs5xp"},
    {"device_id": "H010001181A0100010736", "password": "Pqu7HqET"},
    {"device_id": "H010001181A0100010553", "password": "1Lxdc8gL"},
    {"device_id": "H010001181A0100010511", "password": "8Cq0Ur1b"},
    {"device_id": "H010001181A0100011109", "password": "cYe27jgx"},
    {"device_id": "H010001180F0100010019", "password": "123456"},
    {"device_id": "H010001181A0100011222", "password": "SJ8zMeJe"},
    {"device_id": "H010001181A0100010715", "password": "wB0QkIU4"},
    {"device_id": "H010001181A0100010277", "password": "qXNTwGNH"},
    {"device_id": "H010001181A0100010594", "password": "h0LqbSy2"},
    {"device_id": "H010001181A0100010617", "password": "yxvazLGj"},
    {"device_id": "H010001180F0100010019", "password": "123456"},
    {"device_id": "H010001181A0100011169", "password": "123456"},
    {"device_id": "H010001181A0100010915", "password": "123456"},
    {"device_id": "H010001181A0100011312", "password": "123456"}
    # Добавь другие устройства в список
]

# Основной процесс
if __name__ == "__main__":
    all_devices = get_devices()
    for device in devices_with_passwords:
        device_id = device["device_id"]
        password = device["password"]

        if device_id not in all_devices:
            print(f"⚠️ Device ID {device_id} не найден в списке активных устройств!")
            continue

        user_num = get_user_num(device_id, password)
        if user_num is not None:
            print(f"✅ Device ID: {device_id}, User Num: {user_num}")
