## Langchain Demo
A demo application written as an intro into the Python Langchain framework. Utilizes some prompt templates, a sequential chain, and OpenAI to gather some info on a given UFC fighter and display some interesting historical factoids that occurred
close to their birthdate. Made while watching [Krish Naik's excellent intro to Langchain applications](https://www.youtube.com/watch?v=_FpT1cwcSLg).

<img src="https://github.com/tabcodes/LangchainDemo/assets/7765337/8d6369fc-7299-4fa3-8740-3eb576fbcdd3" width="40%" height="40%" />

### Components

- Langchain / OpenAI
- Streamlit
- Py-Dotenv

### Usage

- Installing requirements: `pip install -r requirements.txt`.
- Configuration: Rename the included `.env.example` file and fill in the config entry
  with your OpenAI API key.
- Starting the application: `streamlit run main.py --server.headless true`
