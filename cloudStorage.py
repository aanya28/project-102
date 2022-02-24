import dropbox
import cv2
import time
import random

startTime = time.time()

def takeSnapshot():
    number = random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)

    result = True

    while(result):
        #read the frames while camera is on
        ret,frame = videoCaptureObject.read()

        # saving the image
        #cv2.imwrite(filename,image)
        img_name= "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        result=False
    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.BClkXCdC6K5H_9-jv-jOzk8PzLLrkNqJuaGQV8ei2_2-0gyoH7C0mrBfqfeVCYitDekLp2sffkxIOPhhHzXT9iTVgjT6YBYQb19LpHCGY94KiDXYZ3phprMLpnTzlgnyrV3pVDfxWlat"
    file =img_name
    file_from = file
    file_to="/image_folder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
            name= takeSnapshot()
            upload_file(name)

main()

        