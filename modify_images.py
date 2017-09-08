#coding:utf-8
import dicom
import os

if __name__ == '__main__':
    images_path = r'F:\images\4'  
    images = 0
    num = 1300000
    checkNo = 2017082403001
    for root, dirs, files in os.walk(images_path):
        images_cnt = 0
        filedirs = "./images/tt/"+str(checkNo)
            #print(filedirs)
        os.mkdir(filedirs)
        i =0
        for filename in files:
            #filedir = os.path.join(root,)
            #print(filedir)
            

            if filename.endswith('.dcm') and i <10:
                filepath = os.path.join(root, filename)
                ds = dicom.read_file(filepath)
                ds.PatientName = "patient"+str(num)+"_"+str(checkNo)
                ds.StudyInstanceUID ="1.2.3.100651."+str(checkNo)
                ds.PatientID = "p"+str(checkNo)
                ds.StudyID = str(checkNo)
                ds.SeriesInstanceUID = "0124"+str(checkNo)
                ds.save_as("{}/{}.dcm".format(filedirs,"patient"+str(num)+"_"+str(checkNo)))
                images_cnt += 1
                num += 1
            i +=1
        checkNo += 1

        images = images_cnt + images
        print(os.path.join(root,),"图像数量：{}".format(images_cnt))
    #     with open("count.txt","a") as f :
    #         f.write(os.path.join(root,)+"图像数量："+str(images_cnt)+"\n" )
    # with open("count.txt","a") as f :
    #     f.write("图像总数量："+str(images)+"\n" )
    print("图像总数量为：{}".format(images))