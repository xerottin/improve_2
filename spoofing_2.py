import requests

region_ids = range(2,15)

date_list = [
    '17', '18', '19', '20', '21',
    '24', '25', '26', '27', '28'
]

tenant_id = 18

BASE_URL = "https://api"

def call_api(session, tenant_id, date, region_id):
    params = {
        "tenant_id": tenant_id,
        "date": f"2025-02-{date}",
        "region_id": region_id,
    }

    try:
        response = session.get(BASE_URL, params=params)

        if response.status_code != 200:
            print(f"Failed {region_id}, {date}: HTTP {response.status_code}")
            return False

        try:
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Error: Invalid JSON for mtt_id {region_id}, date {date}")
            return False

        if response_data.get("status") is True:
            print(f"true {region_id}, {date}")
            return True
        else:
            print(f"Failed {region_id}, {date} - Response: {response_data}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error {region_id}, {date}: {e}")
        return False


def main():
    with requests.Session() as session:
        for date in date_list:
            for region_id in region_ids:
                if not call_api(session, tenant_id, date, region_id):
                    print("Stopping")
                    break


if __name__ == "__main__":
    main()


