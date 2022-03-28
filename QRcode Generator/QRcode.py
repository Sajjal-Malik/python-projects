import qrcode 
import image

qr = qrcode.QRCode(
    version = 15,   #15 means version of the qr code higher the number bigger the code image and complicated will be the picture
    box_size = 10,   #Size of the box where code will be displayed
    border = 5     #It will be the white part of the image  -- border in all 4 side with white color
)

data_to_seen_after_code_scan = " Hello this is Mr Malik here, I am doing these python projects for my Practice and Logic Building";  #Here we can even give any link for redirection but I have just Passed the String It's upto you !

qr.add_data(data_to_seen_after_code_scan)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("QRCODE.png")