import openai
import streamlit as st
from pathlib import Path
from moviepy import VideoFileClip
from dotenv import load_dotenv

load_dotenv()

client = openai.Client(api_key=st.secrets["OPENAI_API_KEY"])

PASTA_TEMPORARIA = Path(__file__).parent / "temp"
PASTA_TEMPORARIA.mkdir(exist_ok=True)
ARQUIVO_AUDIO_TEMPORARIO = PASTA_TEMPORARIA / "audio_temp.mp3"
ARQUIVO_VIDEO_TEMPORARIO = PASTA_TEMPORARIA / "video_temp.mp4"
ARQUIVO_MIC_TEMPORARIO = PASTA_TEMPORARIA / "mic_temp.mp3"


def salva_audio_do_video(video_bytes):
    with st.spinner("Salvando áudio do vídeo..."):
        with open(ARQUIVO_VIDEO_TEMPORARIO, mode='wb') as video_f:
            video_f.write(video_bytes.read())
        moviepy_video = VideoFileClip(str(ARQUIVO_VIDEO_TEMPORARIO))
        moviepy_video.audio.write_audiofile(str(ARQUIVO_AUDIO_TEMPORARIO))


def transcreve_audio(caminho_audio, prompt, method_file=False):
    with st.spinner("Transcrevendo áudio..."):
        if method_file:
            with open(caminho_audio, 'rb') as arquivo_audio:
                transcricao = client.audio.transcriptions.create(
                    model='whisper-1',
                    language='pt',
                    response_format='text',
                    file=arquivo_audio,
                    prompt=prompt,
                )
                return transcricao
        else:
            transcricao = client.audio.transcriptions.create(
                    model='whisper-1',
                    language='pt',
                    response_format='text',
                    file=caminho_audio,
                    prompt=prompt,
                )
            return transcricao

