# Steady Study + ML

Frontend: `index.html` (GitHub Pages compatible).
Backend: Flask API for storing session summaries and generating personalised suggestions.
ML: scikit-learn RandomForestClassifier in `ml/train.py`.

## Local run

```bash
pip install -r requirements.txt
python backend/app.py
```

The API runs on `http://localhost:5000`.

## Train

```bash
python ml/train.py
```

The starter CSV contains demonstration rows only. Replace them with real session data before treating the model as personalised.

## Important architecture note

GitHub Pages cannot execute Flask/scikit-learn. Host the frontend on GitHub Pages and the Python API on a Python-capable host, then set the API URL in the frontend.
