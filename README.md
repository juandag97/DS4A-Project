# DS4A-Project
Group 57 DS4A Colombia Project Cohort-5

Welcome to the code repository! The whole set of analysis scripts and forecasting models can be found here.

The world is slowly but firmly attacking the use of non renewable energy sources such as gas, coal and gasoline. Now, in order to achieve the goal of being completely renewable-dependant by 2050, alternative energy sources must be made accesible and efficient. This doesnt just apply to the large energy producers of the world or the giant firms that move the world, it applies to everyone, the everyday users, every household and every school. 

Inside the directory named simply "Code" we can find several python scripts and ipython notebooks which enabled us to perform the intended energy production forecasts. 

The requirements.txt lists the python modules used throughout the project and may be installed in linux using
~~~
    pip install -r requirements.tx
~~~
on a system that has working pip and a current installation of Python3.

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

Now, to the point of the project and getting usefull data used in the final application.

The first script that must be used is
~~~
    Code:
        DataJoin.py
~~~

In this script all the tables provided by Dynamic Defense solutions SAS are "joined" (further on, reffered as the company or the client).

The main output file of this script is MeteorCOLUnited.csv where all the meteorologic data is joined to a table including information on the file, location and time of observation. 


