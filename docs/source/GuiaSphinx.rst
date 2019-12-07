.. contents::
   :local:

Guia Sphinx  
===========

**Sphinx** es un software generador de documentación que convierte ficheros reStructuredText en sitios web HTML y otros formatos, incluyendo PDF, EPub

El lenguaje en el que normalmente se escribe la documentación para Sphinx es **reStructuredText**, un lenguaje de marcado potente pero menos popular que Markdown y con una curva de aprendizaje más pronunciada.

El servicio **Read the Docs** provee alojamiento de documentación hecha con Sphinx de forma gratuita, y será el que usaremos puesto que se puede navegar entre versiones.

El archivo clave es *index.rst*, que es el índice de nuestra documentación. El contenido que coloquemos ahí será el que se vea en la página principal. Lo normal es poner una introducción y un índice. Por defecto, index.rst incluye un par de encabezados, un índice vacío, un glosario y otros.

Para añadir secciones al índice, simplemente hay que crear nuevos archivos '.rst' y listarlos. 


La documentación se escribe en archivos ``.rst``, que están ubicados en una
carpeta llamada ``source``. A partir de estos archivos, que se escriben en
`reStructuredText`_, se genera la página web. En esos mismos archivos ``.rst``
uno especifica qué *docstrings* extraer desde el código fuente (Python). Más
adelante hay ejemplos y creo que se entiende mejor.

.. _estructura:

Los archivos y carpetas pueden organizarse de varias formas, la forma
`recomendada`__ de organizar el proyecto es::

  .
  ├── docs
  │   ├── build
  │   │   ├── ...
  │   │   └── html
  │   │       ├── ...
  │   │       └── index.html
  │   ├── Makefile
  │   └── source
  │       ├── ...
  │       ├── conf.py
  │       └── index.rst
  ├── LICENSE.txt
  ├── README.md
  └── miproyecto
      ├── ...
      └── main.py

__ http://docs.python-guide.org/en/latest/writing/structure/

En ``docs`` va todo lo relacionado con la documentación, dentro hay un
``Makefile`` y las carpetas ``source`` y ``build``.

``source`` tiene la documentación escrita en `reStructuredText`_ y un archivo
``conf.py`` con las configuraciones usadas por `Sphinx`_.  Dentro de ``build``
está la misma documentación en *html* ya generada por `Sphinx`_. Por último el
``Makefile`` permite generar la documentación (que se pone en ``build``) con un
comando.

Después en otra carpeta aparte, ``miproyecto`` está el código. ``LICENSE.txt`` y
``README.md`` se suelen agregar para presentar el proyecto en por ejemplo
`GitHub`_.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _GitHub: https://github.com/





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
- https://www.ibm.com/developerworks/ssa/opensource/library/os-sphinx-documentation/index.html
- https://pythonhosted.org/an_example_pypi_project/sphinx.html

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

Función 
"""""""

.. function:: format_exception(etype, value, tb[, limit=None])

   Format the exception with a traceback.

   :param etype: exception type
   :param value: exception value
   :param tb: traceback object
   :param limit: maximum number of stack frames to show
   :type limit: integer or None
   :rtype: list of strings

