import cv2
import numpy as np
from keras import models

model = models.load_model("dat.h5")

canvas = np.ones((600, 600), dtype="uint8") * 255
canvas[100:500, 100:500] = 0

start_point = None
end_point   = None
is_drawing  = False

def draw_line(img, start_at, end_at):
  cv2.line(img, start_at, end_at, 255, 15)
  
def on_mouse_events(event, x, y, flags, params):
  global start_point
  global end_point
  global canvas
  global is_drawing
  if event == cv2.EVENT_LBUTTONDOWN:
    if is_drawing:
      start_point = (x, y)
  elif event == cv2.EVENT_MOUSEMOVE:
    if is_drawing:
      end_point = (x, y)
      draw_line(canvas, start_point, end_point)
      start_point = end_point
  elif event == cv2.EVENT_LBUTTONUP:
    is_drawing = False
    
cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", on_mouse_events)

while True:
  cv2.imshow("Canvas", canvas)
  key = cv2.waitKey(1) & 0xFF
  if key == ord("q"):
    break
  elif key == ord("s"):
    is_drawing = True
  elif key == ord("c"):
    canvas[100:500, 100:500] = 0
  elif key == ord("p"):
    image = canvas[100:500, 100:500]
    image = cv2.resize(image, (28, 28), interpolation=cv2.INTER_CUBIC)
    image = image.reshape(1, 28, 28, 1)
    result = model.predict(image)
    print("Prediction:", np.argmax(result))
    
cv2.destroyAllWindows()