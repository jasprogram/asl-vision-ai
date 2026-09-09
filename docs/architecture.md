# Architecture

## Version 0.1

The first version intentionally separates the user interface from the future AI model.

```text
User
  |
  v
Image upload
  |
  v
Streamlit application
  |
  v
Pillow image object
  |
  v
Future preprocessing
  |
  v
Future ASL recognition model
  |
  v
Prediction
```

## Why build this first?

A machine-learning model is only one component of an AI system. A useful product also needs input handling, software logic, an interface, testing, and deployment.

Future versions will add:

- image preprocessing
- hand detection
- sign classification
- confidence scores
- evaluation metrics
- support for live video
- larger ASL vocabulary
