import fileinput
import shutil

Usr=input("Please enter user name: ")
cName=input("Please enter crop name: ")
cLink=input("Please paste the link for the image of the crop here: ")
cBuyLink=input("Please paste the link for buying the crop here: ")

rplLink='<img alt="crop" class="big" src="'+cLink+'" style="display: block; height: auto; border: 0; width: 393px; max-width: 100%;" title="crop" width="393"/>'

buyNowLink='<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="'+cBuyLink+'" style="height:38px;width:93px;v-text-anchor:middle;" arcsize="11%" stroke="false" fillcolor="#2bd95e"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Tahoma, sans-serif; font-size:14px"><![endif]--><a href="'+cBuyLink+'" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#2bd95e;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 28px;">Buy Now</span></span></a>'
filename=cName+'.html'
shutil.copy('mail.html', filename)
print(filename)

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace("<!--UserName-->", Usr), end='')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace("<!--CropName-->", cName), end='')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('<img alt="crop" class="big" src="https://lh3.googleusercontent.com/ot5wOM6j47MsALSkfsLZ9YfzYs9tDI8k-kq3WP2dSvRUaeaRZuMOICz4jJcRYLcjOtleS1GCD31-F4wCRjYYVpvVCYm1XGm6ONyx6zPv6Lsac6wEJDVeDpfWstxscXeXK6AR8_bZHA=w2400" style="display: block; height: auto; border: 0; width: 393px; max-width: 100%;" title="crop" width="393"/>', rplLink), end='')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://ip-exhibit-crop-management.herokuapp.com/shop" style="height:38px;width:93px;v-text-anchor:middle;" arcsize="11%" stroke="false" fillcolor="#2bd95e"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Tahoma, sans-serif; font-size:14px"><![endif]--><a href="https://ip-exhibit-crop-management.herokuapp.com/shop" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#2bd95e;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 28px;">Buy Now</span></span></a>', buyNowLink), end='')


# https://drive.google.com/uc?export=view&id=FILE-ID-GOES-HERE
# 1FpZqYmi0FNXU4vMqkFiwmFG_KNFB_z4q
# https://drive.google.com/uc?export=view&id=1FpZqYmi0FNXU4vMqkFiwmFG_KNFB_z4q
