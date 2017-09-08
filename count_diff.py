#coding:utf-8
import dicom
import os

if __name__ == '__main__':
    images_path = r'F:\python\统计图像\images\dd'  
    images = 0
    checkNo_count = set()
    StudyInstanceUID_count = set()



    for root, dirs, files in os.walk(images_path):
        images_cnt = 0

        for filename in files:


            if filename.endswith('.dcm'):
                filepath = os.path.join(root, filename)
                ds = dicom.read_file(filepath)
                checkNo_count.add(ds.StudyID)               
                StudyInstanceUID_count.add(ds.StudyInstanceUID)

                images_cnt += 1
            

        images = images_cnt + images
        print(os.path.join(root,),"图像数量：{}".format(images_cnt))
    #     with open("count.txt","a") as f :
    #         f.write(os.path.join(root,)+"图像数量："+str(images_cnt)+"\n" )
    # with open("count.txt","a") as f :
    #     f.write("图像总数量："+str(images)+"\n" )
    print("图像总数量为：{}".format(images))
    print(len(checkNo_count))
    print(len(StudyInstanceUID_count))
