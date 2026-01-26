"""RagaliQ - LLM Testing Framework for RAG Systems."""

from ragaliq.core.test_case import RAGTestCase, RAGTestResult
from ragaliq.core.evaluator import Evaluator, EvaluationResult
from ragaliq.core.runner import RagaliQ

__version__ = "0.1.0"

__all__ = [
    "RagaliQ",
    "RAGTestCase",
    "RAGTestResult",
    "Evaluator",
    "EvaluationResult",
]
