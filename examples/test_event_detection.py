import matplotlib.pyplot as plt
import numpy as np
from neuroanalysis.data import TSeries
from neuroanalysis.event_detection import threshold_events


data = np.load("test_data/synaptic_events/events1.npz")
trace_names = sorted([x for x in data.keys() if x.startswith('trace')])
traces = {n:TSeries(data[n], dt=1.0/data['sample_rates'][i]) for i,n in enumerate(trace_names)}

threshold = 5e-10

fig, axes = plt.subplots(len(trace_names), 1, figsize=(10, 2 * len(trace_names)), sharex=True)

for i, name in enumerate(trace_names):
    trace = traces[name]
    events = threshold_events(trace, threshold)

    ax = axes[i]
    ax.plot(trace.time_values, trace.data)
    ax.set_title(name)

    for ev in events:
        ax.axvspan(ev['time'], ev['time'] + ev['duration'], color='r', alpha=0.3)

plt.tight_layout()
plt.show()
