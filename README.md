# Face Security V1

> A modular real-time face recognition system built with Python, OpenCV, and face-recognition.

<p align="center">
  <strong>Face Detection · Face Encoding · Identity Matching · Secure Local Storage</strong>
</p>

## Overview

**Face Security V1** is a modular computer-vision project for real-time face detection and recognition through a webcam.

The system separates camera handling, face detection, face encoding, identity matching, database management, and configuration into independent modules. This makes the project easier to understand, test, extend, and maintain.

The project is intentionally designed as a **V1 foundation** rather than a production access-control system. Biometric data is kept local and excluded from version control.

## Features

- Real-time webcam face detection
- Face encoding using `face-recognition`
- Local identity matching using face embeddings
- Support for multiple enrolled identities
- Enrollment workflow with multiple face samples
- Configurable face-match threshold
- Modular project architecture
- Local JSON-based face database
- Privacy-focused `.gitignore` rules for biometric data
- Lightweight Windows-friendly Python setup

## Architecture

```text
Webcam
  │
  ▼
Camera Manager
  │
  ▼
Face Detector ────────────────┐
  │                           │
  ▼                           │
Face Encoder                  │
  │                           │
  ▼                           │
Face Matcher ◄── Face Database
  │
  ▼
Identity / Unknown
```

### Core pipeline

1. Capture a frame from the webcam.
2. Detect faces with OpenCV Haar Cascade.
3. Convert each detected face into a 128-dimensional face encoding.
4. Compare the encoding with locally stored identities.
5. Calculate the closest face distance.
6. Apply the configured matching threshold.
7. Display the detected identity or `Unknown`.

## Project Structure

```text
Face Recognition V1/
│
├── FaceSecurity/
│   ├── main.py                    # Real-time recognition entry point
│   ├── enroll.py                  # User enrollment workflow
│   │
│   ├── camera/
│   │   └── camera_manager.py      # Webcam lifecycle and frame handling
│   │
│   ├── detection/
│   │   └── face_detector.py       # Face detection and drawing utilities
│   │
│   ├── recognition/
│   │   ├── face_encoder.py        # Face → embedding conversion
│   │   └── face_matcher.py        # Identity matching and threshold logic
│   │
│   ├── database/
│   │   └── face_database.py       # Local embedding storage
│   │
│   ├── config/
│   │   └── settings.py            # Runtime configuration
│   │
│   └── data/
│       └── faces.json             # Local biometric database (ignored)
│
├── requirements.txt
├── pre_github_check.py
├── .gitignore
└── README.md
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Application runtime |
| OpenCV | Camera access and face detection |
| face-recognition | Face encoding and comparison |
| dlib | Face-recognition backend |
| NumPy | Numerical operations |
| JSON | Local biometric-data storage |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mostafasoliman-cloud/face-security-v1.git
cd face-security-v1
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

> The pinned dependencies are selected for the tested Windows/Python 3.11 environment.

## Usage

### Enroll a face

Run the enrollment module from inside `FaceSecurity`:

```powershell
cd FaceSecurity
python enroll.py
```

Enter the person's name and look at the camera. The system captures multiple samples and stores the resulting face embeddings locally.

### Start recognition

```powershell
python main.py
```

Press **Q** to exit the recognition window.

## Configuration

Runtime settings are located in:

```text
FaceSecurity/config/settings.py
```

Example:

```python
CAMERA_INDEX = 0
WINDOW_NAME = "Face Security"
FACE_DATABASE_PATH = "data/faces.json"
FACE_MATCH_THRESHOLD = 0.6
EXIT_KEY = "q"
```

### Match threshold

`FACE_MATCH_THRESHOLD` controls how close an unknown face must be to a stored encoding to be considered a match.

- Lower values → stricter matching
- Higher values → more permissive matching

The default value is `0.6` and should be treated as a starting point, not a security guarantee.

## Privacy & Security

This project processes biometric face representations, so privacy is a core design consideration.

- Face images are not intended to be committed to Git.
- `faces.json` is excluded from version control.
- Local face samples are excluded by `.gitignore`.
- The repository contains source code and configuration, not personal biometric profiles.
- Do not use real biometric data in a public repository.
- For real deployments, implement encryption, access control, retention policies, consent, audit logging, and secure storage.

## Current Limitations

This is a V1 computer-vision project and should **not** be treated as a complete security product.

- No liveness / anti-spoofing detection
- Haar Cascade detection can be affected by lighting, pose, and image quality
- Face matching is threshold-based
- Local JSON storage is not suitable for high-security production systems
- No encrypted biometric database
- No centralized authentication or authorization layer
- No production-grade audit system

## Roadmap

### V1 — Foundation

- [x] Real-time face detection
- [x] Face encoding
- [x] Identity matching
- [x] Multi-user enrollment
- [x] Configurable threshold
- [x] Modular architecture

### V1.x — Reliability

- [ ] Improved detection pipeline
- [ ] Better error handling
- [ ] Robust path management
- [ ] Recognition confidence/status UI
- [ ] Automated tests
- [ ] CI workflow

### V2 — Security Layer

- [ ] Liveness / anti-spoofing
- [ ] Encrypted biometric storage
- [ ] Secure authentication flow
- [ ] Event and access logging
- [ ] Better enrollment validation
- [ ] Production-ready configuration management

## Development Notes

The project intentionally keeps responsibilities separated:

- `camera/` handles the webcam.
- `detection/` handles locating faces.
- `recognition/` handles encoding and matching.
- `database/` handles local persistence.
- `config/` centralizes runtime settings.

This structure makes it possible to replace individual components without rewriting the whole application.

## Testing

A lightweight pre-GitHub validation script is included:

```powershell
python pre_github_check.py
```

It checks project structure, Python syntax, required files, dependency configuration, sensitive files, cache files, `.gitignore`, and duplicate source directories.

## Contributing

Contributions and improvements are welcome.

For substantial changes, open an issue first to discuss the proposed architecture or feature before submitting a pull request.

## License

This project is intended to be released under the **MIT License**. See `LICENSE` for the full license text.

## Author

**Mostafa Soliman**

AI / Computer Vision Engineering Project

GitHub: [@mostafasoliman-cloud](https://github.com/mostafasoliman-cloud)

---

<p align="center">
  Built as a foundation for practical AI and computer-vision engineering.
</p>
