from flask import Flask, request, jsonify
from flask_cors import CORS
import os, pandas as pd
from ml.recommender import suggestions

app=Flask(__name__); CORS(app)
DATA='data/sessions.csv'
COLS=['session_minutes','eye_level_events','eyes_closed_events','face_missing_events','focus_rate','study_mode','focus_state']

@app.get('/health')
def health(): return jsonify({'ok':True})

@app.post('/session')
def session():
    payload=request.get_json(force=True)
    row={c:payload.get(c,0) for c in COLS}
    os.makedirs('data',exist_ok=True)
    df=pd.DataFrame([row])
    if os.path.exists(DATA): df.to_csv(DATA,mode='a',header=False,index=False)
    else: df.to_csv(DATA,index=False)
    all_df=pd.read_csv(DATA)
    return jsonify({'saved':True,'session_count':len(all_df),'suggestions':suggestions(all_df)})

@app.get('/suggestions')
def get_suggestions():
    if not os.path.exists(DATA): return jsonify({'session_count':0,'suggestions':suggestions(pd.DataFrame())})
    df=pd.read_csv(DATA)
    return jsonify({'session_count':len(df),'suggestions':suggestions(df)})

if __name__=='__main__': app.run(host='0.0.0.0',port=5000,debug=True)
