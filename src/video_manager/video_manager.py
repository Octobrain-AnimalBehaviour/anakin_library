
import cv2
import pathlib
import base64
from PIL import Image
from io import BytesIO
import numpy as np
from src.common.config import logger
from ultralytics import YOLO
from typing import List

class VideoManager:

    def __init__(self, sample_rate:int = 30, max_frames:int =15, mmpose_model_name:str = None,
                 mmpose_model_path:str = None, custom_filter_model:str = None, classes:List = []):
        assert sample_rate > 0 == "The sample_rate must be greater than zero."
        assert max_frames > 0 == "The max_frames must be greater than zero."

        self.__sample_rate = sample_rate
        self.__max_frames = max_frames
        self.__frames = []
        self.__frames_skeleton = []
        self.__clases = classes

        if custom_filter_model:
            self.__model = YOLO(custom_filter_model)
        else:
            self.__model = None

        self.__filtering = True if custom_filter_model else False

        if mmpose_model_path:
            self.__inference = self.__load_skeleton_model(mmpose_model_name, mmpose_model_path)
        else:
            self.__inference = None

    def upload_video(self, video_path: str):

        self.__frames = self.__sample_video(video_path)

        if self.__inference:
            self.__frames_skeleton = self.__extract_skeleton()

    def __load_skeleton_model(self, mmpose_model_name:str, mmpose_model_path:str):
        from mmpose.apis import MMPoseInferencer

        if mmpose_model_path:
            assert mmpose_model_name != None
            return MMPoseInferencer(pose2d=mmpose_model_name, pose2d_weigths =mmpose_model_path)

        else:
            return MMPoseInferencer(pose2d=mmpose_model_name)

    def __sample_video(self, video_path:str):
        assert pathlib.Path(video_path).suffix == ".mp4", "The video extension should be .mp4"

        frames = []
        video = cv2.VideoCapture(video_path)

        idx_frame = 0

        while video.isOpened():
            success, frame = video.read()
            if not success:
                break

            if idx_frame % self.__sample_rate == 0:
                pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                if self.__filtering:
                    results = self.__model(pil_img)
                    prediction = results[0].names[results[0].probs.top1]

                    if prediction in self.__clases:
                        frames.append(pil_img)
                else:
                    frames.append(pil_img)

            idx_frame += 1

        assert len(frames) > 0 == "Current sample_rate return zero frames."
        logger.info("Returning video with {} frames sampled".format(len(frames)))

        return frames

    def __extract_skeleton(self):
        base64Frames = []

        for frame in self.__frames:
            result_generator = self.__inference(frame, radius=4, thickness=4, return_vis=True)

            result = next(result_generator)
            vis_image = result['visualization'][0]

            # Convert the visualization image from RGB to BGR (OpenCV uses BGR)
            vis_image = cv2.cvtColor(vis_image, cv2.COLOR_RGB2BGR)

            cv2.imshow("WINDOW", vis_image)

            base64_img = self.__transforme_to_base64(vis_image)
            base64Frames.append(base64_img)

        return base64Frames

    def __transforme_to_base64(self, frame):
        pil_image = Image.fromarray(np.squeeze(frame))  # Convertir a imagen PIL
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return img_str