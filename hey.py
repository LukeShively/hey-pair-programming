import evadb
import string
import os
import pandas
import io
import sys
import contextlib
import warnings
from contextlib import contextmanager

def evadb_format(unformatted):
    formatted = unformatted
    formatted = formatted.replace("\\n", "\n")
    formatted = formatted.replace("\"", "@QUOTE@")
    formatted = formatted.replace(";", "@SEMICOLON@")
    return formatted

cursor = evadb.connect().cursor()

# Download ChatGPT UDF if needed
#import wget
#!wget -nc https://raw.githubusercontent.com/georgia-tech-db/eva/master/evadb/udfs/chatgpt.py -O chatgpt.py


open_ai_key = os.environ.get('OPENAI_KEY')


pandas.set_option('display.max_colwidth', None)

# Create Hey table
hey_query = """
    CREATE TABLE IF NOT EXISTS Hey (request TEXT(3000), answer TEXT(3000));
"""
cursor.query(hey_query).df()

hey_request = """"""
file_list = []

sys.argv[0] = ""
for s in sys.argv:
    s = str(s)
    hey_request += s + " "
    if "." in s and s[len(s) - 1] != "." and s.isalpha():
        s = s.strip(",.?!\'\"()-")
        file_list.append(s)

for file in file_list:
    try:
        f = open(file, "r")
    except:
        continue
    file_text = f.read().strip()
    file_text = evadb_format(file_text)
    
    hey_request += " The file " + file + " is: " + file_text
    print(f.read())

#########################################################################

if hey_request.lower().strip() == "clear":
    
    clear_query = """
            DROP TABLE IF EXISTS Hey;
    """
    cursor.query(clear_query).df()
    exit()

hey_test = f"""
    SELECT request FROM Hey
    WHERE request = "{hey_request}";
"""

answer = ""

requested_query = cursor.query(hey_test).df()
if requested_query.empty:
    chatgpt_udf = f"""
        SELECT ChatGPT("{hey_request}");
    """
    query = cursor.query(chatgpt_udf).df()
    answer = query.iloc[:,0].to_string()[1:].strip()
    answer = evadb_format(answer)

    hey_insertion = f"""
        INSERT INTO Hey (request, answer) VALUES
        ("{hey_request}", "{answer}");
    """
    cursor.query(hey_insertion).df()
else:
    hey_retrieval = f"""
        SELECT answer FROM Hey
        WHERE request = "{hey_request}";
    """
    query = cursor.query(hey_retrieval).df()
    answer = query.iloc[:,0].to_string()[1:].strip().replace("\\n", "\n")

answer = answer.replace("@QUOTE@", "\"")
answer = answer.replace("@SEMICOLON@", ";")

print("\n" + answer)
