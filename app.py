
import queue
import time

import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer

import openai
import pydub
from dotenv import load_dotenv, find_dotenv
from utils import transcreve_audio, salva_audio_do_video, PASTA_TEMPORARIA, ARQUIVO_AUDIO_TEMPORARIO, ARQUIVO_VIDEO_TEMPORARIO, ARQUIVO_MIC_TEMPORARIO


st.set_page_config(
    page_title="Ferramenta de Transcrição de Áudio",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="auto"
)

load_dotenv()


if not 'transcricao_mic' in st.session_state:
    st.session_state['transcricao_mic'] = ''


@st.cache_data
def get_ice_servers():
    return [{'urls': ['stun:stun.l.google.com:19302']}]


def adiciona_chunck_de_audio(frames_de_audio, chunck_audio):
    for frame in frames_de_audio:
        sound = pydub.AudioSegment(
            data=frame.to_ndarray().tobytes(),
            sample_width=frame.format.bytes,
            frame_rate=frame.sample_rate,
            channels=len(frame.layout.channels)
        )
        chunck_audio += sound
    return chunck_audio


def transcrever_audio_mic():
    st.markdown("### Transcrição de Áudio via Microfone")
    prompt_mic = st.text_area(
        "Insira o texto de referência para a transcrição (opcional)",
        help="O nome da empresa é..., O assunto da conversa é...",
        placeholder="Digite o texto de referência",
        key="prompt_input_mic"
    )
    webrtx_ctx = webrtc_streamer(
        key='recebe_audio',
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=5000,
        media_stream_constraints={'video': False, 'audio': True}
    )

    if not webrtx_ctx.state.playing:
        st.write(st.session_state['transcricao_mic'])
        return

    container = st.empty()
    container.markdown('Comece a falar...')
    chunck_audio = pydub.AudioSegment.empty()
    tempo_ultima_transcricao = time.time()
    st.session_state['transcricao_mic'] = ''
    while True:
        if webrtx_ctx.audio_receiver:
            try:
                frames_de_audio = webrtx_ctx.audio_receiver.get_frames(
                    timeout=1)
            except queue.Empty:
                time.sleep(0.1)
                continue
            chunck_audio = adiciona_chunck_de_audio(
                frames_de_audio, chunck_audio)

            agora = time.time()
            if len(chunck_audio) > 0 and agora - tempo_ultima_transcricao > 10:
                tempo_ultima_transcricao = agora
                chunck_audio.export(ARQUIVO_MIC_TEMPORARIO)
                transcricao = transcreve_audio(
                    ARQUIVO_MIC_TEMPORARIO, prompt_mic)
                st.session_state['transcricao_mic'] += transcricao
                container.write(st.session_state['transcricao_mic'])
                chunck_audio = pydub.AudioSegment.empty()
        else:
            break

        


def transcrever_audio_video():
    st.markdown("### Transcrição de Áudio via Vídeo")
    prompt_input_video = st.text_area(
        "Insira o texto de referência para a transcrição (opcional)",
        help="O nome da empresa é..., O assunto da conversa é...",
        placeholder="Digite o texto de referência",
        key="prompt_input_video"
    )
    arquivo_video = st.file_uploader(
        "Faça o upload do arquivo de vídeo",
        type=["mp4"],
        help="""
        Formatos de vídeos suportados: .mp4 
        Coloque apenas um arquivo de vídeo por vez. E dos formatos suportados.
        """,
        key="arquivo_video"
    )

    st.divider()

    if st.button("Transcrever 📝", use_container_width=True, key="button_transcrever_video"):
        if not arquivo_video is None:
            salva_audio_do_video(arquivo_video)
            transcricao = transcreve_audio(
                ARQUIVO_AUDIO_TEMPORARIO, prompt_input_video, method_file=True)
            if transcricao:
                try:
                    st.text_area(
                        "Resultado Transcrição:", 
                        transcricao, height=300,
                        key="resultado_transcricao", 
                        help="Resultado da transcrição"
                        )
                    st.success(
                        "Transcrição realizada com sucesso!", icon="✔️")
                except Exception as error:
                    st.error(f"Erro na transcrição do áudio", icon="❌")
                    print(error)


def trascrever_audio_arquivo():
    st.markdown("### Transcrição de Áudio via Arquivo")
    prompt_input_audio = st.text_area(
        "Insira o texto de referência para a transcrição (opcional)",
        help="O nome da empresa é..., O assunto da conversa é...",
        placeholder="Digite o texto de referência",
        key="prompt_input_audio"
    )
    arquivo_audio = st.file_uploader(
        "Faça o upload do arquivo de áudio",
        type=["mp3"],
        help="""
        Formatos de áudio suportados: mp3 
        Coloque apenas um arquivo de áudio por vez. E dos formatos suportados.
        """,
        key="arquivo_audio"
    )

    st.divider()
    if st.button("Transcrever 📝", use_container_width=True, key="button_transcrever"):
        if arquivo_audio is not None:
            transcricao = transcreve_audio(
                arquivo_audio, prompt_input_audio)
            if transcricao:
                try:
                    st.text_area(
                        "Resultado Transcrição:", 
                        transcricao, 
                        height=300,
                        key="resultado_transcricao_audio", 
                        help="Resultado da transcrição"
                        )
                    st.success("Transcrição realizada com sucesso!", icon="✔️")
                except Exception as error:
                    st.error(f"Erro na transcrição do áudio", icon="❌")
                    print(error)


def render():
    st.header("Ferramenta de Transcrição de Áudio 🔈", divider=True)
    st.markdown(
        "#### Faça o upload de um arquivo de áudio e obtenha a transcrição do conteúdo.")
    tab_mic, tab_video, tab_audio = st.tabs(
        ["Microfone 🎤", "Vídeo 📽️", "Arquivo de Áudio 📁"])

    with tab_mic:
        transcrever_audio_mic()
    with tab_video:
        transcrever_audio_video()
    with tab_audio:
        trascrever_audio_arquivo()


if __name__ == "__main__":
    render()
