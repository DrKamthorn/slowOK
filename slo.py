import streamlit as st
from pydub import AudioSegment
import tempfile

# Function to slow down the tempo of an audio file
def slow_down_tempo(audio_file, speed_factor):
    audio = AudioSegment.from_file(audio_file)

    # Calculate the number of times each chunk should be repeated
    repeat_factor = int(1 / speed_factor)

    # Split the audio into chunks and repeat each chunk
    slowed_audio = audio
    for _ in range(repeat_factor - 1):
        slowed_audio += audio

    return slowed_audio

# Main app
def main():
    st.title("ปรับเสียงให้ช้าลงโดยเลือกสเกลให้ต่ำกว่า 1")
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
    speed_factor = st.slider("Speed Factor", 0.1, 2.0, 1.0, 0.1)

    if audio_file is not None:
        audio = AudioSegment.from_file(audio_file)
        st.audio(audio_file, format='audio/wav')

        if st.button("Slow Down Tempo"):
            slowed_audio = slow_down_tempo(audio_file, speed_factor)
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_filename = tmp_file.name
                slowed_audio.export(tmp_filename, format='wav')
            st.audio(tmp_filename, format='audio/wav', start_time=0)

# Run the app
if __name__ == "__main__":
    main()

