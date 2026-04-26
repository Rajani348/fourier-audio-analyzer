import streamlit as st
import numpy as np
import librosa
import matplotlib.pyplot as plt
import soundfile as sf

st.title("Fourier Audio Analyzer")

uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file is not None:
    y, sr = librosa.load(uploaded_file)

    st.write("### Time Domain Signal")
    fig, ax = plt.subplots()
    ax.plot(y)
    st.pyplot(fig)

    # FFT
    Y = np.fft.fft(y)
    frequencies = np.fft.fftfreq(len(Y), 1/sr)

    st.write("### Frequency Spectrum")
    fig, ax = plt.subplots()
    ax.plot(frequencies, np.abs(Y))
    ax.set_xlim(0, 5000)
    st.pyplot(fig)

    # Slider
    cutoff = st.slider("Remove frequencies above (Hz)", 100, 5000, 1000)

    Y_filtered = Y.copy()
    Y_filtered[np.abs(frequencies) > cutoff] = 0

    # IFFT
    y_filtered = np.fft.ifft(Y_filtered).real

    st.write("### Reconstructed Signal")
    fig, ax = plt.subplots()
    ax.plot(y_filtered)
    st.pyplot(fig)

    # Save audio
    sf.write("output.wav", y_filtered, sr)

    st.audio("output.wav")

    # Error
    error = np.mean(np.abs(y - y_filtered))
    st.write(f"Reconstruction Error: {error}")