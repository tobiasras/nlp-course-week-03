import os
import dspy

def configure_dspy() -> None:
    """Configure DSPy to use the CampusAI OpenAI-compatible chat API."""
    if getattr(dspy.settings, "lm", None) is not None:
        return

    model = os.environ.get("CAMPUSAI_MODEL", "google/gemma-4-26b-a4b")
    api_base = os.environ.get("CAMPUSAI_API_URL", "https://api.campusai.compute.dtu.dk/v1")
    api_key = os.environ.get("CAMPUSAI_API_KEY", "")

    lm = dspy.LM(
        f"openai/{model}",
        api_base=api_base,
        api_key=api_key,
        model_type="chat",
    )
    dspy.configure(lm=lm, adapter=dspy.JSONAdapter())