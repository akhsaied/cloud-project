


from PIL import Image
import base64
import io


im = Image.open("G:\\University\\الفصل الاخير\\flask\\static\\images\\pic2.jpg")
data = io.BytesIO()
im.save(data, "JPEG")
encoded_img_data = base64.b64encode(data.getvalue())

print(len(encoded_img_data)*3/4)




