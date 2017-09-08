import os

if __name__ == '__main__':
    images_path = r'F:\images\4'  
    images = 0
    for root, dirs, files in os.walk(images_path):
        images_cnt = 0
        for filename in files:
            if filename.endswith('.dcm'):
                #filepath = os.path.join(root, filename)
                images_cnt += 1
        images = images_cnt + images

        print(os.path.join(root,),"图像数量：{}".format(images_cnt))
        with open("count.txt","a") as f :
            f.write(os.path.join(root,)+"图像数量："+str(images_cnt)+"\n" )
    with open("count.txt","a") as f :
        f.write("图像总数量："+str(images)+"\n" )
    print("图像总数量为：{}".format(images))






               
         
            