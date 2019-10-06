¿Qué es?
========

**GML**, acrónimo inglés de Geography Markup Language (Lenguaje de Marcado Geográfico), es un lenguaje basado en XML (eXtensible Markup Language) escrito en un esquema XML para el modelado, transporte y almacenamiento de información geográfica.

**Cross-Domain** es un mecanismo de seguridad de las comunicaciones en navegadores actuales. Evitan que un script (XMLHttpRequest de AJAX) o una aplicación (Flash, Silverlight) de una página web pueda acceder a un servidor web diferente del que residen. En otras palabras, no es posible solicitar desde un cliente un fichero XML o GML a un servidor distinto del que se descargó la aplicación web.

**JSON** (JavaScript Object Notation) está diseñado para ser manipulado con el lenguaje JavaScript (que implementan la mayoría de los clientes web) como mecanismo que permite sortear el Cross-Domain.

**GeoJSON** es un formato de intercambio de datos geoespaciales basado en JSON. Soporta los siguientes tipos de geometría: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon y GeometryCollection.

https://www.ericholscher.com/blog/2016/jul/1/sphinx-and-rtd-for-writers/

https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax

example:

.. code-block:: python
   :linenos:

   import antigravity

   def main():
       antigravity.fly()

.. warning:: This is a Warning!


.. toctree::
    :maxdepth: 2
    :numbered:
    :titlesonly:
    :glob:
    :hidden:

    intro.rst
    a.rst
    Sentinel2.ipynb
    
