import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import time

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIBl0eG1xROswrvwKd2ddOAYtDfNt-i9XOqw&usqp=CAU"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(img)
ax.axis('off')
plt.show()