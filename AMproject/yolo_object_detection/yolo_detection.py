import cv2
import numpy as np
print(cv2.__version__)

def result_str(imagepath):

    # basic model
    # path_w = ".\yolo_object_detection\yolov3.weights"
    # path_cfg = ".\yolo_object_detection\yolov3.cfg"
    # path_name = ".\yolo_object_detection\coco.names"

    # mymodel
    path_w = ".\yolo_object_detection\yolov3real.weights"
    path_cfg = ".\yolo_object_detection\yolov3_testing.cfg"
    path_name = ".\yolo_object_detection\yolov3real.names"

    #yolo 로드
    net = cv2.dnn.readNet(path_w, path_cfg)
    classes = []
    with open(path_name, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # 이미지 가져오기
    img = cv2.imread(imagepath)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # 정보를 화면에 표시
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # 좌표
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    #노이즈 제거???
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    try:
        resultclass=classes[class_ids[0]]
    except:
        resultclass="찾을 수 없습니다."

    return resultclass
