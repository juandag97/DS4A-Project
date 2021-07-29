Scripts running different tasks and DS4A_Project folder structure
-DS4A_Project:
    -Code:
        -Basura:
            Files not used any more
        -ExportData:
            Files to use in EDA or further along milestones including Autocorrelation plots, heatmaps, csv files 
            Month_Mean all data organized by month and location
            Year_Mean all data organized by year and location
        Autocorrelation.py python script that generates autocorrelation plots and saves them to ExportData directory
        DataJoin.py python script that using glob "joins" all available csv datasets in the Raw_Data directory
        EDA_MeterCOL.py saves figure of all 9 plottable variables for an input year for all stations in ExportData
        HeatMap_VariableGenerator.py Generates LocationMonthAverage.csv and LocationYearAverage.csv
        LonLat_ML_variables.py Generates AllVariables_HeatData.csv in ExportData/HeatData to use in Map_data.py
        Map_data.py Generates follium map and heatmap layer with file AllVariables_HeatData.csv
        Modelos_AERO.py python script analogous to MATLAB script provided by David Rosero
        README.md this file
    -Processed_Data:
        HistoLoadUnited.csv Cols: Time Stamp,Time Zone,Name,PTID,Load,Time
        LocationMonthAverage.csv Cols: Month,Longitude,Latitude,Longitude-Latitude, + ClimateVars average per month per location
        LocationYearAverage.csv Cols:Year,Longitude,Latitude,Longitude-Latitude + ClimateVars average per year per location
        MeteorCOLUnited.csv Cols: All variables - complete data all locations in Colombia all measurements
        MeteorUnited.csv Cols: All variables - complete data since 2005 including Costa Rica locations
        ResidencesUnited.csv Cols: Time Bucket (America/New_York),JFP_1 (kWhs),JFP_2 (kWhs),room outlets (kWhs),Heater  (kWhs),Hall Light (kWhs),Oven (kWhs),Family Light (kWhs),Fridge (kWhs),Washer/Dryer (kWhs),Fam Outlets (kWhs)
    -Raw_Data: Data provided by DDSSAS 
