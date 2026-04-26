# Fourier Audio Analyzer

This project demonstrates Fourier Transform on real audio signals.

## Features
- Upload audio file (.mp3/.wav)
- View time-domain signal
- View frequency spectrum using FFT
- Remove selected frequency components
- Reconstruct signal using inverse FFT
- Compare original and modified audio

## Concepts Used
- Fourier Series
- Fourier Transform
- Discrete Fourier Transform (DFT)
- Fast Fourier Transform (FFT)

## How to Run
pip install numpy matplotlib librosa soundfile streamlit  
streamlit run app.py

## Output
- Time domain waveform
- Frequency spectrum
- Modified audio after filtering
- Reconstruction error

## Conclusion
This project shows how audio signals can be decomposed into frequencies and reconstructed using Fourier Transform.
