"""Combine all the datasets into one dataset. Fixing the labels and images"""
import os
import shutil
import glob
import yaml
import cv2

class PotatoDataset():
    def __init__(self, root_paths, output_path):
        self.root_paths = root_paths
        self.output_path = output_path
    
        #Build the output folder
        if os.path.isdir(self.output_path):
            shutil.rmtree(self.output_path)
        os.mkdir(self.output_path)
    
    def build_dataset(self):
        cnt = 0
        #traverse through the root paths
        for root_path in self.root_paths:
            #read the yaml file
            yaml_path = glob.glob(f"{root_path}/*.yaml")[0]
            with open(yaml_path, "r") as f:
                yaml_data = yaml.safe_load(f)
                classes = yaml_data["names"]

            #get the class_id of potato in the dataset
            potato_id = [classes.index(class_name) for class_name in classes if "potato" in class_name.lower()]
            
            #read the images and modify the label files
            for label_path in glob.glob(f"{root_path}/*/*/*.txt"):
                #get the mode (train/valid/test)
                mode = label_path.split("/")[-3]

                #read the label file
                with open(label_path, "r") as f:
                    lines = f.readlines()

                #modify the label file
                new_lines = []
                for line in lines:
                    parts = line.strip().split(" ")
                    if int(parts[0]) in potato_id:
                        parts[0] = "0"
                        new_lines.append(" ".join(parts))
                
                #if the image has no potato
                if len(new_lines) == 0:
                    continue

                #save the new label file
                save_label_path = os.path.join(self.output_path, mode, "labels", f"{cnt}.txt")
                if not os.path.isdir(os.path.dirname(save_label_path)):
                    os.makedirs(os.path.dirname(save_label_path))
                with open(save_label_path, "w") as f:
                    f.writelines([line + "\n" for line in new_lines])
                
                #get the image path
                image_path = label_path.replace(".txt", ".jpg").replace("/labels/", "/images/")
                
                #save the image
                save_image_path =os.path.join(self.output_path, mode, "images", f"{cnt}.jpg")
                if not os.path.isdir(os.path.dirname(save_image_path)):
                    os.makedirs(os.path.dirname(save_image_path))
                image = cv2.imread(image_path)
                cv2.imwrite(save_image_path, image)

                #increment the counter
                cnt += 1

    def create_yaml(self, train_path, valid_path, test_path):
        yaml_path = os.path.join(self.output_path, "data.yaml")
        if os.path.isfile(yaml_path):
            os.remove(yaml_path)
        
        with open(yaml_path, "w") as f:
            yaml_data = {
                "train": train_path,
                "val": valid_path,
                "test": test_path,
                "nc": 1,
                "names": ["potato"]
            }
            yaml.dump(yaml_data, f)


if __name__ == "__main__":
    root_paths = glob.glob("./datasets/potato_downloads/*")
    output_path = "./datasets/potato"
    dataset = PotatoDataset(root_paths, output_path)
    dataset.build_dataset()
    dataset.create_yaml(
        train_path = "/home/minh/Documents/DL for CV/Exercises/datasets/potato/train/images",
        valid_path = "/home/minh/Documents/DL for CV/Exercises/datasets/potato/valid/images",
        test_path = "/home/minh/Documents/DL for CV/Exercises/datasets/potato/test/images"
    )