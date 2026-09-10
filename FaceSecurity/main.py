import cv2

from camera.camera_manager import CameraManager
from detection.face_detector import FaceDetector
from recognition.face_encoder import FaceEncoder
from recognition.face_matcher import FaceMatcher
from database.face_database import FaceDatabase
from config.settings import FACE_MATCH_THRESHOLD


def main():

    camera = CameraManager()
    detector = FaceDetector()
    encoder = FaceEncoder()
    matcher = FaceMatcher()
    database = FaceDatabase()

    known_encodings = database.get_encodings()

    print("Face Recognition V1 started.")
    print("Press Q to exit.")

    while True:

        frame = camera.read()

        if frame is None:
            print("Could not access the camera.")
            break

        faces = detector.detect(frame)

        for x, y, w, h in faces:

            # Convert Haar Cascade coordinates
            # to face_recognition format:
            # (top, right, bottom, left)

            face_location = (
                y,
                x + w,
                y + h,
                x
            )

            # Generate face encoding
            face_encoding = encoder.encode(
                frame,
                face_location
            )

            # Find best matching person
            name, distance = matcher.find_best_match(
                known_encodings,
                face_encoding
            )

            # Decide whether the face is recognized
            if matcher.is_match(
                distance,
                FACE_MATCH_THRESHOLD
            ):
                label = name
            else:
                label = "Unknown"

            # Draw face box
            detector.draw_face(
                frame,
                x,
                y,
                w,
                h
            )

            # Draw name
            detector.draw_label(
                frame,
                label,
                x,
                y
            )

        camera.show(frame)

        if camera.should_exit():
            break

    camera.release()


if __name__ == "__main__":
    main()