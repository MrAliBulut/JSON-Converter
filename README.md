# JSON Converter

This code is designed to perform the following tasks:
*Created with the assistance of ChatGPT.*

1. **Retrieve JSON Data from an API**
   - The function `getJsonFromAPI(apiUrl)` takes a URL (`apiUrl`) as input and attempts to retrieve JSON data from it. If successful, it returns the JSON data.

2. **Process Input JSON File and Export as Excel**
   - The function `processFile(filePath)` takes a file path (`filePath`) of a JSON file as input. It reads the JSON data from the file, converts it into a pandas DataFrame, and exports it as an Excel file named "Entries.xlsx" located in the "JSON_Converter/Output/" directory.

3. **Detect Unique Entries and Export as Excel**
   - The function `detectUniqueEntries(JSON)` takes a JSON object as input. It identifies unique entries based on the "status" field having the value "in". It then converts these unique entries into a pandas DataFrame and exports them as an Excel file named "uniqueEntries.xlsx" located in the "JSON_Converter/Output/" directory.

4. **Output JSON Data to a File**
   - The function `outputAsFile(uniqueEntries, filePath)` takes a JSON object (`uniqueEntries`) and a file path (`filePath`) as input. It writes the JSON data to the specified file.

---

## How to Use

1. **API Data Retrieval (Optional)**
   - If you want to retrieve data from an API, call the `getJsonFromAPI(apiUrl)` function, providing the API URL as the `apiUrl` parameter. This function will return the JSON data if successful.

2. **Processing an Input JSON File**
   - If you have a JSON file you want to process, call the `processFile(filePath)` function, passing the file path as the `filePath` parameter. This function will read the JSON data, convert it to an Excel file, and return the original JSON data.

3. **Detecting and Exporting Unique Entries**
   - If you want to find unique entries with "status" set to "in", call the `detectUniqueEntries(JSON)` function, passing the JSON data as the `JSON` parameter. This function will create an Excel file of unique entries and return a list of those unique entries.

4. **Output JSON Data to a File**
   - If you want to save the JSON data to a file, call the `outputAsFile(uniqueEntries, filePath)` function, providing the list of unique entries and the desired file path as parameters.

---

*Please make sure to have the required modules (`pandas`, `json`, `requests`) installed in your Python environment before running the code.*

DEV Note: Also make sure that path variables to input files are correct.
