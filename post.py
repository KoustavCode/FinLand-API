import requests

HOST = 'http://127.0.0.1'
PORT = '5000'
URL_POST = f'{HOST}:{PORT}/upload-file'

img = open('image5.jpeg', 'rb')
files = {
	'image': img
}

post_img = requests.post(url=URL_POST, files=files)
