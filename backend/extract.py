from __future__ import annotations
from typing import List
import dspy
from dspy_setup import configure_dspy

_predictor = None

def _get_predictor():
    global _predictor
    if _predictor is None:
        configure_dspy()
        _predictor = dspy.Predict(_extract_persons_signature())
    return _predictor


def _extract_persons_signature():
    class ExtractPersons(dspy.Signature):
        """Extract names of real people mentioned in the text.
        Return only person names. Do not include places, organizations, product
        names, street names, or metaphorical uses of a name like (Einsteins sum). 

        Be very strict about what not to include
        """
        text: str = dspy.InputField(desc="Text that may mention people.")
        persons: list[str] = dspy.OutputField(
            desc="Person names in the order they appear. Empty list if none."
        )
    return ExtractPersons


def campusai_extract_persons(text: str) -> List[str]:
    """Extract person names from text via CampusAI using DSPy."""
    result = _get_predictor()(text=text)
    persons = result.persons
    if persons is None:
        return []
    if isinstance(persons, str):
        persons = [persons]
    return [str(name).strip() for name in persons if str(name).strip()]
