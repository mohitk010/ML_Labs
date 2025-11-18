"""
Log generator for a sample data processing pipeline.
Produces simulated logs for ingestion, transformation, and analysis steps.
"""

import logging
import random
import time

# Configure the logging system
logging.basicConfig(
    filename="pipeline_activity.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

log = logging.getLogger("Sample-Pipeline")

# Example stages that might appear in a real pipeline
pipeline_stages = [
    "data_ingest",
    "feature_extraction",
    "transcription",
    "model_inference",
    "result_packaging"
]

# Different outcomes for each stage
state_types = ["success", "warning", "error"]

print("Creating sample pipeline log data...")

for i in range(50):
    stage = random.choice(pipeline_stages)

    # Weighted distribution: 70% success, 20% warning, 10% error
    outcome = random.choices(state_types, weights=[70, 20, 10])[0]

    if outcome == "success":
        log.info(f"Stage '{stage}' completed successfully (task {i+1})")
    elif outcome == "warning":
        log.warning(f"Stage '{stage}' finished with a warning (task {i+1}) - processing slower than expected")
    else:
        log.error(f"Stage '{stage}' failed (task {i+1}) - operation timeout or processing error")

    time.sleep(0.1)

print("✔️ 50 log entries generated in 'pipeline_activity.log'")
