mport re
import string
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib inline
from plotly import graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from collections import Counter

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


import nltk
from nltk.corpus import stopwords

from tqdm import tqdm
import os
import nltk
import spacy
import random
from spacy.util import compounding
from spacy.util import minibatch


class Useraccount:

    def __init__(self,alias,email, tweets, followers, timeline, retweets):
        self.alias = alias
        self.__email = email
        self.tweets = tweets
        self.__followers = followers
        self.__timeline = timeline
        self.__retweets = retweets()

    def Follow(self,Useraccount):
        Useraccount.alias.append(Useraccount.__followers)


    def Tweetear(self, alias, tweets, Useracoount):
        if self.alias == True:
            print ("si desea publicar un tweet pulse T, si no pulse cualquier tecla ")
            if input() == "T" :
                if len.tweets > 140:
                    print("este mensaje tiene mas de 140 digitos")
                else:

                self.tweets.append(input("introduzca su tweet:"))
                self.alias.__timeline.append(Useracoount.tweets)
            else:
                break





class Twitter(Useraccount):

   def __init__(self,alias,email,tweets):
       self.alias = alias
       self.email = email
       self.tweets = tweets

   def Mensajedirecto(self, Useraccount,mensajes, ):
       self.Useraccount.alias.mensajes = mensajes
       mensajes = ()
       Useraccount.input("introduzca su mensaje").append(mensajes)
       self.Useraccount.alias.print(mensajes)

   def Retweet (self,mensajes,alias):
       word = int(input("introduzca el numero del tweet que desea retweetear:"))
       mensajes = mensajes
       self.Useraccount.mensajes(word).append.followers.timeline
       self.Useraccount.mensajes(word).append.retweets


