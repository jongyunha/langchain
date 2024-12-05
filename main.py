from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler

chat = ChatOpenAI(
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)


chef_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class international chef. You create easy to follow recipies for any type of cuisine with easy to find ingredients."),
    ("human", "I want to cook {cuisine} food.")
])

chef_chain = chef_prompt | chat

veg_chef_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a vegetarian chef specialized on making traditional recipes vegetarian. You find alternative ingredients and explain their preparation. You don't radically modify the recipe. If there is no alternative for a food just say you don't know how to recipe it."),
    ("human", "{recipe}")
])

veg_chef_chain = veg_chef_prompt | chat

final_chain = {"recipe": chef_chain} | veg_chef_chain

response = final_chain.invoke({
    "cuisine": "Italian"
})

print(response.content)