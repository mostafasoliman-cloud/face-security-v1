from camera.camera_manager import CameraManager
from detection.face_detector import FaceDetector
from recognition.face_encoder import FaceEncoder
from database.face_database import FaceDatabase


def enroll_user():

    name = input("Enter person's name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    camera = CameraManager()
    detector = FaceDetector()
    encoder = FaceEncoder()
    database = FaceDatabase()

    samples = 0
    required_samples = 20

    print()
    print(f"Starting enrollment for: {name}")
    print("Look at the camera and move your face slightly.")
    print("Press Q to cancel.")
    print()

    while samples < required_samples:

        frame = camera.read()

        if frame is None:
            print("Could not access the camera.")
            break

        faces = detector.detect(frame)

        if len(faces) == 1:

            x, y, w, h = faces[0]

            face_location = (
                y,
                x + w,
                y + h,
                x
            )

            encoding = encoder.encode(
                frame,
                face_location
            )

            if encoding is not None:

                database.add_face(
                    name,
                    encoding
                )

                samples += 1

                detector.draw_face(
                    frame,
                    x,
                    y,
                    w,
                    h
                )

                detector.draw_label(
                    frame,
                    f"Samples: {samples}/{required_samples}",
                    x,
                    y
                )

        camera.show(frame)

        if camera.should_exit():
            print("Enrollment cancelled.")
            break

    camera.release()

    if samples == required_samples:
        print()
        print(f"Enrollment completed successfully for {name}.")
    else:
        print()
        print(f"Enrollment stopped. Captured {samples}/{required_samples} samples.")


if __name__ == "__main__":
    enroll_user()