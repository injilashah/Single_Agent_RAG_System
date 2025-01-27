from langchain import hub
def prompt_template():
    prompt = hub.pull('hwchase17/openai-functions-agent')

    return prompt