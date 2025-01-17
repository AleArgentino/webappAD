#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import base64
import numpy as np

st.title("Gráficos Phyton+Streamlit")
st.header("Tabela Inicial:")

#DB
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vToXjLeT4rFKXxS3g8xu-EYwfOZU-9HBNuH9UqudfBtx2LX-pOCYzKlZkFwYAO4AJInYPtlXmAyMqA0/pub?gid=1281694547&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)
dfD.columns = ['Idade', 'Opinião', 'Resumo']
st.dataframe(dfD) 
# eliminar as colunas com valores ausentes
summary = dfD.dropna(subset=['Resumo'], axis=0)['Resumo']
# concatenar as palavras
all_summary = " ".join(s for s in summary)
# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["de", "ao", "o", "nao", "para", "da", "meu", "em", "você", "ter", "um", "ou", "os", "ser", "só"])
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=1280, height=720).generate(all_summary)

#def add_bg_from_local(image_file):
    #with open(image_file, "rb") as image_file:
        #encoded_string = base64.b64encode(image_file.read())
    #st.markdown(
    #f"""
    #<style>
    #.stApp {{
        #background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        #background-size: cover
    #}}
    #</style>
    #""",
    #unsafe_allow_html=True
    #)
#add_bg_from_local('FabLabBackground.PNG')  

#col1, col2, col3 = st.columns((1, 1, 1))
#with col1:
    #st.image('LOGO - FabLLab.JPG', width=150, output_format='auto')
#with col2: 
    #st.write(" ") 
#with col3: 
    #st.subheader("Como está sendo a sua experiência no FabLab?")
    #SUB_TITULO1 = '<p style="font-family:tahoma; color:black; font-size: 28px;">Como está sendo a sua experiência no FabLab?</p>'
    #st.markdown(SUB_TITULO1, unsafe_allow_html=True)

st.header("Gráfico de Pizza:")
fig, ax = st.plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

labels = 'Críticas', 'Sugestões', 'Elogios'
data = [nCritica, nSugestao, nElogio]
explode = (0, 0.1, 0)  # only "explode" the 1st slice

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} respostas)"

wedges, texts, autotexts = ax.pie(data, explode = explode, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, labels,
          title="Opiniões",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

st.plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Percentual de Opiniões")

plt.show()

st.header("Nuvem de palavras:")
# mostrar a imagem final
#fig, ax = plt.subplots(figsize=(10,6))
#ax.imshow(wordcloud, interpolation='bilinear')
#ax.set_axis_off()
plt.imshow(wordcloud);
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
#st.pyplot()
wordcloud.to_file("NuvemPalavras.png")

st.pyplot() #Este método faz exibir a nuvem de palavras
st.set_option('deprecation.showPyplotGlobalUse', False)

st.info(" Desenvolvido em Linguagem Python | Programador: Alexandre M. Argentino e Nicholas C. Tonhi")

SUB_TITULO = '<p style="font-family:tahoma; color:white; font-size: 14px;">CC BY-NC-SA - Esta licença permite que outros alterem, adaptem e criem a partir desta publicação para fins não comerciais, desde que atribuam aos criadores o devido crédito e que licenciem as novas criações sob termos idênticos.</p>'
st.markdown(SUB_TITULO, unsafe_allow_html=True)

