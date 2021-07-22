from fake_web_events import Simulation
import json

simulation = Simulation(user_pool_size=100, sessions_per_day=100000)
events = simulation.run(duration_seconds=60)

for event in events:
    print(json.load(event))
    break