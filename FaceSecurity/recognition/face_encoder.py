import cv2
import face_recognition


class FaceEncoder:

    def encode(self, frame, face_location):
        """
        Convert a detected face into a face encoding.

        face_location format:
        (top, right, bottom, left)
        """

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        encodings = face_recognition.face_encodings(
            rgb_frame,
            known_face_locations=[face_location]
        )

        if not encodings:
            return None

        return encodings[0]