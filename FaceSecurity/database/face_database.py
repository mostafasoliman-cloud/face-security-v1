import json
import os
import numpy as np


class FaceDatabase:

    def __init__(self, database_path="data/faces.json"):
        self.database_path = database_path
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.database_path):
            return {}

        with open(
            self.database_path,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    def save(self):
        directory = os.path.dirname(self.database_path)

        if directory:
            os.makedirs(
                directory,
                exist_ok=True
            )

        with open(
            self.database_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                self.data,
                file,
                indent=4
            )

    def add_face(self, name, encoding):

        if name not in self.data:
            self.data[name] = []

        self.data[name].append(
            encoding.tolist()
        )

        self.save()

    def get_encodings(self):

        return {
            name: [
                np.array(encoding)
                for encoding in encodings
            ]
            for name, encodings in self.data.items()
        }

    def get_names(self):
        return list(self.data.keys())