get_ipython().system("!pip install Flask")
get_ipython().system("!pip install folium")

import pandas as pd
corona_df = pd.read_csv('basededatos.csv')
por_pais = corona_df.groupby('País').sum()[['Confirmado', 'Muertes', 'Recuperado', 'Activos']]
cdf = por_pais.nlargest(n, 'Confirmado')[['Confirmado']]

def encontrar_confirmados(n = 15):
  import pandas as pd
  corona_df = pd.read_csv('basededatos.csv')
  por_pais = corona_df.groupby('País').sum()[['Confirmado', 'Muertes', 'Recuperado', 'Activos']]
  cdf = by_country.nlargest(n, 'Confirmado')[['Confirmado']]
  return cdf

import folium
import pandas as pd
corona_df = pd.read_csv('basededatos.csv')
corona_df=corona_df.dropna()
m=folium.Map(location=[34.223334,-82.461707],
            tiles='Stamen toner',
            zoom_start=8)
def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2])*10,
                 color="red",
                 popup='{}\n confirmed cases:{}'.format(x[3],x[2])).add_to(m)
corona_df[['Lat','Long_','Confirmed','Combined_Key']].apply(lambda x:circle_maker(x),axis=1)
html_map=m._repr_html_()

from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html",table=cdf, cmap=html_map,pairs=pairs)
if __name__=="__main__":
    app.run(debug=True)
