from src.anakin_library.llm_manager import LLMManager
from src.anakin_library.video_manager import VideoManager
from src.anakin_library.vector_db_client import VectorDBClient

def demo():
    OPENAI_API_KEY2 = "the open ai key"

    db_location = "the folder where you want to store the db"
    upload_video = r"the video path"
    pdfs_dir = r"the directory of the files"

    llm_manager = LLMManager(OPENAI_API_KEY2)
    video_manager = VideoManager()
    db_manager = VectorDBClient(db_location)

    prompt1 = "Please analyze this frames in base 64 and tell me what is this about"
    prompt2 = "Write a report about the condition of the animal"

    frames = video_manager.upload_video(upload_video)
    first_output, question = llm_manager.analyze_video(frames, prompt1)

    if question:
        snippets = db_manager(question, "monkeys", [])
        texts = "\n".join([psg["snippet"] for psg in snippets])
        print("Snippets", snippets)
        second_output = llm_manager.analyze_video_with_context(frames, prompt2, texts, first_output)

        print(second_output)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo()

