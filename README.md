# bitacoRa

**GML**, acrónimo inglés de Geography Markup Language (Lenguaje de Marcado Geográfico), es un lenguaje basado en XML (eXtensible Markup Language) escrito en un esquema XML para el modelado, transporte y almacenamiento de información geográfica.

**Cross-Domain** es un mecanismo de seguridad de las comunicaciones en navegadores actuales. Evitan que un script (XMLHttpRequest de AJAX) o una aplicación (Flash, Silverlight) de una página web pueda acceder a un servidor web diferente del que residen. En otras palabras, no es posible solicitar desde un cliente un fichero XML o GML a un servidor distinto del que se descargó la aplicación web.

**JSON** (JavaScript Object Notation) está diseñado para ser manipulado con el lenguaje JavaScript (que implementan la 
mayoría de los clientes web) como mecanismo que permite sortear el Cross-Domain.

**GeoJSON** es un formato de intercambio de datos geoespaciales basado en JSON. Soporta los siguientes tipos de geometría: *Point*, *LineString*, *Polygon*, *MultiPoint*, *MultiLineString*, *MultiPolygon* y *GeometryCollection*.

> [Ejemplo .GeoJSON](./carto/mup60.geojson)

**TopoJSON** es una extensión de GeoJSON que codifica topología. TopoJSON introduce un nuevo tipo, *"Topology"*, que contiene objetos GeoJSON. 

> [Ejemplo .TopoJOSON](/carto/mup60.topojson)

### Referencias

- [Mapping geoJSON files on GitHub](https://help.github.com/articles/mapping-geojson-files-on-github)

- [Working with non code files](https://help.github.com/categories/working-with-non-code-files/)

- [Binder](https://www.r-bloggers.com/2019/06/r-binder-interactive-jupyter-notebooks-in-the-cloud/)

- [Binder ejemplos](https://github.com/binder-examples/r)

- [Binder ejemplos más completo](https://github.com/AuthorCarpentry/carpentry-R-ecology-report)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marlucjo/bitacoRa/HEAD)


### Want to play with these notebooks online without having to install anything?

* <a href="https://colab.research.google.com/github/marlucjo/bitacoRa/blob/main/" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> (recommended)

⚠ _Colab provides a temporary environment: anything you do will be deleted after a while, so make sure you download any data you care about._

<details>

Other services may work as well, but I have not fully tested them:

* <a href="https://homl.info/kaggle3/"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open in Kaggle" /></a>

* <a href="https://mybinder.org/v2/gh/ageron/handson-ml3/HEAD?filepath=%2Findex.ipynb"><img src="https://mybinder.org/badge_logo.svg" alt="Launch binder" /></a>

* <a href="https://homl.info/deepnote3/"><img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg" alt="Launch in Deepnote" /></a>

* Jupyter+R: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/marlucjo/bitacoRa/master?filepath=index.ipynb)
  
* Jupyter+R_ej: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/marlucjo/bitacoRa/master?filepath=R/index.ipynb)
  
* RStudio: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/marlucjo/bitacoRa/master?urlpath=rstudio)

* RShiny: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/marlucjo/bitacoRa/master?urlpath=shiny/bus-dashboard/)
  
*JupyterLite: [![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)]
(https://jupyterlite.rtfd.io/en/latest/try/lab)
  
Binder supports using R and RStudio, with libraries pinned to a specific
snapshot on [packagemanager.rstudio.com](https://packagemanager.rstudio.com/client/#/).
</details>




