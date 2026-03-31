from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()

model = "claude-sonnet-4-0"

msg = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
           "role": "user",
           "content": "what is quantum computing in one sentence" 
        }
    ]
    
)

print(msg)


