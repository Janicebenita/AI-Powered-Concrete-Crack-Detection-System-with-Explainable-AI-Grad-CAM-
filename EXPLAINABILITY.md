# Concrete Crack Reviewer: Explainability

## Decision and reasoning

The intended decision is whether the model outputs provide enough evidence to flag an image region for engineering review. The reasoning should identify the YOLOv8 bounding box or localization result, ResNet-18 crack classification, associated confidence values, and the Grad-CAM region influencing the prediction. A Grad-CAM heatmap explains model attention but does not prove that the highlighted feature is a crack or establish its structural significance.

## Inputs and data sources

Inputs include a concrete-surface image, preprocessing configuration, trained YOLOv8 and ResNet-18 model artifacts, detection or classification outputs, and Grad-CAM visualizations. The repository describes training and evaluation using a Concrete Surface Crack Image Dataset with crack and no-crack classes. Reported accuracy, precision, recall, F1, AUC, confusion-matrix, operational-impact, savings, and ROI figures should be connected to reproducible datasets, splits, code, model versions, and calculation assumptions before being treated as verified evidence.

## Limits and known constraints

The system can miss real cracks or incorrectly flag shadows, joints, stains, texture, lighting artifacts, or surface damage as cracks. Dataset shift, image quality, camera angle, preprocessing, threshold selection, and training-data representativeness can materially change performance. Bounding boxes and Grad-CAM do not measure crack depth, width, propagation, severity, load-bearing impact, or structural safety. The project is an inspection-support and research tool, and every result requires qualified human review and appropriate on-site assessment.

## Implementation in This Repository

The executable analysis is contained in `crack_detection.ipynb`, with its Python dependencies declared in `requirements.txt`. The notebook performs the repository's image preparation, model execution, evaluation, and Grad-CAM visualization steps; its rendered predictions and heatmaps are the evidence exposed to a reviewer.

The OpenGAP files document that concrete-image outputs are decision support only. No autonomous inspection, repair authorization, or structural-safety decision is implemented in this repository.
