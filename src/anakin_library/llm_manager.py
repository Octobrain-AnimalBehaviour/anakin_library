
from src.anakin_library.config import logger
import json, time
from unidecode import unidecode
from openai import OpenAI
from typing import List
import re

class LLMManager:
    def __init__(self, openai_key:str):
        self.__client = OpenAI(api_key=openai_key)
        self.__qq_prompt = "Formulate a concreate but justify question related to your findings to feed a rag vector db. Return the questions in this format <QUESTION>Your question</QUESTION>"

    def analyze_video(self, frames:List, prompt:str):

        prompt += self.__qq_prompt

        try:
            content = self.__call_gpt(frames, prompt, 0)
            question = None

            if "QUESTION" in content:
                question = content.split("</QUESTION>")[0]
                question = question.split("<QUESTION>")[1]

            return content, question

        except Exception as e:
            logger.info("Unexpected error while parsing the json output: {}".format(e))
            time.sleep(5)

        return None


    def analyze_video_with_context(self, frames: List, prompt: str, passages:str, details:str):

        if not passages and not details:
            return None

        request_prompt = prompt.replace("PASSAGES", passages).replace("DETAILS", str(details))

        return self.__call_gpt(frames, request_prompt, 0)


    def __call_gpt(self, frames: List, request_prompt: str, tries=0):

        if tries > 3:
            logger.info("Maximum limit of calls reached (3)")
            return None

        if frames:
            prompt_messages = [
                {
                    "role": "user",
                    "content": [unidecode(request_prompt), *map(lambda x: {"image": x, "resize": 768}, frames), ],
                },
            ]
        else:
            prompt_messages = [
                {
                    "role": "user",
                    "content": unidecode(request_prompt),
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
