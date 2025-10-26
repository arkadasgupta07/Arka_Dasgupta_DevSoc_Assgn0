import os
import json
from google import genai
from google.genai import types
# Imports the types module, which provides data structures for API interactions

# --- Configuration ---
# Stored my API key as an environment variable (GEMINI_API_KEY)
# The client will automatically pick it up.
try:
    client = genai.Client()
except Exception as e:
    print(f"Error initializing Gemini client. Make sure the GEMINI_API_KEY environment variable is set.")
    print(f"Details: {e}")
    exit(1)

# Set the model to use
MODEL_NAME = 'gemini-2.5-flash'
INPUT_FILENAME = 'text.txt'
OUTPUT_FILENAME = 'llm_responses_output.json' # the file where the API responses will be saved in JSON format.


# --- Core Functions ---

# Defines a function to read the input queries, expecting a file path (str) and returning a list of strings (list[str]).
def read_queries_from_file(file_path: str) -> list[str]:
    """Reads lines from a text file, treating each line as a separate query."""
    print(f"-> Reading queries from {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # It opens the file to read every line, remove leading/trailing whitespace (.strip()), and filter out completely empty lines.
            queries = [line.strip() for line in f if line.strip()]
        print(f"   Successfully read {len(queries)} queries.") # Reports the total number of valid queries found.
        return queries
    except FileNotFoundError:
        print(f"ERROR: Input file not found at '{file_path}'. Please create it.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

# Defines a function to call the LLM API (here GEMINI API), taking a list of queries and returning a list of structured dictionaries (results).
def get_llm_responses(queries: list[str]) -> list[dict]:
    """Calls the LLM API for each query and formats the response data."""
    if not queries:
        return []

    print(f"-> Sending {len(queries)} requests to the LLM ({MODEL_NAME})...")
    
    response_data = []
    
    for i, query in enumerate(queries):
        print(f"   Processing Query {i+1}/{len(queries)}: '{query[:50]}...'")
        try:
            # Makes the API call by using the initialized client and the specified MODEL_NAME and query.
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=query
            )

            # Structure the result for JSON
            result = {
                "id": i + 1,
                "input_query": query,
                "llm_response": response.text,
                "model_used": MODEL_NAME,
                "status": "success"
            }
            response_data.append(result)

        # Catches an error during the API call (e.g., network error, invalid API key, quota exceeded), prints a warning, and logs a structured failure dictionary into the response_data list.
        except Exception as e:
            print(f"   WARNING: Failed to get response for Query {i+1}. Error: {e}")
            # Log the failure
            response_data.append({
                "id": i + 1,
                "input_query": query,
                "llm_response": None,
                "model_used": MODEL_NAME,
                "status": f"failed: {str(e)}"
            })
            
    print("-> All API calls completed.")
    return response_data

# Defines a function to save the data to a JSON file.
def save_to_json_file(data: list[dict], file_path: str):
    """Saves the list of dictionaries to a JSON file."""
    print(f"-> Saving results to {file_path}...")
    try:
        # It opens the output file in write mode ('w') and uses json.dump to write the data.
        # indent=4 makes the JSON file human-readable.
        with open(file_path, 'w', encoding='utf-8') as f:
            # Use json.dump for clean, human-readable formatting
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"   Successfully saved {len(data)} records to {file_path}.")
    except Exception as e:
        print(f"ERROR: Could not save data to JSON file. Details: {e}")


# --- Main Execution ---

if __name__ == "__main__":
    print("\n--- LLM Processor Script Started ---")
    
    # 1. Read input from the text file
    queries = read_queries_from_file(INPUT_FILENAME)
    # Calls the function to read all queries from the text.txt file.
    
    if queries:
        # 2. Checks if any queries were read. If so, it calls the LLM for responses.
        results = get_llm_responses(queries)
        
        # 3. Save the received responses in a JSON file
        if results:
            # If responses were received (even failed ones), it calls the function to save the final results to the JSON file.
            save_to_json_file(results, OUTPUT_FILENAME)
        
    print("--- LLM Processor Script Finished ---\n")