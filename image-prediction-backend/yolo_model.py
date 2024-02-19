#yolov8 model for detecting object

from ultralytics import YOLO

model = YOLO("yolov8m.pt")

objects_detected =[]

def yolo_predict(image):
    print("Mothod Called")
    results = model.predict(image)
    result = results[0]

    #box = result.boxes[0]

    '''cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    class_id = result.names[box.cls[0].item()]
    conf = round(box.conf[0].item(), 2)
    print("Object type:", class_id)   #prints the class of object'''


    for box in result.boxes:
        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
        print("Object type:", class_id)
        print("---")
        objects_detected.append(class_id) #array containing all the objects it detected

    return objects_detected
