from math import *
import numpy as np

def to_Cartesian(lat, lng):
    '''
    function to convert latitude and longitude to 3D cartesian coordinates
    '''
    R = 6371 # radius of the Earth in kilometers

    x = R * cos(lat) * cos(lng)
    y = R * cos(lat) * sin(lng)
    z = R * sin(lat)
    return x, y, z

def deg2rad(degree):
    '''
    function to convert degree to radian
    '''
    rad = degree * 2*np.pi / 360
    return(rad)

def rad2deg(rad):
    '''
    function to convert radian to degree
    '''
    degree = rad/2/np.pi * 360
    return(degree)

def distToKM(x):
    '''
    function to convert cartesian distance to real distance in km
    '''
    R = 6371 # earth radius
    gamma = 2*np.arcsin(deg2rad(x/(2*R))) # compute the angle of the isosceles triangle
    dist = 2*R*sin(gamma/2) # compute the side of the triangle
    return(dist)

def kmToDIST(x):
    '''
    function to convert real distance in km to cartesian distance 
    '''
    R = 6371 # earth radius
    gamma = 2*np.arcsin(x/2./R) 
    
    dist = 2*R*rad2deg(sin(gamma / 2.))
    return(dist)

def geo_to_cartesian(lats,lons):
    return zip(*map(to_Cartesian, lats, lons))
