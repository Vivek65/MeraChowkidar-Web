import pandas as pd
import shapefile as shp
from shapely.geometry import Point
from shapely.geometry import shape as shapely

shp_path = "AC_data/India_AC.shp"
sf = shp.Reader(shp_path)


def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords' column holding
    the geometry information. This uses the pyshp package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]

    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)

    return df


df = read_shapefile(sf)


def return_location_data(long=None, lat=None):
    """
    Reads the shapefile and its Pandas dataframe
    Takes in long lat of a point and return the dataframe row in which it lies.
    """
    indexList = df.index.to_numpy()[0:]
    for ids in indexList:
        polygon = shapely(sf.shape(ids))
        point = Point(long, lat)
        if (polygon.contains(point)):
            return df.iloc[ids].to_json()


reqLoc = return_location_data(75, 26)