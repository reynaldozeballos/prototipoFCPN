from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
# Cargar los datos
dw = pd.read_csv("d:/archivos/lista.csv")
textos = ' '.join(dw.textos)
wc = WordCloud(width=1024, height=800, colormap='Blues', min_font_size=14).generate(textos)
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wc)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()