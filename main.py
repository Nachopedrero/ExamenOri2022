
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

tweets = ()

from cuenta import Useraccount
cuenta1 = Useraccount(Nacho,nachopedrero@gmail.com,tweets,followers,timeline,retweets)
cuenta2 = Useraccount(Jose,josepedrero@gmail.com,tweets,followers,timeline,retweets)
mensajes = ()
cuenta1.Tweetear(Jose,mensaje,Useraccount)


cuenta2.Retweet(mensajes,Nacho)


#para modificar los atributos de tweet y timeline, para que tengas especificaciones de la clase Retweet podemos
# añadir un contador por cada persona que retwiteé o modificar los retwiits para que aparezcan como twits normales
#solo que haciendo referencia al alias de la persona que lo publico originalmente.

#¿Deberá modificar el método def tweet(Tweet tweet1) de la clase UserAccount
#(definida en el ejercicio 1) para que pueda enviar también objetos de tipo
#Retweet? Justifique su razonamiento y, si cree que hay que modificarlo, explique
#también cómo lo haría.
#no haria falta, podemos usar la opcion de publicar el tweet( si hubiera estado bien creada) y añadir un tweet de otra
#persona, mediante una referencia al alias y al numero del tweet
