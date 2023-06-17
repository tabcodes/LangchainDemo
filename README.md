## Langchain Demo

A demo application written as an intro into the Python framework. Utilizes some prompt templates, a sequential chain, and OpenAI to gather some info on a given MMA fighter and display some interesting historical factoids
close to their birthdate.

### Components

- Langchain / OpenAI
- Streamlit
- Py-Dotenv

### Usage

- Installing requirements: `pip install -r requirements.txt`.
- Configuration: Rename the included `.env.example` file and fill in the config entry
  with your OpenAI API key.
- Starting the application: `streamlit run main.py --server.headless true`