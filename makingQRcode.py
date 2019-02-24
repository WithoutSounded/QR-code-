import qrcode

studentID = ['410521231\n張維凱\n資工三','410521232\n張凱\n資工三','410521233\n張維\n資工三',\
             '410521234\n維凱\n資工三','410521235\n張\n資工三','410521236\n維\n資工三',\
             '410521237\n凱\n資工三','410521238\nJustin Chang\n資工三','410521239\nJustin\n資工三',\
             '410521230\nChang\n資工三']
             
for ID in studentID:
    img = qrcode.make(ID)
    img.save("D:\\Software\\APP\\QR code sign in\\"+ID[:9]+".png")
    
# ID:410521231\nName:張維  \nSubject:資工三  以上為QR Code 的儲存格式 ID為9 Name為4 Subject為3 的長度(app inventor2 不論實際儲存大小)
    
