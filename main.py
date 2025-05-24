import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("./potato_counting/potatoes_input_vid.mp4")  # path to video file
assert cap.isOpened(), "Error reading video file"

region_points = [[1603, 1012], [474, 1012], [0, 265], [6, 8], [465, 0]]
# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize object counter object
counter = solutions.ObjectCounter(
    show=True,
    region=region_points,
    model="./runs/detect/train6/weights/best.pt",
    tracker="botsort.yaml",  # or "bytetrack.yaml"
    tracker_conf=0.3,        # Increase to filter weak tracks
    tracker_iou=0.2,         
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = counter(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows