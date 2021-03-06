#coding:utf-8
#######################
#
#
#
#单个图像修改
#一个病人一幅图像
#
#
#
#
######################




import dicom
import os

if __name__ == '__main__':
    images_path = r'F:\python\统计图像\client\1222333333333333332017082403002'  
    images = 0
    num = 2017072700001
    checkNo = 1709080003
    for root, dirs, files in os.walk(images_path):
        images_cnt = 0
        for filename in files:

            if filename.endswith('.dcm'):
                filepath = os.path.join(root, filename)
                ds = dicom.read_file(filepath)
                ds.PatientName = "patient_"+str(checkNo)
                ds.StudyInstanceUID ="100651."+str(checkNo)
                ds.PatientID = "p"+str(checkNo)
                ds.SeriesInstanceUID = "0124"+str(checkNo)
                ds.save_as("./{}.dcm".format("patient"+str(num)+"_"+str(checkNo)))
                images_cnt += 1
                num += 1
                checkNo += 1

        images = images_cnt + images
        print(os.path.join(root,),"图像数量：{}".format(images_cnt))
        with open("count.txt","a") as f :
            f.write(os.path.join(root,)+"图像数量："+str(images_cnt)+"\n" )
    with open("count.txt","a") as f :
        f.write("图像总数量："+str(images)+"\n" )
    print("图像总数量为：{}".format(images))