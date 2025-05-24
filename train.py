from ultralytics import YOLO

def train(yaml_path):
    model = YOLO("yolo11n.pt")

    model.train(data = yaml_path,
                epochs = 50,
                batch = 4,
                patience = 10,
                lr0 = 1e-3,
                cos_lr = True,
                imgsz = 1280,
                resume = False,
                save = True)

if __name__ == "__main__":
    train("./datasets/potato/data.yaml")