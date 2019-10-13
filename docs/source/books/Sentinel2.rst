Sentinel 2
----------

+------------------+-------------------------+--------------------------+
| Bandas           | Resolución Espacial (m) | Resolución Espectral (nm)|
+==================+=========================+==========================+
|Banda 1 (Aerosol) | 60                      |                      443 |
+------------------+-------------------------+--------------------------+
|Banda 2 (Azul)    | 10                      |                      490 |
+------------------+-------------------------+--------------------------+
|Banda 3 (Verde)   | 10                      |                       560|
+------------------+-------------------------+--------------------------+
|Banda 4 (Rojo)    | 10                      |                       665| 
+------------------+-------------------------+--------------------------+
|Banda 5           |                         |                          |
|(Infrarrojo       | 20                      |                       705|
|cercano -NIR)     |                         |                          |
+------------------+-------------------------+--------------------------+


|Banda 6 (NIR)| 20| 740|
|Banda 7 (NIR)| 20| 783|
|Banda 8 (NIR)| 10| 842|
|Banda 8a (Infrarrojo cercano - NIR)| 20| 865|
|Banda 9 (Vapor de Agua)| 60| 9945|
|Banda 10 (Cirrus)| 60| 1375|
|Banda 11 (Infrarrojo Lejano - SWIR)| 20| 1610|
|Banda 12 ( SWIR)| 20| 2190|


.. note:: Bandas Sentinel2.
   
Insertamos parte del código de un fichero:

.. literalinclude:: ndvi.py
   :language: python
   :linenos:
   :lines: 1-5

.. literalinclude:: ndvi.r
   :language: R
   :linenos:
   :lines: 1-3

.. literalinclude:: ../Notebooks/Sentinel2.ipynb
   :language: python
   :linenos:
   :lines: 1-3

