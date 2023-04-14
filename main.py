# import params as params
import requests
from pprint import pprint

with open ("token.txt") as file_object:
    token_vk = file_object.readline().split()
    token_ya = file_object.readline().split()



class Vkusers:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):

        self.params = {
            'access_token': token,
            'v': version
        }

    def _get_photos_vk_load(self, owner_id):
        photos_url = self.url + 'photos.get'
        photos_params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1
        }
        res = requests.get(photos_url, params={**photos_params, **self.params}).json()
        return res

    def photos_vk_sort(self, owner_id):
        data_load = self._get_photos_vk_load(owner_id)
        photos_list = data_load['response']['items']
        photos_list_result = []
        counter = 0
        for photos_dict in photos_list:
            counter += 1
            max_ = 0
            photos_dict_result = {}
            for photos_objeсt in photos_dict['sizes']:
                if photos_objeсt['height'] >= max_:
                    max_ = photos_objeсt['height']
                    max_photos = photos_objeсt['url']
                    name_photos = str(photos_dict['likes']['count'])
                    # if name_photos in photos_list[:counter - 1]['likes']['count']:
                    for k in photos_list_result:
                        if name_photos in k:
                            name_photos = f'{name_photos} {photos_dict["date"]}'
            photos_dict_result[name_photos] = max_photos
            photos_list_result.append(photos_dict_result)

        return photos_list_result


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_path(self, disk_file_path):
        path_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        # path_file = disk_file_path.split('/')[0]
        params = {"path": disk_file_path}
        response = requests.put(url=path_url, headers=headers, params=params)
        # return response.json()

    # def _upload_preview(self, file_path):
    #     upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    #     headers = self.get_headers()
    #     params = {"path": file_path, "overwrite": "true"}
    #     response = requests.get(url=upload_url, headers=headers, params=params)
    #     return response.json()

    def upload(self, disk_file_path, path_to_file):
        # file_path_preview = self._get_path(disk_file_path)
        # file_path = file_path_preview.get('href', '')
        headers = self.get_headers()
        self._get_path(disk_file_path)
        'path': disk_file_path
        for dict in path_to_file:
            for k, v in dict.items():
                url_vk = v
                file_name = str(f"{k}.jpg")
                file_path = disk_file_path + '/' + file_name
                with open(file_name, 'wb') as f:
                    res = requests.get(url=url_vk)
                    f.write(res.content)
                file_upload = self._upload_preview(file_path)
                href_upload = file_upload.get('href', '')
                params = {'path': file_path,
                          'url':get_photos_vk_load}
                response = requests.post(url=href_upload, headers=headers, params=params)
                if response.status_code == 202:
                    print("Success")


if __name__ == '__main__':
    token_vk = 'vk1.a.z8VJQGJyW3nlzhL17sIXD0nfrwPW-CyA2VILozaDIAvWumfs2dkpk0OijW9KPrn0InwMUpe4j_flakN_bUqz-zutI3Z6Yvi9hl2IMtuq6bexd1TDS8iCIxbifEF51OndLKFxcwcMRApTR52Eg0rqotNKwOEMaw5SAkcTjT-pCVn7mY_Edky-GEIJj_zyzNy3xsC81_GIQjdSJ99icXT8Ww'
    client = Vkusers(token_vk, 5.131)
    # pprint(client._get_photos_vk_load('14'))
    pprint(client.photos_vk_sort('14'))
    #
    path_to_file = client.photos_vk_sort('14')
    disk_file_path = 'Vk'
    token_ya = 'y0_AgAAAAAJqIy2AADLWwAAAADe6oGCT3eoF5yoTdG2Ge-LXh6hXQYs858'
    uploader = YaUploader(token_ya)
    result = uploader.upload(disk_file_path, path_to_file)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
