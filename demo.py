import streamlit as st
from src.anakin_library.llm_manager import LLMManager
from src.anakin_library.video_manager import VideoManager
from src.anakin_library.vector_db_client import VectorDBClient
from src.anakin_library.preprocessing import load_files
import tempfile, os

def save_uploaded_pdfs_to_dirs(uploaded_pdfs):
    temp_dir = tempfile.mkdtemp()

    for pdf_file in uploaded_pdfs:
        pdf_path = os.path.join(temp_dir, pdf_file.name)

        with open(pdf_path, "wb") as f:
            f.write(pdf_file.read())

    return temp_dir

def save_uploaded_video(video_file):
    suffix = ".mp4"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(video_file.read())
        return tmp_file.name


def execute(self, frames:list, prompt1: str, prompt2: str, list_of_chunks: list):

        first_output = self.__llm_manager.analyze_video(frames, prompt1)

        snippets = self.__db_manager("Which disease is more associated to wrong posture?", "monkeys", list_of_chunks)

        second_output = self.__llm_manager.analyze_video_with_context(frames, prompt2, snippets, first_output)

        return second_output


def load_front():
    st.set_page_config(page_title="ANAKIN", layout="centered")

    st.title("Animal Behavior Analyzer: Monkey Eye")

    # Inicializa el estado si no está ya creado
    if "pdfs" not in st.session_state:
        st.session_state["pdfs"] = []
    if "video" not in st.session_state:
        st.session_state["video"] = None
    if "prompt1" not in st.session_state:
        st.session_state["prompt1"] = ""
    if "prompt2" not in st.session_state:
        st.session_state["prompt2"] = ""
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = ""
    if "report" not in st.session_state:
        st.session_state["report"] = ""
    if "pdfs_uploaded" not in st.session_state:
        st.session_state["pdfs_uploaded"] = False

    st.header("🔑 Introduce your Open AI Key")
    api_key = st.text_input("API Key", type="password", value=st.session_state["api_key"])
    st.session_state["api_key"] = api_key

    st.header("📝 Introduce your Prompts")
    prompt1 = st.text_area("Prompt 1: First analysis", value=st.session_state["prompt1"], height=300)
    prompt2 = st.text_area("Prompt 2: Second analysis based on relevant paper info", value=st.session_state["prompt2"], height=300)
    st.session_state["prompt1"] = prompt1
    st.session_state["prompt2"] = prompt2

    st.header("📄 Load your relevant pdfs to create a Knowledge Base")
    uploaded_pdfs = st.file_uploader(
        "Select one or more PDFs",
        type="pdf",
        accept_multiple_files=True,
        key="pdf_uploader"
    )

    if uploaded_pdfs:
        st.session_state["pdfs"] = uploaded_pdfs
        st.session_state["pdfs_uploaded"] = True
        st.success(f"{len(uploaded_pdfs)} PDF(s) cargado(s).")

    st.header("🎥 Load an MP4 video")
    uploaded_video = st.file_uploader(
        "Select a video, MP4",
        type=["mp4"],
        key="video_uploader"
    )

    if uploaded_video:
        st.session_state["video"] = uploaded_video  # Just one video, not a list
        st.video(uploaded_video)

    st.markdown("---")

    # Botón de procesamiento
    if st.button("🚀 Start"):
        if not st.session_state["api_key"]:
            st.error("Please, introduce the API Key.")
        elif not st.session_state["prompt1"] or not st.session_state["prompt2"]:
            st.error("Please, introduce both prompts")
        elif not st.session_state["pdfs"]:
            st.error("Please load at least one PDF.")
        elif not st.session_state["video"]:
            st.error("Please load at least one video")
        else:
            api_key = st.session_state["api_key"]
            prompt1 = st.session_state["prompt1"]
            prompt2 = st.session_state["prompt2"]

            llm_manager = LLMManager(api_key)
            video_manager = VideoManager()
            db_manager = VectorDBClient(".")

            # Step 1: Guardar PDFs
            with st.spinner("📁 Loading and preparing PDFs..."):
                pdf_dirs = save_uploaded_pdfs_to_dirs(st.session_state["pdfs"])
                list_of_chunks = load_files(pdf_dirs)

            st.success(f"✅ {len(list_of_chunks)} passages have been processed")

            with st.spinner("🎞️ Loading and preparing video..."):
                video_path = save_uploaded_video(st.session_state["video"])
                frames = video_manager.upload_video(video_path)

            st.success("✅ Video has been processed, {} frames are ready".format(len(frames)))

            with st.spinner("🎞️ Analizing video based on first prompt..."):
                first_output, question = llm_manager.analyze_video(frames, prompt1)

            st.success("✅ First analysis ready...")

            answer = None
            if question:
                with st.spinner("🎞️ Searching appropriate references"):

                    snippets = db_manager(question, "monkeys", list_of_chunks)
                    texts = "\n".join([psg["snippet"] for psg in snippets])

                    st.success("✅ Snippets ready...")

                with st.spinner(" Analyzing video - Second iteration"):
                    answer = llm_manager.analyze_video_with_context(None, prompt2, texts, first_output)

            st.session_state["report"] = first_output+"\n\n\n"+ answer if answer else first_output

    # Mostrar resultado
    st.header("📊 Report")
    st.write(st.session_state["report"])

load_front()
