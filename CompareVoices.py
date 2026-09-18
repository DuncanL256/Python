import numpy as np 
import librosa 
import sounddevice as sd
import soundfile as sf

def extract_features(file_path): 
    """Extract MFCC features from the audio file."""
    y, sr = librosa.load(file_path, sr=None)  # Load the audio file
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)  # Extract MFCCs
    mfccs_mean = np.mean(mfccs.T, axis=0)  # Take the mean of the MFCCs across time
    return mfccs_mean 

def compare_audio(file1, file2, threshold=35): 
    """Compare two audio files and return authentication status."""
    features1 = extract_features(file1)  
    features2 = extract_features(file2)  
    distance = np.linalg.norm(features1 - features2)  
    print(f"Distance: {distance}")  
    return distance < threshold  # Returns True if the distance is within the threshold

def record_voice(filename, duration=5, samplerate=22050):
    """Records audio and saves it to a file."""
    print("!!Speak clearly!!")
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()  
    sf.write(filename, audio, samplerate)  
    print(f"Recording saved as {filename}")
    return filename  

def authenticate_user():
    """Prompts for username, records voice, and checks authentication."""
    name = input("Enter your name: ").strip()  
    stored_voice_file = name + '.wav'  

    # Record a new voice sample for login
    login_voice_file = record_voice('login.wav')  

    # Compare stored vs new voice sample
    if compare_audio(stored_voice_file, login_voice_file):  
        print("Access Granted")
        return True  
    else:  
        print("Access Denied")
        return False  

# Exicutible code
record_voice()
extract_features()
compare_audio()
authenticate_user()