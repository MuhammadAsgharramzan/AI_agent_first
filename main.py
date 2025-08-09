from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

external_client = AsyncOpenAI(
    api_key="AIzaSyDG_Fpjnf0JHFSX5w4tNDGpgwcbilU9MlY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

assitant = Agent(
    name="Assistant",
    instructions="""You are a helpful AI assistant. You can answer questions, provide information, and assist with tasks. Always be polite and concise. If you don't know the answer, say 'I don't know.' If the question is not clear, ask for clarification.""",
    )


result = Runner.run_sync(starting_agent=assitant, input = "hi how are you?.", run_config=config)
print(result.final_output)
    