import requests


def main():
    # 1600023 -> '東京都新宿区西新宿'
    # 入力
    zipcode = str(input("input zipcode ? > "))
    url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'

    # 計算
    response = requests.get(url)  # import requests必要

    # 出力
    if response.json()['status'] == 200:
        address = response.json()["results"][0]

        都道府県 = address["address1"]  # 東京都
        市区町村 = address["address2"]  # 新宿区
        町域 = address["address3"]  # 西新宿
        print(f'{都道府県} {市区町村} {町域}')

    else:
        print(response.json()['message'])


if __name__ == '__main__':
    main()
