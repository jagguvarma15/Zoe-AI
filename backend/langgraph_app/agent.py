from guardrails.response_validator import validate_output
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.evaluator import evaluate
from evaluation_logger import log_evaluation
from ragas_evaluator import evaluate_ragas
import uuid

def run_agent(query: str, session_id: str):
    # 1. Run chain
    raw = qa_chain.run(query)

    # 2. Validate with Guardrails
    validated = validate_output(query, raw)

    # 3. Retrieve context
    retrieved_docs = vectorstore.similarity_search(query, k=3)
    retrieval_context = [doc.page_content for doc in retrieved_docs]

    # 4. DeepEval
    test_case = LLMTestCase(
        id=str(uuid.uuid4()),
        input=query,
        actual_output=validated,
        retrieval_context=retrieval_context,
        expected_output=None
    )
    deepeval_results = evaluate(
        [test_case],
        metrics=[
            AnswerRelevancyMetric(threshold=0.6),
            FaithfulnessMetric(threshold=0.6),
        ]
    )[0].__dict__
    print("🧪 DeepEval:", deepeval_results)

    # 5. RAGAS
    ragas_results = evaluate_ragas(query, validated, retrieval_context)
    print("📊 RAGAS:", ragas_results)

    # 6. Log both evaluations
    log_evaluation({
        "session_id": session_id,
        "query": query,
        "response": validated,
        "metrics": {
            "deepeval": deepeval_results,
            "ragas": ragas_results
        }
    })

    # 7. Return final validated response
    return {"response": validated}
