import face_recognition


class FaceMatcher:

    def find_best_match(self, known_encodings, face_encoding):

        if not known_encodings or face_encoding is None:
            return None, None

        best_name = None
        best_distance = float("inf")

        for name, encodings in known_encodings.items():

            distances = face_recognition.face_distance(
                encodings,
                face_encoding
            )

            if len(distances) == 0:
                continue

            distance = min(distances)

            if distance < best_distance:
                best_distance = distance
                best_name = name

        return best_name, best_distance

    def is_match(self, distance, threshold=0.6):

        if distance is None:
            return False

        return distance <= threshold