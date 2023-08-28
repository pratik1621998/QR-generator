# import qrcode as qr
import qrcode
img = qrcode.make("https://res.cloudinary.com/dl2y4laeg/video/upload/v1684909968/media/video/Instagram_87513363-3566-43f0-a80c-a05c8e900953_psxrfe.mp4")
img.save("demo.png")
