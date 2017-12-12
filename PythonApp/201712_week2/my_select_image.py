import os
import os.path
import shutil

IMG_PATH = os.path.dirname(os.path.abspath(__file__))

def main():
    flowers = ["sakura", "sunflower", "rose"]
    for flower in flowers:
        src_path = os.path.join(IMG_PATH, flower)
        dst_path = os.path.join(IMG_PATH, flower + "-ok")

        file_names = os.listdir(src_path)
        counter = 0
        for file_name in file_names:
            src_file = os.path.join(src_path, file_name)
            dst_file = os.path.join(dst_path, file_name)
            shutil.move(src_file, dst_file)    
            counter = counter + 1
            if counter == 300:
                break
        
if __name__ == '__main__':
    main()
