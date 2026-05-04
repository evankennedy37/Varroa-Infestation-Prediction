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

### /pipeline
Contains the three Juypter notebooks that form the three phases of the pipeline:
 - Data Processor: Processes the specified data files into combined Tensors
 - Model Fitter: Fits a predictive model onto the data
 - Predictor: Makes a true/false prediction of infestation, accompanied by a probability of infestation, for a given data range

Additionally includes a folder labeled 'outputs' with an empty 'dummy.txt' file in it: The folder is important to have in place, the file inside can be removed if desired.

Generally speaking, users should not interact directly with any of this folder's contents

Note: While these notebooks can be run in sequence to simulate the pipeline, it is not the intended approach, and can fail or produce uninteded behavior if the local environment does not match the requirements laid out in Requirements.txt, & is running Python 3.11.9

### pipeline.yml
A Docker Compose file used to run the pipeline through all of its phases, producing a predictive model and predictions, based on the configuratons specified in the /configs files

Running Options:
 - On Windows: Double-click the pipeline.bat file
 - Non-Windows: Navigate to the project directory in a Terminal/Command-Line Interface, then run 'docker compose -f pipeline.yml build --no-cache && docker compose -f pipeline.yml up --remove-orphans'
      - Note: Easiest way to naivgate to project directory is with 'cd {full project directory path}', copying the directory path in appropriately

### predict.yml
A Docker Compose file used to run the predictor, ONLY works after the pipeline.yml file has already been run at least once to produce the model the predictor is specified to use (by the /configs files)

Running Options:
 - On Windows: Double-click the predictor.bat file
 - Non-Windows: Navigate to the project directory in a Terminal/Command-Line Interface, then run 'docker compose -f predict.yml build --no-cache && docker compose -f predict.yml up --remove-orphans'
      - Note: Easiest way to naivgate to project directory is with 'cd {full project directory path}', copying the directory path in appropriately

### pipeline.bat & predict.bat
Windows shortcuts to run the Docker Compose files the project is built on (use explained above)

### /utilities
A folder with a supporting file included in it, should not be interacted with by user

### .gitattributes & .gitignore
Files included for the GitHub integration of the project, not to be interacted with by the user

### Dockerfile
A file used in the running of the pipeline and the predictor, not interacted with directly by the user

### Requirements.txt
A text file encoding the installation requirements for running the pipeline, not neccesary to be interacted with by the user

Note: Can be used as reference if wishing to run the notebooks individually within a Virtual Environment, though this approach is not the recommended one.

## Using this Repository
To use the main utilities of the project repositories, pipeline.yml & predict.yml, two prerequisite steps are required:
 - Docker Desktop must be open in the background: Necessary to enable the Docker daemon that the Docker Compose files use
     - If Help Needed: https://www.docker.com/products/docker-desktop/
 - ClearML API Credentials must be configured for the system: These are used for logging model performance in the ClearML Web UI
     - If Help Needed: https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/

Once these prerequisties are satisfied, pipeline.yml & predict.yml can be run using methods described above, for the following results:
(All the following based on configurations specified in /configs files, as explained above)
 - pipeline.yml: 
    - Tensors Datafile in pipeline/outputs [Not for user interaction]
    - Model file in pipeline/outputs [Not for user interaction]
    - A Prediction in the 'predictions' folder (the folder will appear if it was absent)
  - predictions.yml: (If ran properly, only after pipeline.yml has already created a model)
    - A Prediction in the 'predictions' folder (the folder will appear if it was absent)
  
