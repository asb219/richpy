import requests
import pandas as pd

__all__ = ['get_data']


def get_data(latitude=None, longitude=None, elevation=None, sampling_year=None):
    """
    Parameters
    ----------
    latitude : tuple(float,float), optional
        2-tuple of min and max limits of latitude range (degrees North)
    longitude : tuple(float,float), optional
        2-tuple of min and max limits of longitude range (degrees East)
    elevation : tuple(float,float), optional
        2-tuple of lower and upper limits of site elevation (m a.s.l.)
    sampling_year : tuple(int,int), optional
        2-tuple of lower and upper limits of sampling year range
    
    Returns
    -------
    data : pandas.DataFrame
    
    Examples
    --------
    # Get data for samples from sites at elevations above 1400 m a.s.l.
    # and longitudes between 7° and 8.5° East (inclusive).
    data = get_data(elevation=(1400,None), longitude=(7,8.5))
    
    # Get data for samples collected between 2010 and 2015 (inclusive).
    data = get_data(sampling_year=(2010,2015))
    """

    def add_range_param(params, name, x):
        if x is not None:
            x0, x1 = x
            if x0 is not None:
                params.append((name, f'gte.{x0}'))
            if x1 is not None:
                params.append((name, f'lte.{x1}'))

    url = 'https://api.rich.ethz.ch/samples'
    params = []

    add_range_param(params, 'latitude', latitude)
    add_range_param(params, 'longitude', longitude)
    add_range_param(params, 'site_elevation', elevation)
    add_range_param(params, 'sampling_years', sampling_year)

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = pd.DataFrame(response.json())

    return data
