text = """
In general, AI systems work by ingesting large amounts of labeled training data, analyzing the data for correlations and patterns, and using these patterns to make predictions about future states. 
In this way, a chatbot that is fed examples of text chats can learn to produce lifelike exchanges with people, or an image recognition tool can learn to identify and describe objects in images by reviewing millions of examples.
"""
print(text.split())
print(len(text.split()))

text1 = """
a b c A a b
"""

word_count = {}

for word in text1.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
print(word_count)