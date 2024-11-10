from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from ouput_parser import CommandOutputParser

chat = ChatOpenAI(
    temperature=0.5,
)

template = ChatPromptTemplate.from_messages([
    ("system",
     "You are alist generating machine. Everything you are asked will be answered with a comma seperated list of max {max_items}. Do NOT reply with anything else."),
    ("human", "{question}"),
])

chain = template | chat | CommandOutputParser()
response = chain.invoke({
    "max_items": 5,
    "question": "What are the popular npm packages?"
})

print(response)
