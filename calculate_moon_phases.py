import ephem
from datetime import datetime, timedelta
import json

def get_moon_phases(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    current_date = start_date

    phases = ["New Moon", "First Quarter", "Full Moon", "Last Quarter"]
    phase_data = []

    while current_date <= end_date:
        moon_phase = ephem.Moon(current_date).phase
        if 0 <= moon_phase < 7.4:
            phase = phases[0]  # New Moon
        elif 7.4 <= moon_phase < 14.8:
            phase = phases[1]  # First Quarter
        elif 14.8 <= moon_phase < 22.1:
            phase = phases[2]  # Full Moon
        else:
            phase = phases[3]  # Last Quarter

        phase_data.append({"date": current_date.strftime("%Y-%m-%d"), "phase": phase})
        current_date += timedelta(days=1)

    return phase_data

# Генерируем данные для 2025 года
moon_phases = get_moon_phases(2025)

# Сохраняем данные в JSON-файл в папке web-app
with open('web-app/moon_phases.json', 'w') as f:
    json.dump(moon_phases, f, indent=4)

print("Файл moon_phases.json успешно создан!")
