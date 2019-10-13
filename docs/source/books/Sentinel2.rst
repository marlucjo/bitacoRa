Sentinel 2
----------

.. image:: https://landsat.gsfc.nasa.gov/wp-content/uploads/2015/06/Landsat.v.Sentinel-2.png
  :width: 400
  :alt: Alternative text

.. image::https://idecyl.jcyl.es/geoserver/ps/wms?service=WMS&version=1.1.0&request=GetMap&layers=ps%3Aznie_cyl_montes_up&bbox=163530.578125%2C4440891.0%2C603087.375%2C4790762.5&width=768&height=611&srs=EPSG%3A25830&format=image%2Fpng
  :width: 400
  :alt: MUP


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

