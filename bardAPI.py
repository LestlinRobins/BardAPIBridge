from bardapi import Bard
import os

os.environ['_BARD_API_KEY']="Wgi1NHsDGaZdByqoz2iGw6E4s7GgCFRwGwXkFIQ6kXFpVu3NG8aUdjAL1edu0b5q52geQA."
a=Bard().get_answer("write captions for an image of a cat")['content']
print(a)
