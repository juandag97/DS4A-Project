# DS4A-Project
## Group 57 DS4A Colombia Project Cohort-5

## Welcome to the code repository! The whole set of analysis scripts and forecasting models can be found here.

The world is slowly but firmly attacking the use of non renewable energy sources such as gas, coal and gasoline. Now, in order to achieve the goal of being completely renewable-dependant by 2050, alternative energy sources must be made accesible and efficient. This doesnt just apply to the large energy producers of the world or the giant firms that move the world, it applies to everyone, the everyday users, every household and every school. 

Inside the directory named simply "Code" we can find several python scripts and ipython notebooks which enabled us to perform the intended energy production forecasts. 

The requirements.txt lists the python modules used throughout the project and may be installed in linux using
~~~
    pip install -r requirements.tx
~~~
on a system that has working pip and a current installation of Python3.

## Trash and additional code
Before the actual guide to exploring the code we should first discard some of the code that was used in the process but in the developement of the project ended up in the trash. Ths code can be found in the directory structure:
~~~
    Code -> Basura:
                EDA_MeterCOL.py
                EDA_timeSeries.py
                HearMap_VariableGenerator.py
                LonLat_ML_variables.py
                Map_data.py
                Modelos_AERO.py
                Modelos_solar_MyImp.py
                Modelos_SOLAR.py
                NN_solarforecaster.ipynb
~~~
Most of this code was part of the "this doesnt work" phase in the project, where we tried different approaches and cadence in analysing the data provided. This code must not be used but is included in case the user wants to explore the capabailities of different approaches. As a warning, most of this code IS NOT completed or in a completely working state.

On the other hand, the files found in the folder
~~~
    Code -> ExportData
~~~
has figures and maps usefull to examine the data and understanding the available information.



## Data
Now, to the point of the project and getting usefull data used in the final application.

The first script that must be used is
~~~
    Code:
        DataJoin.py
~~~

In this script all the tables provided by Dynamic Defense solutions SAS are "joined" (further on, reffered as the company or the client).

The main output file of this script is MeteorCOLUnited.csv where all the meteorologic data is joined to a table including information on the file, location and time of observation. The folder paths must be updated inside the file in order to give python the desired tables. In this script all files inside "Datos_Meteorologicos" corresponding to meteorological observations per location are merged.

## EDA
A file that was really usefull for us in the EDA phase was 
~~~
    Code:
        Autocorrelation.py
~~~
Where the autocorelation is computed and we found an obvious correlation between the time series and itself when lagged 12 months. This is how we decided on the models explained below. Inside the script the user must chose a location by inputing a number between 0 and 22 and the user must also chose which variable to analyze by inputing a number between 0 and 9.

The files
~~~
    Code:
        Consumption_averages.ipynb
        DESCRIPTIVE_STATS_METERCOL.py
        EDA_timeSeries.py
        HEATMAP_nulls_METERCOL.py
~~~
Are the files which we used to generate the figures of the final report but are not directly involved in the forecasting models pipeline.

## Models

Two main models where generated to forecast variables to different time windows. 

### ARIMA

Based on the autocorrelation plots, we made an ARIMA approach to forecasting where we forecasted the two main variables with a monthly cadence for the next 2 years (namely 2021 and 2022). This model uses as base the output file MeteorCOLUnited.csv.

The python3 notebook
~~~
    Code:
        ARIMA.ipynb
~~~
Was the first approach were we can find figures relating prediction power and parameters importance. 

Meanwhile,The python3 script
~~~
    Code:
        ARIMA.py
~~~
generates the GHI and WindSpeed time series for the next two years for every location in one output file named "ARIMAEnergy_24months.csv".  This output file is the one used to generate the figures in the final application. In the database, this table is named forecasted_24months.

### Horizontal linear regression

The second model, Horizontal linear regression, relies completely on the yearly seasonality in the data. a linear regression is generated using the same date in every year before 2020 to fit the same date on 2020. then (like a rolling window) this linnear regression is applied to the years before 2021, excluding the first year, to forecast the value on the date in 2021. For example, to generate the 21st of November at 9:00 am values in 2021, we fit a linear regression model with the available data for the 21st of November at 9:00 am and then apply that linnear regression moving each parameter forward one year. 

The forecasted data is generated with the notebook
~~~
    Code:
        HorizonData_forecast.ipynb
~~~

The output files from this model are the ones that can be seen in the final app when "Regresion lineal horizontal" option is selected. Namely, GHI_gen_preds.csv and WIN_gen_preds.csv.

### Neural networks

In the directory

~~~
    Code -> forecating
~~~

we can finda high cadence (hourly), high accuracy model to forecast the desired variables up to a 7 day horizon. we did not include this model in the final app as it would require high maintenance in the data which is not ideal. But, if the user wants to find accurately the behaviour of meteorologic data in the next days he may use the code here which is based on included data from the IDEAM institute in Colombia.

## Generation strategy

Finally, an important mention is the generation startegy. 

The company provided us with MATLAB models for solar and wind energy generation with output figures that relate wind speed and output power. We took the maximum posible generation values for both energy sources and fitted a simple XY linnear regression among this values. In this way, for every forecasted value of GHI and Wind Speed we could find the maximum posible generation. The data (taken from MATLAB) can be found in the directory

~~~
    Code -> ExportData
            GHI_generation.csv
            WindSpeed.csv
~~~

# Recommendations!

In team 57 we hope you have a great experience with the data and predictive power of both models to find the best alternative for your energy grid! On the other hand, we by no means insure the values presented here will be the real generation you will achieve but rather you may find a general idea of what you could achieve. All the models are assuming perfect power generation and weather conditions, something that in reality does not happen.

Thank you for reading and enjoy!

