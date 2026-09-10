import cv2


class CameraManager:

    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)

    def read(self):
        ret, frame = self.camera.read()

        if not ret:
            return None

        return cv2.flip(frame, 1)

    def show(self, frame, window_name="Face Security"):
        cv2.imshow(window_name, frame)

    def should_exit(self):
        return cv2.waitKey(1) & 0xFF == ord("q")

    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()