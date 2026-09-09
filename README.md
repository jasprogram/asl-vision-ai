# ASL Vision AI

A learning and research project exploring visual recognition of American Sign Language (ASL).

## Goal

Build an application that can observe an ASL sign, identify the sign, and return a useful visual or textual result.

## Current version

Version 0.1 establishes the basic application pipeline:

1. User uploads an image.
2. Python receives the image.
3. The application displays the image.
4. A placeholder prediction is returned.

A trained computer-vision model will replace the placeholder in later versions.

## Planned architecture

Camera / Image
    ↓
Python application
    ↓
Image preprocessing
    ↓
AI model
    ↓
Prediction
    ↓
Word / picture / interface output

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run src/app.py
```

## Learning objectives

This repository is being developed alongside a structured AI and computer-science learning program. Topics will include Python, Git, APIs, computer vision, datasets, machine learning, neural networks, model training, inference, evaluation, deployment, and research methodology.

## Status

Early prototype / educational research project.

## Copyright

Copyright © 2026. All rights reserved.

This repository may be made publicly viewable for educational, research, and portfolio-review purposes. No permission is granted to copy, redistribute, modify, commercialize, or incorporate the work into another project unless separately authorized by the author.
