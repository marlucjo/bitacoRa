Guia Sphinx  
===========

**Sphinx** es una herramienta para crear documentación bonita, navegable y que da gusto usar. 

El lenguaje en el que normalmente se escribe la documentación para Sphinx es **reStructuredText**, un lenguaje de marcado potente pero menos popular que Markdown y con una curva de aprendizaje más pronunciada.

El servicio **Read the Docs** provee alojamiento de documentación hecha con Sphinx de forma gratuita, y será el que usaremos puesto que se puede navegar entre versiones.

El archivo clave es *index.rst*, que es el índice de nuestra documentación. El contenido que coloquemos ahí será el que se vea en la página principal. Lo normal es poner una introducción y un índice. Por defecto, index.rst incluye un par de encabezados, un índice vacío, un glosario y otros.

Para añadir secciones al índice, simplemente hay que crear nuevos archivos '.rst' y listarlos. 


.. index:: Título 1

Título 1
--------
**negrita**, *cursiva*,
``código``.


.. index:: Título 2
Título 2
~~~~~~~~
.. warning:: This is a Warning!

Título 3
^^^^^^^^
.. code-block:: python
   :linenos:

   import antigravity

   def main():
       antigravity.fly()

Título 4
""""""""

Here are a few notes about the different options

1. **maxdepth** is used to indicates the depth of the tree.
2. **numbered** adds relevant section numbers.
3. **titlesonly** adds only the main title of each document
4. **glob** can be used to indicate that * and ? characters are used to indicate patterns.
5. **hidden** hides the toctree. It can be used to include files that do not need to be shown (e.g. a bibliography).


Referencias
~~~~~~~~~~~
- https://www.ericholscher.com/blog/2016/jul/1/sphinx-and-rtd-for-writers/
- https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax
- https://restructuredtext.readthedocs.io/en/latest/sphinx_tutorial.html
- https://martinber.github.io/guia-sphinx/escribir.html
- https://automating-gis-processes.github.io/CSC/master/lessons/L1/Intro-Python-GIS.html
- https://martinber.github.io/guia-sphinx/escribir.html

.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle

    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

