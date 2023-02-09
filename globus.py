import tensorflow as tf
from transformers import pipeline

summ = pipeline("summarization")

f = open('GLO.txt','r')
GLO = f.read()
print(GLO)


