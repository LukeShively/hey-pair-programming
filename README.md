# hey-pair-programming
AI pair programming assistant powered by EvaDB. <b>This application is intended for Windows devices</b>, and uses EvaDB. If you want to see the application this is inspired by, or do not have a Windows device but wish to have a pair programming assistant, please visit this website: https://github.com/lnxpy/hey

# Requirements
Must have Python >=3.9 downloaded.

Since this application uses ChatGPT, please assign the environment variable OPENAI_KEY to your OpenAI key string (<b>OpenAI account is required</b>).

# Setup

Since this app uses EvaDB, please make sure to install it. The guide can be found here: https://evadb.readthedocs.io/en/stable/source/overview/getting-started.html

Please install the required libraries with these commands in the command terminal if you haven't done so already:

pip install evadb

pip install eva-decord

pip install openai

Next, please download hey.py and save it in your desired location, preferably somewhere safe. Then, run the following line in the command terminal:

doskey hey=python (path to hey.py) $*

where (path to hey.py) is the absolute path to hey.py on your computer, including hey.py.

# Usage

To use Hey, simply write "hey" in the command line, followed by your request. Hey is designed to be a pair programming assistant, so you can ask it about your project files as well! Simply ask your question about the file, making sure to include the file path in your question relative to your location in the command terminal. For example, if you are in directory A and want to ask Hey to annotate file.py in directory B, you could either type "hey annotate .../B/file.py" from A, or you could cd to B then type "hey annotate file.py".

This application uses EvaDB in order to query ChatGPT, and it stores previously made requests so that repeated requests can be more efficiently retrieved. If you wish to clear Hey's memory, you can type "hey clear".

If you close and reopen your command terminal, please run this line of code again:
doskey hey=python (path to hey.py) $*

Alternatively, you can call hey.py directly for your questions or requests like so:

py (path to hey.py) (question/request)
