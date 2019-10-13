from osgeo import gdal
import numpy

# import modules
from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32
import numpy as np

filename = 'Navarredonda_Urban.tif'
g = gdal.Open(filename, GA_ReadOnly)
if g is None:
    raise IOError, "Couldn't open Navarredonda_Urban.tif"
b3 = g.GetRasterBand(8).ReadAsArray().astype(np.float32)
b4 = g.GetRasterBand(4).ReadAsArray().astype(np.float32)
 
ndvi = (b4 - b3)/(b4 + b3)
 
drv = gdal.GetDriverByName ( "GTiff" )
dst_ds = drv.Create ( "output_file.tif", g.RasterXSize, g.RasterYSize, 1, gdal.GDT_Float32, options=["COMPRESS=LZW"] )
dst_ds.GetRasterBand(1).WriteArray ( dst_ds.astype (np.float32) )
dst_ds = None
