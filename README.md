# Varroa-Infestation-Prediction

## Repository Description

## Getting your Own Copy
The simplest way to use this tool is to download the repository as a ZIP file, and host it locally on your own machine.

Downloading this repository as a ZIP file can be accomplished by clicking on the green 'Code' button at the top right of the repository's main page, and selecting 'Download ZIP'

More advanced users may also clone the repository via git for local use, but should be aware that pushes to the repository are not allowed without admin permission.
 - Note: Cloning the repository is NOT necessary to ensure the latest functionalities are being used locally

## Repository Components
### /data
A folder containing 6 .csv files: These files are included as demonstration, and are the files used as reference when the model was originally developed.

Data from a user's own operation should be placed in this folder and specified in the appropriate config files (explained below) to be used for model creation and/or making predictions. Appropriate formatting is as follows:
 - Weather Data: Timeseries CSV with fields ["station_id","date","hour","air_temp","dew_point","pressure","wind_dir","wind_spd"]
    - station_id: Weather station identifier, can be from a weather service, or proprietary labeling: Must be an integer value
    - date: XXXX-XX-XX string, encoding Year-Month-Day
    - hour: XX:XX:XX string, encoding Hour:Minute:Second
    - All Other Fields (ie. Weather Measuring Fields): Floating point numbers (ie. decimals allowed), using -9999.0 to represent a missing
    - For Reference, see: weather.csv
 - Varroa Sampling Data: CSV with ["sampling_id","date_from","date_to","varroa_count","yard_id"]
    - sampling_id: Unique identifier for a sampling count of varroa mites: Must be an integer value
    - date_from: Date when the drop board was freshly set, prior to the sampling: XXXX-XX-XX string, encoding Year-Month-Day
    - date_to: Date when the mites were counted: XXXX-XX-XX string, encoding Year-Month-Day
    - varroa_count: Manual count of Varroa Mites on the board: Must be an integer value
    - yard_id: A unique integer identifier for a particular yard/apiary
    - For Reference, see: varroa_sampling.csv
 - Yard Data: CSV with ["yard_id", "elevation", "station_id"]
    - yard_id: A unique integer identifier for a particular yard/apiary: Should match up with those used in the selected Varroa Sampling Data
    - elevation: Floating point value (ie. decimals allowed), denoting the elevation of the particular yard/apiary
    - station_id: Closest weather station identifier: Should match up with those used in the selected Weather Data
    - For Reference, see: yard.csv

IMPORTANT: User-included data files should be given names without spaces (ie. replace spaces with an _)

Note: The easiest way to turn records into CSV files is often to use Excel's 'Export as CSV' option to convert an Excel notebook into a CSV file

### /configs
A folder with 2 JSON files in it, used for inputs to phases of the pipeline:
 - pipeline_config.json: Inputs to the model-creation segment of the pipeline
     - model_name: What you would like the model produced to be called, useful primarily if creating multiple models from different data
         - FORMATTING REQIUREMENT: In quotes (ie. "name"), Ends in .json file extension
     - varroa_samplings_file_path: Path to the desired varroa sampling data, from the base directory of the project
         - FORMATTING REQIUREMENT: In quotes (ie. "name")
     - yard_information_file_path: Path to the desired yard information data, from the base directory of the project
         - FORMATTING REQIUREMENT: In quotes (ie. "name")
     - weather_data_file_path: Path to the desired weather data, from the base directory of the project
         - FORMATTING REQIUREMENT: In quotes (ie. "name")
 - prediction_confg.json: Inputs to the prediction segment of the pipeline
     - predictor_model_name: What model you would like to use to make a prediction, matches with created model name by default
         - FORMATTING REQIUREMENT: In quotes (ie. "name"), Ends in .json file extension
     - weather_data_file_path: Path to the desired weather data (definite or forecast), from the base directory of the project
         - FORMATTING REQIUREMENT: In quotes (ie. "name")
     - weather_station_id: The identifier for the weather station closest to the yard/apiary having a prediction made for it
         - FORMATTING REQIUREMENT: In quotes (ie. "name")
     - yard_density: An integer value for the number of hives in the yard/apiary having a prediction made for it
         - FORMATTING REQIUREMENT: Integer value
     - yard_elevation: An floating point value (ie. decimals allowed) for the elevation of the yard/apiary having a prediction made for it
         - FORMATTING REQIUREMENT: Floating point value
     - prediction_period_start_date: XXXX-XX-XX string, encoding Year-Month-Day, for the start of the date range to make predictions for
         - FORMATTING REQIUREMENT: In quotes (ie. "XXXX-XX-XX"), XXXX-XX-XX string, encoding Year-Month-Day
     - prediction_period_end_date: XXXX-XX-XX string, encoding Year-Month-Day, for the end of the date range to make predictions for
         - FORMATTING REQIUREMENT: In quotes (ie. "XXXX-XX-XX"), XXXX-XX-XX string, encoding Year-Month-Day

These files can be opened with a standard text editor for changing input parameters: Be mindful that the parameters are the values to the right of the ':' on each line, before the comma. When adjusting parameters, be sure to keep the comma and ':' in place, and to match the format of the data inplace by default (specified above).
