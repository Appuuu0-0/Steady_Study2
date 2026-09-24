import pandas as pd

def suggestions(df):
    if df.empty: return ['Complete a few study sessions so the app can learn your patterns.']
    out=[]
    recent=df.tail(10)
    avg_len=recent.session_minutes.mean()
    avg_focus=recent.focus_rate.mean()
    avg_drop=recent.eye_level_events.mean()
    avg_closed=recent.eyes_closed_events.mean()
    avg_missing=recent.face_missing_events.mean()
    if avg_len >= 45 and avg_focus < 0.70: out.append('Your recent longer sessions have had more interruptions. Try a shorter study block with a planned break.')
    elif avg_focus >= 0.80: out.append('Your recent sessions have had a high share of signals in range. You can keep a similar session length and routine.')
    if avg_drop >= 5: out.append('Eye-level changes have been frequent recently. Recheck your camera position and consider recalibrating before the next session.')
    if avg_closed >= 3: out.append('There have been several extended eye-closure events. Consider a short break if you feel tired.')
    if avg_missing >= 3: out.append('Your face has often left the camera view. A clearer camera position may reduce tracking interruptions.')
    if not out: out.append('Your recent sessions do not show a strong pattern yet. Keep collecting sessions and the suggestions will become more personalised.')
    return out[:3]
