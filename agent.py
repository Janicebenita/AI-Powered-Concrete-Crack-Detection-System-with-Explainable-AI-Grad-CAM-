"""Explain model-produced concrete crack evidence for human inspection."""
from __future__ import annotations


def review_detection(result: dict) -> dict:
    """Review detector/classifier outputs; this function does not infer an image."""
    probability = min(max(float(result.get("crack_probability", 0.0)), 0.0), 1.0)
    boxes = list(result.get("bounding_boxes") or [])
    gradcam_overlap = result.get("gradcam_overlap")
    status = "crack-evidence" if probability >= 0.5 or boxes else "no-crack-evidence"
    uncertainty = "high" if probability < 0.65 or gradcam_overlap is None else "moderate"
    return {
        "status": status,
        "crack_probability": probability,
        "localized_regions": len(boxes),
        "gradcam_overlap": gradcam_overlap,
        "uncertainty": uncertainty,
        "evidence": {"probability": probability, "bounding_boxes": boxes, "gradcam_overlap": gradcam_overlap},
        "limitations": ["Does not measure crack depth, width, propagation, or structural safety."],
        "human_inspection_required": True,
    }
