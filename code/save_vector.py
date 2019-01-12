# _*_ coding: utf-8 _*_
__author__ = 'xbr'
__date__ = '2018/10/31 14:32'

import sys
from osgeo import ogr

ds = ogr.Open(r'D:\osgeopy-data\global', 1)
if ds is None:
    sys.exit('Could not open folder.')
in_lyr = ds.GetLayer('ne_50m_populated_places')
if ds.GetLayer('capital_cities'):
    ds.DeleteLayer('capital_cities')
out_lyr = ds.CreateLayer('capital_cities',
                     in_lyr.GetSpatialRef(),
                     ogr.wkbPoint)
out_lyr.CreateFields(in_lyr.schema)

out_defn = out_lyr.GetLayerDefn()
out_feat = ogr.Feature(out_defn)
for in_feat in in_lyr:
    if in_feat.GetField('FEATURECLA') == 'Admin-0 capital':
        geom = in_feat.geometry()
        out_feat.SetGeometry(geom)
        for i in range(in_feat.GetFieldCount()):
            value = in_feat.GetField(i)
            out_feat.SetField(i, value)
        out_lyr.CreateFeature(out_feat)
del ds
