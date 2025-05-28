
from anakin_library.config import logger
import json, time
from unidecode import unidecode
from openai import OpenAI
from typing import List


class LLMManager:
    def __init__(self, openai_key:str):
        self.__client = OpenAI(api_key=openai_key)

    def analyze_video(self, frames:List, prompt:str, tries=0):

        if tries > 3:
            logger.info("Maximum limit of tries reached (3)")
            return None

        try:
            content = self.__call_gpt(frames, prompt, 0)

            if len(content.split("json", maxsplit=1)) > 1:
                first_cut = content.split("json", maxsplit=1)[1]
                second_cut = first_cut[::-1].split("```", maxsplit=1)[1]
                final_json = second_cut[::-1]

                json_obj = json.loads(final_json)
                return json_obj

        except Exception as e:
            logger.info("Unexpected error while parsin the json output: {}".format(e))
            time.sleep(5)

            self.analyze_video(frames, prompt, tries=tries + 1)

        return None


    def analyze_video_with_context(self, frames: List, prompt: str, passages=None, details=None):

        if not passages and not details:
            return None

        request_prompt = prompt.replace("PASSAGES", passages).replace("DETALLES", str(details))

        return self.__call_gpt(frames, request_prompt, 0)


    def __call_gpt(self, frames: List, request_prompt: str, tries=0):

        if tries > 3:
            logger.info("Maximum limit of calls reached (3)")
            return None

        prompt_messages = [
            {
                "role": "user",
                "content": [unidecode(request_prompt), *map(lambda x: {"image": x, "resize": 768}, frames), ],
            },
        ]

        params = {
            "model": "gpt-4o",
            "messages": prompt_messages
        }

        try:
            result = self.__client.chat.completions.create(**params)
            logger.info("Finished called to OpenAI API")
            logger.info(f"Result: {result}")

            return result.choices[0].message.content

        except Exception as e:
            logger.info("Unexpected error from GPT-side: {}".format(e))
            time.sleep(5)

            self.__call_gpt(frames, request_prompt, tries=tries + 1)

        return None
