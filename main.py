

api_id = '1239727'
api_hash = 'a12d841c6ddd543b2010b8fad15ef1d7'
from telethon import TelegramClient, sync
client = TelegramClient('Sabitov', api_id, api_hash)
client.start()
def convert_time_to_string(dt):
    return f'{dt.hour}:{dt.minute:02}'
import cv2
import numpy as np
from datetime import datetime, timedelta
def get_black_background():
    return np.zeros((500, 500))
start_time = datetime.strptime('2019-01-01', '%Y-%m-%d') 
end_time = start_time + timedelta(days=1)

def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (int(image.shape[0]*0.35), int(image.shape[1]*0.5)), font, 1.5, (255, 255, 0), 2, cv2.LINE_AA)
    return image

while start_time < end_time:
    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text)
    cv2.imwrite(f'E:\AUDIO_TS\\time_images/{text}.jpg', image)
    start_time += timedelta(minutes=1)
    from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time
prev_update_time = 'qalesan:'
while True:
    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(datetime.now())
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f'E:\AUDIO_TS\\time_images/{prev_update_time}.jpg')
        client(UploadProfilePhotoRequest(file))
    
