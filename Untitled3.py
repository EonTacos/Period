#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
import gradio


# In[2]:


openai.api_key = "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"


# In[3]:


messages = [{"role": "system", "content": "You are a] reproductive health expert and you specialize in electrolytes"}]


# In[ ]:





# In[4]:


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


# In[5]:


demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Guardian Angel")

demo.launch(share=True)

