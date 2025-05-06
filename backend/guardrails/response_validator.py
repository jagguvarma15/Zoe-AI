from guardrails import Guard
from guardrails.utils.reask_utils import get_reasks
from pathlib import Path

# Load RAIL definition
RAIL_PATH = Path(__file__).parent / "zoe.rail"
guard = Guard.from_rail(open(RAIL_PATH).read())

def validate_output(prompt: str, raw_output: str):
    validated_output, _ = guard(
        prompt_params={"user_input": prompt},
        output=raw_output,
    )

    reasks = get_reasks(validated_output)
    if reasks:
        print("⚠️ Guardrails re-asked for corrections.")
    return validated_output["response"]
