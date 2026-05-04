# Varroa-Infestation-Prediction

## Repository Description

## Getting your Own Copy
The simplest way to use this tool is to download the repository as a ZIP file, and host it locally on your own machine.

Downloading this repository as a ZIP file can be accomplished by clicking on the green 'Code' button at the top right of the repository's main page, and selecting 'Download ZIP'

More advanced users may also clone the repository via git for local use, but should be aware that pushes to the repository are not allowed without admin permission.
 - Note: Cloning the repository is NOT necessary to ensure the latest functionalities are being used locally

## Repository Components
### /configs
A folder with 2 JSON files in it:
 - pipeline_config.json: Inputs to the model-creation segment of the pipeline
 - prediction_confg.json: Inputs to the prediction segment of the pipeline

These files can be opened with a standard text editor for changing input parameters: Be mindful that the parameters are the values to the right of the ':' on each line, before the comma. When adjusting parameters, be sure to keep the comma and ':' in place, and to match the format of the data inplace by default (elaborated in a later section).

### /data
A folder containing 6 .csv files: These files are included as demonstration, and are the files used as reference when the model was originally developed.

Data from a user's own operation should be placed in this folder and specified in the appropriate config files (explained below) to be used for model creation and/or making predictions. Appropriate formatting is as follows:
 - Weather Data: Timeseries CSV with fields ["station_id","date","hour","air_temp","dew_point","pressure","wind_dir","wind_spd"]
    - station_id: Weather station identifier, can be from a weather service, or proprietary labeling: Must be an integer value
    - date: XXXX-XX-XX string, encoding Year-Month-Day
    - hour: XX:XX:XX string, encoding Hour:Minute:Second
    - All Others (Weather Measuring Fields): Floating point numbers (ie. decimals allowed), using -9999.0 to represent a missing 
 - Varroa Sampling Data: CSV with [sampling_id","date_from","date_to","varroa_count","yard_id"]
