# Python Code to run the Kcb ET algorithm from remote sensing data
# Author: Edson Costa-Filho, M.Sc.
# Date: 4/1/2022

# References:

# Bausch, W. C. (1995). Remote sensing of crop coefficients
# for improving the irrigation scheduling of corn.
# Agricultural Water Management, 27(1), 55-68.

# Chávez, J. L., Gowda, P. H., Howell, T. A., Neale, C. M. U., & Copeland, K. S. (2009).
# Estimating hourly crop ET using a two-source energy balance model
# and multispectral airborne imagery. Irrigation Science, 28(1), 79-91.

# Huete, A. R. (1988). A soil-adjusted vegetation index (SAVI).
# Remote sensing of environment, 25(3), 295-309.

# Johnson, L. F., & Trout, T. J. (2012).
# Satellite NDVI assisted monitoring of vegetable
# crop evapotranspiration in California’s San Joaquin Valley.
# Remote Sensing, 4(2), 439-455.

# Neale, C. M., Bausch, W. C., & Heermann, D. F. (1990).
# Development of reflectance-based crop coefficients for corn.
# Transactions of the ASAE, 32(6), 1891-1900.

# Trout, T. J., Johnson, L. F., & Gartung, J. (2008).
# Remote sensing of canopy cover in horticultural crops.
# HortScience, 43(2), 333-337.

# Defining Constant Variables Regarding the Date of the Image

L = 0.50  # Constant for Calculating SAVI (i.e., low vegetation: L = 1;...
# intermediate vegetation: L = 0.50;...
#...high vegetation: L = 0.25)

from math import *
# packages for data analysis
import pandas as pd
import numpy as np

# packages for visualizing data
import imageio
from PIL import Image
import matplotlib.pyplot as plt

# Importing ancillary data from excel (local weather and reference ET data)

data_excel = pd.read_excel(r'C:\Users\edson\OneDrive - Colostate\Desktop\Input_Data_v2.xlsx')
all_columns = list(data_excel.columns)
print(all_columns)
Date = data_excel['Date']   # Date of the Data (MM/DD/YYYY)
Time = data_excel['Time']   # Time of the Data (HH:MM:SS)
DOY = data_excel['DOY']     # Day of the Year (DOY)
ETrd = data_excel['ETrd']   # Daily Alfalfa-based Reference ET (mm/d)

# Importing remote sensing imagery data (TIFF file)
# NOTE: Add the directory of the imagery as filename for the RED and NIR surface reflectance bands
filename_RED = r'file_directory\RED_surface_reflectance_filename.tif'
filename_NIR = r'file_directory\NIR_surface_reflectance_filename.tif'

# Reading the remote sensing imagery data and converting to array data format
RED_img = Image.open(filename_RED)
NIR_img = Image.open(filename_NIR)
RED_RFL = np.array(RED_img)
NIR_RFL = np.array(NIR_img)
size = range(len(RED_RFL))
img_shape = RED_RFL.shape

# Obtaining the number of rows and columns of the remote sensing imagery data
sz = np.array(img_shape)

# Assigning initial values for each variable to be calculated in the code
NDVI = 0
SAVI = 0
OSAVI = 0
fc_trout = 0
LAI = 0
Kcb_trout = 0
Kcb_bausch = 0
Kcb_neale = 0
ETa_trout = 0
ETa_bausch = 0
ETa_neale = 0

# for loop to calculate remote sensing indices, actual ETa from each reflectance-based crop coefficient model

for row in size:

    for column in size:

        # Calculation of NDVI
            NDVI = (NIR_RFL - RED_RFL)/(NIR_RFL + RED_RFL)

        # Calculation of SAVI (Huete, 1988)
            SAVI = (NIR_RFL - RED_RFL) / (NIR_RFL + RED_RFL + L)*(1+L)

        # Calculation of OSAVI (Rondeaux et al., 1996)
            OSAVI = (NIR_RFL - RED_RFL) / (NIR_RFL + RED_RFL + 0.16) * 1.16

        # Calculation of fractional vegetation cover (Trout and Jonhson, 2012)
            fc_trout = 1.26 * NDVI - 0.18

        # Calculation of leaf area index (Chávez et al., 2009)
            LAI = 0.263 * np.exp(3.813 * OSAVI)

        # Calculation of reflectance-based crop coefficient
            Kcb_trout = 1.10 * fc_trout + 0.17  # Trout and DeJonge (2018)
            Kcb_bausch = 1.416 * SAVI + 0.017   # Bausch (1995)
            Kcb_neale = 1.181 * NDVI - 0.026    # Neale et al. (1990)

        # Calculation of actual daily ETa from each reflectance-based crop coefficient method
            ETa_trout = Kcb_trout * ETrd[0]     # Trout and DeJonge (2018)
            ETa_bausch = Kcb_bausch * ETrd[0]   # Bausch (1995)
            ETa_neale = Kcb_neale * ETrd[0]     # Neale et al. (1990)

        # Exporting the results as .tif files
    imageio.imwrite('NDVI.tiff',NDVI)                   # NDVI map
    imageio.imwrite('LAI.tiff',LAI)                     # Chávez et al. (2009) LAI map
    imageio.imwrite('ETa_Kcb_fc.tiff',ETa_trout)        # Trout and DeJonge (2018) ETa map
    imageio.imwrite('ETa_Kcb_SAVI.tiff',ETa_bausch)     # Bausch (1995) ETa map
    imageio.imwrite('ETa_Kcb_NDVI.tiff',ETa_neale)      # Neale et al. (1990) ETa map