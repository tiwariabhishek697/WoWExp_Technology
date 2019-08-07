from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    
    #for male
    from PIL import Image
    img_male_left =Image.open("C:/Users/dell/images/api_image_male1.jpg")
    width, height = img_male_left.size
    x=width 
    y=height
    left = width/5
    top = height/16
    right =74* width/100
    bottom =3*height/3
    cropped_image = img_male_left.crop((left, top, right, bottom))

    cropped_image.show()
    cropped_image.size
    
    
    #for female
    img_female_right =Image.open("C:/Users/dell/images/api_image_female1.jpg")
    width, height = img_female_right.size
    left = width/4
    top = height/12
    right = 2 * width/4
    bottom =3*height/3
    cropped_image_fe = img_female_right.crop((left, top, right, bottom))

    cropped_image_fe.show()
    cropped_image_fe.size
    
    
    #resizing the male cropped image
    cropped_image=cropped_image.resize((75,574))
    cropped_image.show()
    
    #resizing the female cropped image
    cropped_image_fe=cropped_image_fe.resize((75,574))
    cropped_image_fe.show()
    
    #craeting the white box for the images
    bi = Image.new('RGBA',(150,1148),'white')
    bi.show()
    
    bi.paste(cropped_image_fe,(0,0,75,574))#female
    bi.show()
    
    
    bi.paste(cropped_image,(0,0,75,574))
    bi.show()
    
    
    #Combining both the images
    bi.paste(cropped_image_fe,(75,0,150,574))
    bi.show()
    
    
    return "task completed!!!!!!!!!!!!!!"


if __name__ == '__main__':
    app.run(debug=True)