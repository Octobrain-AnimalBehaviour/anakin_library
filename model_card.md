# MonkeyEye Model Card

## Model Overview
MonkeyEye is an AI-powered system that analyzes video footage of wild and captive primates to detect signs of distress, injury, malnutrition, or illness. It combines species classification (YOLOv8), pose estimation (MMPOSE), and Retrieval-Augmented Generation (RAG) with a large language model (ChatGPT) to produce explainable, human-readable health reports.

## Intended Use
- Support zookeepers and field biologists in early detection of health problems.
- Monitor behavioral and postural changes in primates in low-resource or remote environments.
- Aid conservation efforts by enabling proactive care.

**Not Intended For**:
- Replacing veterinary diagnosis.
- Use without human verification.
- Non-primate species (without retraining).

## Architecture and Components
- **YOLOv8** for animal species classification across 27 classes.
- **MMPOSE** for 2D skeleton keypoint detection in primates.
- **ChatGPT + RAG** for contextual health inference using structured prompts and scientific literature.
- Modular Python library architecture (`anakin_library`) for customizable use.

## Training Data
- Classification model trained on 17,333 labeled animal images.
- Pose estimation based on the AP-10K dataset and in-house annotations.
- Scientific retrieval grounded in 15+ peer-reviewed animal health and behavior papers.

## Performance
- **YOLOv8 classifier**: 90.2% accuracy on 27 animal classes.
- **MMPOSE**: 73.1% average keypoint detection accuracy (AP-10K).
- Health reports align with expert assessments in test cases.

## Limitations
- May not distinguish between pathologies with overlapping visual features.
- Dependent on literature coverage and video visibility.
- Lower accuracy in night conditions or extreme occlusion.

## Ethical Considerations
- Designed for assistive—not diagnostic—use.
- Requires verification by trained human personnel.
- Data privacy respected (no human subjects involved).

## Additional Information
This model is part of the **Moodeng AI Challenge** submission under **Track 3 – Care and Connection Insights**.  
For full methodology, results, and implementation details, please refer to the accompanying Scientific Report.

