import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

num_sessions = 100
station_ids = [f'STN{str(i).zfill(3)}' for i in range(1, 11)]

data = {
    'station_id': [random.choice(station_ids) for _ in range(num_sessions)],
    'start_time': [datetime.now() - timedelta(hours=random.randint(0, 240)) for _ in range(num_sessions)],
    'energy_kwh': [round(random.uniform(5.0, 50.0), 2) for _ in range(num_sessions)],
}

df = pd.DataFrame(data)
df = df.sort_values('start_time')
df.to_csv('data/ev_charging_sessions.csv', index=False)

print(f"✔ Created {len(df)} sample sessions")
print("✔ Saved to data/ev_charging_sessions.csv")
