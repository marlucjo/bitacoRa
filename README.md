# bitacoRa

Bitácora  de prueba ....

# Specifying an R environment with a runtime.txt file

Jupyter+R: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/marlucjo/bitacoRa/r/HEAD?filepath=index.ipynb)

RStudio: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?urlpath=rstudio)

RShiny: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?urlpath=shiny/bus-dashboard/)

https://mybinder.org/v2/gh/binder-examples/r/HEAD?filepath=index.ipynb
https://mybinder.org/v2/gh/marlucjo/bitacoRa/HEAD


**GML**, acrónimo inglés de Geography Markup Language (Lenguaje de Marcado Geográfico), es un lenguaje basado en XML (eXtensible Markup Language) escrito en un esquema XML para el modelado, transporte y almacenamiento de información geográfica.

**Cross-Domain** es un mecanismo de seguridad de las comunicaciones en navegadores actuales. Evitan que un script (XMLHttpRequest de AJAX) o una aplicación (Flash, Silverlight) de una página web pueda acceder a un servidor web diferente del que residen. En otras palabras, no es posible solicitar desde un cliente un fichero XML o GML a un servidor distinto del que se descargó la aplicación web.

**JSON** (JavaScript Object Notation) está diseñado para ser manipulado con el lenguaje JavaScript (que implementan la 
mayoría de los clientes web) como mecanismo que permite sortear el Cross-Domain.

**GeoJSON** es un formato de intercambio de datos geoespaciales basado en JSON. Soporta los siguientes tipos de geometría: *Point*, *LineString*, *Polygon*, *MultiPoint*, *MultiLineString*, *MultiPolygon* y *GeometryCollection*.

> [Ejemplo .GeoJSON](./carto/mup60.geojson)

**TopoJSON** es una extensión de GeoJSON que codifica topología. TopoJSON introduce un nuevo tipo, *"Topology"*, que contiene objetos GeoJSON. 

> [Ejemplo .TopoJOSON](/carto/mup60.topojson)

### Referencias

[Mapping geoJSON files on GitHub](https://help.github.com/articles/mapping-geojson-files-on-github)

[Working with non code files](https://help.github.com/categories/working-with-non-code-files/)
