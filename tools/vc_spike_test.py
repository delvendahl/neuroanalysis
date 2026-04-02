import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from neuroanalysis.spike_detection import detect_vc_evoked_spikes
from neuroanalysis.data import TSeries


# Load test data
data = np.load('test_data/evoked_spikes/vc_evoked_spikes.npz')['arr_0']
dt = 20e-6

# gaussian filtering constant
sigma = 20e-6 / dt

# Create a window with a grid of plots (N rows, 1 column)
fig, axes = plt.subplots(data.shape[0], 1, sharex=True, figsize=(10, 2 * data.shape[0]))

# Loop over all 10 channels
for i in range(data.shape[0]):
    # select the data for this channel
    trace = data[i, :, 0]
    stim = data[i, :, 1]

    # select the plot we will use for this trace
    ax = axes[i]

    # use stimulus to find pulse edges
    diff = np.diff(stim)   # np.diff() gives first derivative
    on_times = np.argwhere(diff > 0)[:,0]
    off_times = np.argwhere(diff < 0)[:,0]

    # decide on the region of the trace to focus on
    start = on_times[1] - 1000
    stop = off_times[8] + 1000
    chunk = trace[start:stop]

    # plot the selected chunk
    t = np.arange(chunk.shape[0]) * dt
    ax.plot(t[:-1], np.diff(ndi.gaussian_filter(chunk, sigma)), color='0.5', alpha=0.5)
    ax.plot(t, chunk)

    # detect spike times
    peak_inds = []
    rise_inds = []
    for j in range(8):  # loop over pulses
        pstart = on_times[j+1] - start
        pstop = off_times[j+1] - start
        spike_info = detect_vc_evoked_spikes(TSeries(chunk, dt=dt), pulse_edges=(pstart, pstop))
        if spike_info is not None:
            peak_inds.append(spike_info['peak_index'])
            rise_inds.append(spike_info['rise_index'])

    # display spike rise and peak times as ticks
    for p_ind in peak_inds:
        ax.axvline(p_ind * dt, color='r', alpha=0.5)
    for r_ind in rise_inds:
        ax.axvline(r_ind * dt, color='y', alpha=0.5)

axes[-1].set_xlabel('Time (s)')
plt.tight_layout()
plt.show()
    
    
    
