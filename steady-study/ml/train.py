import os, joblib, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

DATA='data/sessions.csv'; MODEL='ml/focus_model.pkl'; LABELS='ml/labels.pkl'
FEATURES=['session_minutes','eye_level_events','eyes_closed_events','face_missing_events','focus_rate','study_mode']

if not os.path.exists(DATA):
    raise SystemExit('No data/sessions.csv yet. Run sessions first, then export/collect data.')

df=pd.read_csv(DATA)
if len(df)<8 or 'focus_state' not in df.columns:
    raise SystemExit('Need at least 8 labeled rows with focus_state before training.')
for c in FEATURES:
    if c not in df.columns: raise SystemExit(f'Missing column: {c}')
X=df[FEATURES].copy(); X['study_mode']=X['study_mode'].astype(str)
X=pd.get_dummies(X,columns=['study_mode'])
y=df['focus_state'].astype(str)
model=RandomForestClassifier(n_estimators=150,max_depth=8,random_state=42,class_weight='balanced')
model.fit(X,y)
os.makedirs('ml',exist_ok=True)
joblib.dump({'model':model,'columns':list(X.columns)},MODEL)
print(f'Trained on {len(df)} sessions. Saved {MODEL}')
