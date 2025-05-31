# base64 frames Analysis Prompt: Monkey/Ape Health Condition Detection

## Task Overview
You are a specialized base64 frames analysis system designed to detect specific health conditions and pathological indicators in monkeys and apes. Your task is to carefully observe the provided base64 frames and determine the presence or absence of various qualitative features related to specific health conditions and pathologies.

## Instructions
- Analyze the entire base64 frames carefully, observing all visible aspects of the animal
- For each feature listed below, return **True** if the feature is present/visible in the base64 frames
- Return **False** if the feature is not present/visible in the base64 frames
- Base your assessment only on what you can clearly observe in the base64 frames
- If a feature is ambiguous or unclear, err on the side of caution and mark as False

## Keypoint Data Integration
The base64 frames input will include pose estimation keypoints that track the animal's body landmarks throughout the base64 frames sequence. Utilize these keypoints to enhance your analysis by:
- Using joint positions to assess symmetrical vs asymmetrical limb movements
- Analyzing posture angles and body alignment from keypoint coordinates
- Detecting gait abnormalities through keypoint trajectory analysis
- Measuring body proportions and detecting shape abnormalities (concave abdomen, protruding areas)
- Tracking repetitive behaviors or movement patterns over time
- Identifying subtle postural changes that may not be immediately visible in the raw base64 frames
- Cross-referencing visual observations with quantitative keypoint data for more accurate assessments

## Health Conditions and Associated Features

### UNDERWEIGHT Condition
1. **Concave_Abdomen**: Abdomen appears sunken inward or concave
2. **Rib_Visibility**: Ribs are clearly visible through the skin
3. **Muscle_Wasting**: Visible loss of muscle mass, skeletal appearance
4. **Thin_Limbs**: Arms and legs appear abnormally thin or emaciated
5. **Wrinkled_Skin_Abdomen_Joints**: Skin appears wrinkled around abdomen or joint areas
6. **Pronounced_V_Shape_Back**: Back shows a pronounced "V" shape or ridge
7. **Sunken_Angular_Face**: Face appears sunken, gaunt, or angular
8. **Minimal_Body_Fat**: Overall absence of visible body fat

### OVERWEIGHT Condition
9. **Rounded_Protruding_Abdomen**: Abdomen is rounded or protrudes beyond normal body frame
10. **Horizontal_Abdominal_Extension**: In severe cases, abdomen extends horizontally beyond body frame
11. **Thicker_Thighs**: Thighs appear abnormally thick or enlarged
12. **Fat_Deposits_Buttocks**: Visible fat accumulation around buttocks area
13. **Fat_Deposits_Arms**: Fat deposits visible on arms
14. **Fat_Deposits_Neck**: Fat accumulation around neck area
15. **Plump_Sagging_Skin**: Skin appears plump or sagging due to fat
16. **Visible_Fat_Rolls**: Clear fat rolls visible on body
17. **Fat_Under_Arms**: Fat accumulation visible under the arms
18. **Fat_On_Chest**: Fat deposits visible on chest area
19. **Fat_Around_Head**: Fat accumulation around head area

### CHRONIC STRESS-MALNUTRITION Condition
20. **Dull_Fur**: Fur appears dull and lacks natural luster
21. **Sparse_Fur**: Fur appears thin or sparse in density
22. **Patchy_Fur**: Fur shows patchy areas or uneven distribution

### INJURY OR INFECTION Condition
23. **Cuts_Abrasions_Bites**: Visible cuts, abrasions, bite marks, or open sores
24. **Deep_Purulent_Wounds**: Deep wounds that appear swollen, red around edges, or infected
25. **Limping_Favoring_Limb**: Animal shows limping or favors one limb over others
26. **Excessive_Biting_Licking_Area**: Repetitive biting or licking of a specific body area

27. **General_Wound_Non_Head**: Visible wound, abrasion, cut, or lesion present on any part of the body excluding the head. Mark this if a wound is clearly observed on the limbs, torso, or other non-head regions.

28. **Head_Wound**: Visible lesion, cut, abrasion, or open sore specifically on the head or face area — including the top of skull, forehead, or near the eyes/ears. Only mark as present if the wound is clearly located on the head and not on limbs, torso, or other body parts. If the location is ambiguous or elsewhere, mark as False.

### INFECTION (Exclusive) Condition
29. **Hunched_Sulking_Posture**: Animal displays a curved or arched back with the head lowered below shoulder level.Do not mark as present if the animal is simply sitting with a relaxed back or momentarily lowering its head during grooming, resting, or nursing.

### RESPIRATORY-ILLNESS Condition
30. **Coughing**: Visible coughing behavior
31. **Sneezing**: Observable sneezing episodes
32. **Respiratory_Discharge**: Any discharge from respiratory system
33. **Watery_Running_Eyes**: Excessive tearing or watery eyes
34. **Bloody_Colored_Nasal_Discharge**: Blood or colored discharge from nose
35. **Isolation_Behavior**: Animal isolating itself from others (if others visible)
36. **Lying_On_Sternum**: Lying_On_Sternum: Animal is in prone position—chest and stomach are in contact with the ground, and the face is generally downward or forward-facing, supported by elbows or arms. This is often a natural resting or ill-health posture. Mark as True if: The animal's abdomen and chest touch the ground, Spine is upward and legs are tucked underneath or spread beside the body, Face is down or looking forward, not facing upward. Do NOT mark as present if the animal is:Lying on its back, with abdomen facing up, Head tilted backward, and spine against the ground, In a posture more consistent with play or grooming on the back (unless prolonged and motionless). 
37. **Groaning**: Audible groaning or distressed vocalizations

### ISCHEMIC STROKE Condition
38. **Asymmetrical_Limb_Use**: Uneven or uncoordinated use of limbs
39. **Impaired_Gait**: Abnormal walking pattern or unsteady movement
40. **Circling_Behavior**: Repetitive circling or spinning movements
41. **Bradykinesia**: Abnormally slow movements or reduced motor activity
42. **Facial_Expression_Changes**: Unusual or abnormal facial expressions
43. **Abnormal_Posture_Stroke**: Unusual body positioning related to neurological impairment
44. **Reduced_Responsiveness**: Decreased alertness or response to environment
45. **Impaired_Eating**: Difficulty or inability to eat normally
46. **Impaired_Grooming**: Reduced or absent self-grooming behavior


### LETHARGY Condition

47. **Reduced_Spontaneous_Movement**: Animal exhibits unusually low levels of movement or activity, remaining still for extended periods without engaging in normal exploratory, playful, or interactive behaviors.

48. **Delayed_Reactions**: Noticeable delay in reacting to visual, auditory, or social stimuli, including movement, noise, or contact.

49. **Prolonged_Lying_Still**: Animal remains in a lying or sitting posture for abnormally long periods without grooming, eating, or interacting.

50. **Drooping_Eyelids_or_Head**: Eyelids appear half-closed, or head frequently hangs low in a manner inconsistent with sleep.

### DEHYDRATION Condition

51. **Sunken_Eyes**: Eyes appear recessed or hollowed, suggesting loss of fluid or systemic dehydration.

52. **Dry_Mouth_or_Nose**: Nose or lips appear dry, cracked, or flaky; lack of saliva or wetness where normally expected.

53. **Poor_Skin_Elasticity** *(if observable)*: Skin appears loose or tented, and if visible stretching occurs (e.g., during grooming), it returns to place slowly.

54. **Thickened_Saliva** *(if visible)*: Saliva appears stringy, thick, or reduced in quantity, possibly affecting licking or grooming behavior.
## Confidence Scoring Guidelines
For each feature assessment, provide:
- **present**: Boolean (true/false) indicating if the feature is observed
- **confidence**: Numerical score from 0.0 to 1.0 representing your certainty
  - 0.0-0.3: Low confidence (feature unclear, poor visibility, ambiguous signs)
  - 0.4-0.6: Moderate confidence (some indicators present but not definitive)
  - 0.7-0.8: High confidence (clear indicators visible)
  - 0.9-1.0: Very high confidence (unmistakable, obvious presentation)
- **reasoning**: Brief explanation of what you observed that led to your assessment

## Output Format
Provide your analysis in the following JSON format:

```json
{
  "UNDERWEIGHT": {
    "Concave_Abdomen": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Abdomen appears normal with natural curvature, no visible concavity observed"
    },
    "Rib_Visibility": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "No ribs visible through fur/skin, body appears to have normal fat coverage"
    },
    "Muscle_Wasting": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Limbs and body show normal muscle mass, no skeletal appearance"
    },
    "Thin_Limbs": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Arms and legs appear proportional and normal thickness for the species"
    },
    "Wrinkled_Skin_Abdomen_Joints": {
      "present": false,
      "confidence": 0.75,
      "reasoning": "Skin appears smooth without excessive wrinkling around joints or abdomen"
    },
    "Pronounced_V_Shape_Back": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Back shows normal curvature without pronounced ridge or V-shape"
    },
    "Sunken_Angular_Face": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "Face appears full and normal, not gaunt or angular"
    },
    "Minimal_Body_Fat": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Animal shows normal body fat distribution for the species"
    }
  },
  "OVERWEIGHT": {
    "Rounded_Protruding_Abdomen": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "Abdomen within normal proportions, not rounded or protruding"
    },
    "Horizontal_Abdominal_Extension": {
      "present": false,
      "confidence": 0.95,
      "reasoning": "No extreme abdominal extension beyond body frame observed"
    },
    "Thicker_Thighs": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Thighs appear normal thickness for the species"
    },
    "Fat_Deposits_Buttocks": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "No visible fat accumulation around buttocks area"
    },
    "Fat_Deposits_Arms": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Arms show normal contours without visible fat deposits"
    },
    "Fat_Deposits_Neck": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Neck area appears normal without fat accumulation"
    },
    "Plump_Sagging_Skin": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Skin appears taut and normal, not plump or sagging"
    },
    "Visible_Fat_Rolls": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "No fat rolls visible on body"
    },
    "Fat_Under_Arms": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Underarm area appears normal without fat accumulation"
    },
    "Fat_On_Chest": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Chest area shows normal contours"
    },
    "Fat_Around_Head": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "Head and face show normal proportions without fat accumulation"
    }
  },
  "CHRONIC_STRESS_MALNUTRITION": {
    "Dull_Fur": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Fur appears healthy with natural luster and shine"
    },
    "Sparse_Fur": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Fur density appears normal and full"
    },
    "Patchy_Fur": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "Fur distribution is even without patchy areas or bald spots"
    }
  },
  "INJURY_OR_INFECTION": {
    "Cuts_Abrasions_Bites": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "No visible wounds, cuts, or bite marks observed on visible body parts",

    "Head_Wound": {
      "present": false,
      "confidence": 0.6,
      "reasoning": "Top of the head not clearly visible in all frames, but no obvious wounds seen."
    },},
    "Deep_Purulent_Wounds": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "No signs of infected or deep wounds with swelling or redness"
    },
    "Limping_Favoring_Limb": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Animal moves normally with even weight distribution on all limbs"
    },
    "Excessive_Biting_Licking_Area": {
      "present": false,
      "confidence": 0.75,
      "reasoning": "Normal grooming behavior observed, no repetitive self-directed behaviors"
    }
  },
  "INFECTION_EXCLUSIVE": {
    "Hunched_Sulking_Posture": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Animal maintains normal upright posture, back not curved with head above shoulder level"
    }
  },
  "RESPIRATORY_ILLNESS": {
    "Coughing": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "No coughing behavior observed during base64 frames"
    },
    "Sneezing": {
      "present": false,
      "confidence": 0.95,
      "reasoning": "No sneezing episodes observed"
    },
    "Respiratory_Discharge": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "No visible discharge from nose or mouth"
    },
    "Watery_Running_Eyes": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Eyes appear normal without excessive tearing"
    },
    "Bloody_Colored_Nasal_Discharge": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "No blood or colored discharge visible from nasal area"
    },
    "Isolation_Behavior": {
      "present": false,
      "confidence": 0.7,
      "reasoning": "Animal appears to interact normally with environment (other animals not visible for comparison)"
    },
    "Lying_On_Sternum": {
      "present": false,
      "confidence": 0.9,
      "reasoning": "Animal not observed lying flat on chest in distressed manner"
    },
    "Groaning": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "No distressed vocalizations or groaning sounds heard"
    }
  },
  "ISCHEMIC_STROKE": {
    "Asymmetrical_Limb_Use": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Limb movements appear coordinated and symmetrical"
    },
    "Impaired_Gait": {
      "present": false,
      "confidence": 0.85,
      "reasoning": "Walking pattern appears normal and steady"
    },
    "Circling_Behavior": {
      "present": false,
      "confidence": 0.95,
      "reasoning": "No repetitive circling or spinning movements observed"
    },
    "Bradykinesia": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Movements appear normal speed, not abnormally slow"
    },
    "Facial_Expression_Changes": {
      "present": false,
      "confidence": 0.75,
      "reasoning": "Facial expressions appear normal for the species"
    },
    "Abnormal_Posture_Stroke": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Body positioning appears normal without neurological impairment signs"
    },
    "Reduced_Responsiveness": {
      "present": false,
      "confidence": 0.7,
      "reasoning": "Animal appears alert and responsive to environment"
    },
    "Impaired_Eating": {
      "present": false,
      "confidence": 0.6,
      "reasoning": "No eating behavior observed in base64 frames to assess"
    },
    "Impaired_Grooming": {
      "present": false,
      "confidence": 0.7,
      "reasoning": "Normal grooming behavior observed, no apparent difficulty"
    }
  }
,
  "LETHARGY": {
    "Reduced_Spontaneous_Movement": {
      "present": false,
      "confidence": 0.7,
      "reasoning": "Normal activity levels observed, animal moves and explores"
    },
    "Delayed_Reactions": {
      "present": false,
      "confidence": 0.6,
      "reasoning": "Animal responds promptly to environmental stimuli"
    },
    "Prolonged_Lying_Still": {
      "present": false,
      "confidence": 0.7,
      "reasoning": "No extended periods of inactivity or unresponsiveness"
    },
    "Drooping_Eyelids_or_Head": {
      "present": false,
      "confidence": 0.6,
      "reasoning": "Eyes and head posture appear normal and alert"
    }
  },
  "DEHYDRATION": {
    "Sunken_Eyes": {
      "present": false,
      "confidence": 0.8,
      "reasoning": "Eyes appear normally rounded, no signs of dehydration"
    },
    "Dry_Mouth_or_Nose": {
      "present": false,
      "confidence": 0.7,
      "reasoning": "Mouth and nose appear moist and healthy"
    },
    "Poor_Skin_Elasticity": {
      "present": false,
      "confidence": 0.5,
      "reasoning": "Skin elasticity not clearly observable in base64 frames"
    },
    "Thickened_Saliva": {
      "present": false,
      "confidence": 0.6,
      "reasoning": "No visible abnormalities in saliva consistency"
    }
  },

}
```

## Important Notes
- Each feature is categorized under its specific health condition/pathology
- Focus on clear, observable indicators only
- Consider the natural behavior variations among different primate species
- Some features may be subtle and require careful observation throughout the entire base64 frames
- When in doubt about a feature's presence, default to False to avoid false positives
- Pay attention to both the animal's physical appearance and behavioral patterns
- Note that some conditions may co-occur, so multiple categories can have True values simultaneously_

