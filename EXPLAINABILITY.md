# Concrete Crack Reviewer: Explainability

## Decision and reasoning

The intended decision is whether the model outputs provide enough evidence to flag an image region for engineering review. The reasoning should identify the YOLOv8 bounding box or localization result, ResNet-18 crack classification, associated confidence values, and the Grad-CAM region influencing the prediction. A Grad-CAM heatmap explains model attention but does not prove that the highlighted feature is a crack or establish its structural significance.

## Inputs and data sources

Inputs include a concrete-surface image, preprocessing configuration, trained YOLOv8 and ResNet-18 model artifacts, detection or classification outputs, and Grad-CAM visualizations. The repository describes training and evaluation using a Concrete Surface Crack Image Dataset with crack and no-crack classes. Reported accuracy, precision, recall, F1, AUC, confusion-matrix, operational-impact, savings, and ROI figures should be connected to reproducible datasets, splits, code, model versions, and calculation assumptions before being treated as verified evidence.

## Limits and known constraints

The system can miss real cracks or incorrectly flag shadows, joints, stains, texture, lighting artifacts, or surface damage as cracks. Dataset shift, image quality, camera angle, preprocessing, threshold selection, and training-data representativeness can materially change performance. Bounding boxes and Grad-CAM do not measure crack depth, width, propagation, severity, load-bearing impact, or structural safety. The project is an inspection-support and research tool, and every result requires qualified human review and appropriate on-site assessment.

## Implementation in This Repository

`crack_detection.ipynb` contains the image preparation, model execution, evaluation, and Grad-CAM workflow. `agent.py` implements `review_detection(result)`, a deterministic review boundary that consumes the notebook/model outputs, bounds the reported probability, retains bounding boxes and Grad-CAM overlap as evidence, reports uncertainty when support is weak or missing, and always requires human inspection. `test_agent.py` verifies that localized evidence is preserved.

The worker does not pretend to run a model when artifacts are absent and does not infer crack depth or structural safety. No autonomous inspection, repair authorization, or structural-safety decision is implemented.
