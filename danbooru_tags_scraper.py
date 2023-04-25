import requests


def scraper():
    base_url = "https://danbooru.donmai.us"
    tags_endpoint = "/tags.json"

    page_number = 1
    all_tags = []

    with open("./tags.txt", mode='w') as file:
        while True:
            params = {"search[order]": "name", "search[hide_empty]": True, "limit": 1000, "page": page_number}

            response = requests.get(base_url + tags_endpoint, params=params)

            if response.status_code != 200:
                print(f"Error fetching tags. Status code: {response.status_code}")
                break

            tags_data = response.json()
            all_tags.extend(tags_data)
            if len(tags_data) == 0:
                break

            tags_names = [tag_data["name"] for tag_data in tags_data]

            for tag in tags_names:
                file.write(tag + '\n')

            page_number += 1

    print(f"Total tags downloaded: {len(all_tags)}")


def main():
    scraper()


if __name__ == "__main__":
    main()
