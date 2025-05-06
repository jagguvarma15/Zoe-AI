from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_precision,
    context_recall,
    answer_semantic_similarity,
)
from ragas.evaluation import evaluate
from datasets import Dataset
import uuid

def evaluate_ragas(query: str, answer: str, contexts: list[str]):
    dataset = Dataset.from_dict({
        "question": [query],
        "answer": [answer],
        "contexts": [contexts]
    })

    result = evaluate(
        dataset,
        metrics=[
            answer_relevancy,
            faithfulness,
            context_recall,
            context_precision,
            answer_semantic_similarity,
        ]
    )

    return result.to_pandas().to_dict("records")[0]
