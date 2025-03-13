# #first code
# from pydantic import BaseModel


# class User(BaseModel):
#     id: int
#     name: str = 'Jane Doe'

# user1=User(id=1)

# print(user1.id)
# print(user1.name)


#second code

from pydantic import BaseModel, Field, validator
from typing import List, Optional
import json
import openai

# Define a Pydantic model for LLM input
class LLMPrompt(BaseModel):
    prompt: str
    max_tokens: int = Field(default=100, ge=1, le=2000)
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)
    
    @validator('prompt')
    def prompt_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Prompt cannot be empty')
        return v

# Define a Pydantic model for LLM response
class LLMResponse(BaseModel):
    text: str
    usage: dict
    model: str


def call_llm(prompt_data: LLMPrompt) -> LLMResponse:
    # Set up your OpenAI API key
    openai.api_key = "your-api-key-here"
    
    # Make the actual API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_data.prompt}],
        max_tokens=prompt_data.max_tokens,
        temperature=prompt_data.temperature
    )
    
    # Parse the real response
    llm_response = {
        "text": response.choices[0].message.content,
        "usage": response.usage.to_dict(),
        "model": response.model
    }
    
    # Return as a Pydantic model
    return LLMResponse(**llm_response)

# Example usage
if __name__ == "__main__":
    # Create prompt with Pydantic
    prompt = LLMPrompt(
        prompt="Explain what Pydantic is",
        max_tokens=150,
        temperature=0.5
    )
    
    # Call the LLM
    response = call_llm(prompt)
    
    # Access validated response data
    print(f"Response: {response.text}")
    print(f"Token usage: {response.usage}")
    print(f"Model: {response.model}")
    
    # Serialize to JSON
    print("\nJSON output:")
    print(json.dumps(response.dict(), indent=2))










##third code
# from datetime import datetime

# from pydantic import BaseModel, PositiveInt
# # print(dir(pydantic))

# class User(BaseModel):
#     id: int  
#     name: str = 'John Doe'  
#     signup_ts: datetime | None  
#     tastes: dict[str, PositiveInt]  


# external_data = {
#     'id': 123,
#     'signup_ts': '2019-06-01 12:22',  
#     'tastes': {
#         'wine': 9,
#         b'cheese': 7,  
#         'cabbage': '1',  
#     },
# }

# user = User(**external_data)  

# print(user.id)  
# #> 123
# print(user.model_dump())  
# """
# {
#     'id': 123,
#     'name': 'John Doe',
#     'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
#     'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
# }
# """




