from ai.apps import AiConfig

co = AiConfig.co


def send_question(question: str) -> str:
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=question,
        max_tokens=40,
        temperature=0.6,
        stop_sequences=["--"])
    return response.generations[0].text
