# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 23:29:33 2023

@author: andre
"""

     
def convert_coordinates(coordinate_list):
    decimal_coordinates = []
    
    for coordinate_str in coordinate_list:
        parts = re.findall(r"(\d+)° (\d+)' ([\d.]+)\"([NSWE])", coordinate_str)
        degrees = int(parts[0][0])
        minutes = int(parts[0][1])
        seconds = float(parts[0][2])
        direction = parts[0][3]
        
        decimal_coordinate = degrees + minutes/60 + seconds/3600
        if direction in ['S', 'W']:
            decimal_coordinate = -decimal_coordinate
        
        decimal_coordinates.append(decimal_coordinate)
    
    return decimal_coordinates

# Example usage #EJEMPLO : "8° 54' 21.127\"S",
coordinate_inputs = ["2° 29' 15.24\"S",	"73° 40' 45.29\"W"]

decimal_coordinates = convert_coordinates(coordinate_inputs)

print("coordenada decima de la estacion [lat, lon]:", decimal_coordinates)













