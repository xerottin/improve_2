import requests

BASE_URL = "https://api"
tenant_id = 1
date = "2025-03-11"

district_ids = range(139, 210)


def call_api(session, district_id):
    params = {
        "tenant_id": tenant_id,
        "date": date,
        "district_id": district_id
    }

    try:
        response = session.get(BASE_URL, params=params)

        if response.status_code != 200:
            print(f"Failed {district_id}: HTTP {response.status_code}")
            return False

        try:
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Error: Invalid JSON for district_id {district_id}")
            return False

        if response_data.get("status") is True:
            print(f"Success{district_id}")
            return True
        else:
            print(f"Failed{district_id}: {response_data}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error{district_id}: {e}")
        return False


def main():
    with requests.Session() as session:
        for district_id in district_ids:
            if not call_api(session, district_id):
                print("Stopping")
                break


if __name__ == "__main__":
    main()


