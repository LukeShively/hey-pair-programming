# hey-pair-programming
AI pair programming assistant powered by EvaDB. <b>This application is intended for Windows devices</b>, and uses EvaDB. If you want to see the application this is inspired by, or do not have a Windows device but wish to have a pair programming assistant, please visit this website: https://github.com/lnxpy/hey

# Requirements
Must have Python >=3.8 downloaded.

Since this application uses ChatGPT, please assign the environment variable OPENAI_KEY to your OpenAI key string. (OpenAI account is required)

# Setup
Please install the required libraries with these commands in the command line if you haven't done so already:

pip install evadb

pip install eva-decord

pip install openai

Next, please download hey.py and save it in your desired location. You can more easily reference local files if hey.py is in your project directory. Then, run the following line in the command terminal:

doskey hey=python (path to hey.py) $*

where (path to hey.py) is the absolute path to hey.py on your computer, including hey.py.

# Usage

To use Hey, simply write "hey" in the command line, followed by your request. Hey is designed to be a pair programming assistant, so you can ask it about your project files as well! Simply ask your question about the file, making sure to include the file path in your question relative to hey.py. For example, if hey.py and file.py are in the same directory, one could type "hey annotate file.py" if they wanted Hey to annotate their file.

If you relocate hey.py to another project directory, make sure to update the file path by running the following line in the command terminal:

doskey hey=python (new path to hey.py) $*
