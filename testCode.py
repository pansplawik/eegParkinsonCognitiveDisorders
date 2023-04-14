import mne
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
# wczytaj dane
raw = mne.io.read_raw_edf('PD129.edf',preload=True)
events = mne.make_fixed_length_events(raw, duration=1.0)

# przetwórz dane
raw.filter(1, 40, fir_design='firwin')
epochs = mne.Epochs(raw, events, tmin=0, tmax=2, baseline=None)
epo_spectrum = epochs.compute_psd(method='multitaper', fmin=5, fmax=30,
                picks='eeg')
psds, freqs = epo_spectrum.get_data(return_freqs=True)