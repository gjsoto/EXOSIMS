# -*- coding: utf-8 -*-
import numpy as np
from astropy import units as u

class ZodiacalLight(object):
    """Zodiacal Light class template
    
    This class contains all variables and methods necessary to perform
    Zodiacal Light Module calculations in exoplanet mission simulation.
    
    Args:
        \*\*specs:
            user specified values
    
    Attributes:
        exozodi (float):
            exozodi level in zodi
        exozodiVar (float):
            exozodi variation (variance of log-normal distribution)
        
    """

    _modtype = 'ZodiacalLight'
    
    def __init__(self, **specs):
                
        # default values
        self.exozodi = 1.5 # exo-zodi level in zodi
        self.exozodiVar = 0. # exo-zodi variation (variance of log-normal distribution)
        
        # replace default values with user specified values
        atts = self.__dict__.keys()
        for att in atts:
            if att in specs:
                setattr(self, att, specs[att])
                
        # initialize values updated by functions
        # set values derived from quantities above
                
    def __str__(self):
        """String representation of the Zodiacal Light object
        
        When the command 'print' is used on the Zodiacal Light object, this 
        method will return the values contained in the object"""

        atts = self.__dict__.keys()
        
        for att in atts:
            print '%s: %r' % (att, getattr(self, att))
        
        return 'Zodiacal Light class object attributes'
        
    def eclip_lats(self, coords):
        """Returns ecliptic latitudes 
        
        This method returns ecliptic latitudes for equatorial right ascension 
        and declination values in Star Catalog data (astropy.coordinates does 
        not yet support this conversion).
        
        Args:
            coords (SkyCoord):
                numpy ndarray of astropy SkyCoord objects with right ascension 
                and declination in degrees
                
        Returns:
            el (ndarray):
                ecliptic latitudes in degrees
        
        """
        
        eps = 23.439281 # obliquity of ecliptic in degrees
        a = np.cos(np.radians(eps))*np.sin(coords.dec)
        b = np.sin(coords.ra)*np.cos(coords.dec)*np.sin(np.radians(eps))
        el = np.degrees(np.abs(np.arcsin(a-b)))

        return el
        
    def fzodi(self, Inds, I, targlist):
        """Returns exozodi levels for systems 
        
        This method is called in __init__ of SimulatedUniverse.
        
        Args:
            Inds (ndarray):
                1D numpy array of indices referring back to target list stars
            I (ndarray):
                1D numpy ndarray or scalar value of inclination in degrees
            targlist (TargetList):
                TargetList class object
        
        Returns:
            fzodicurr (ndarray):
                1D numpy ndarray of exozodiacal light levels

        """
        
        fzodicurr = np.array([10.]*len(Inds))
        
        return fzodicurr