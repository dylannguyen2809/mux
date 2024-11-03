from openai import OpenAI
import os

client = OpenAI()

def summarizer(transcript):
    text = " ".join(transcript)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a language teacher reviewing the following transcript with a student. Please provide a review of how they did, what improvements they could do, and an encouraging message to help them continue their studies. compose the message like a text, without adding explicit headers for each section."},
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return completion.choices[0].message.content

test = [
    "Student: 你好，教授！今天我们可以练习中文吗？",
    "Professor: 当然可以！你想练习什么内容？",
    "Student: 我想练习一些日常对话，比如问路和购物。",
    "Professor: 好的。我们先从问路开始吧。你可以问我怎么去图书馆。",
    "Student: 请问，图书馆怎么走？",
    "Professor: 图书馆在校园的北边。你可以沿着这条路一直走，然后在第二个路口左转。",
    "Student: 谢谢教授！那购物呢？",
    "Professor: 你可以试着问我一些关于价格和商品的问题。",
    "Student: 好的。请问，这个苹果多少钱？",
    "Professor: 这个苹果三块钱一个。你还想买什么？",
    "Student: 我还想买一些蔬菜。",
    "Professor: 好的。你可以问我蔬菜的价格。",
    "Student: 请问，这些蔬菜多少钱？",
    "Professor: 这些蔬菜五块钱一斤。",
    "Student: 谢谢教授！今天的练习对我很有帮助。",
    "Professor: 不客气！继续加油，你的中文会越来越好的。"
]

print(summarizer(test))
