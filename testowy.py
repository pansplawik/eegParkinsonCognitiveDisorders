# testy
import mne
import numpy as np
import matplotlib.pyplot as plt

raw = mne.io.read_raw_edf('PD129.edf', preload=True)

raw = raw.crop(tmax=120)

raw.filter(l_freq=1, h_freq=40)


sfreq = raw.info['sfreq']
duration = raw.times[-1]
n_samples = int(sfreq * duration)
n_samples_per_second = int(sfreq)
raw_resampled = raw.resample(sfreq=n_samples_per_second, n_samples=n_samples, npad="auto")

freqs = np.logspace(*np.log10([1, 40]), num=60)
tfr = mne.time_frequency.tfr_morlet(raw_resampled, freqs=freqs, n_cycles=freqs / 2,
                                    return_itc=False, average=False, picks=None)

tfr.plot(picks='eeg')
