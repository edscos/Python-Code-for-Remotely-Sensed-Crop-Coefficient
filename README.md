# Python-Code-for-Remotely-Sensed-Crop-Coefficient-Modeling for Actual Daily Evapotranspiration

Support material based on Python coding to estimate actual daily maize evapotranspiration (ETa) using reflectance-based crop coefficient models.

# REFERENCES:

Bausch, W. C. (1995). Remote sensing of crop coefficients for improving the irrigation scheduling of corn. Agricultural Water Management, 27(1), 55-68.

Chávez, J. L., Gowda, P. H., Howell, T. A., Neale, C. M. U., & Copeland, K. S. (2009). Estimating hourly crop ET using a two-source energy balance model and multispectral airborne imagery. Irrigation Science, 28(1), 79-91.

Huete, A. R. (1988). A soil-adjusted vegetation index (SAVI). Remote sensing of environment, 25(3), 295-309.

Johnson, L. F., & Trout, T. J. (2012). Satellite NDVI assisted monitoring of vegetable crop evapotranspiration in California’s San Joaquin Valley. Remote Sensing, 4(2), 439-455.

Neale, C. M., Bausch, W. C., & Heermann, D. F. (1990). Development of reflectance-based crop coefficients for corn. Transactions of the ASAE, 32(6), 1891-1900.

Trout, T. J., Johnson, L. F., & Gartung, J. (2008). Remote sensing of canopy cover in horticultural crops. HortScience, 43(2), 333-337.

# CODE DESCRIPTION:

The Python script labeled "ETa_Kcr_RFL_Code.py" performs the calculation of daily maize ETa using three different linear models for maize basal crop coefficient (Kcr) based on different remote sensing vegetation indices as input. The Kcr models are the following:

      Neale et al. (1990) - Normalized Difference Vegetation Index (NDVI) as predictor
      Bausch (1995) - Soil Adjusted Vegetation Index (SAVI) as predictor
      Trout and DeJonge (2018) - Fractional Vegetation Cover (fc) as predictor

The SAVI index calculation is based on Huete (1988) and considered a fixed soil background adjustment factor equals to 0.50.

There is an spreadsheet labeled "Input_Data_v2.xlsx" that provides the input variables needed to calculate daily maize ETa. The inputs in the spreadsheet are the folllowing ones:

      Date, Time, and Alfalfa-based reference ET (mm/d)

The Alfalfa-based reference ET has to be calculated or obtained before running the Python script. Agricultural weather station data often provide reference ET values for a given location. Users might find the ETo calculator from the Food and Agriculture Organization (FAO) useful to calculate daily values of reference ET using agricultural weather station data (see https://www.fao.org/land-water/databases-and-software/eto-calculator/en/).

The other input data are the red (RED_RFL) and near-infrared (NIR_RFL) surface reflectance imagery from a given remote sensing platform (e.g., satellite, or unmanned aerial vehicle). The RED_RFL and NIR_RFL surface reflectance imagery has to be individual .tif files.

The code is designed to provide the following maps:

      Leaf area index (LAI), NDVI, SAVI, fc, ETa_ NDVI (mm/d), ETa_SAVI (mm/d), and ETa_fc (mm/d).
      
# NOTE: Make sure to add the file directory in which the RED_RFL and NIR_RFL imagery is stored.


      
      
      
      
      

