import evadb
import string

import os
import pandas
cursor = evadb.connect().cursor()


# Download ChatGPT UDF if needed
#import wget
#!wget -nc https://raw.githubusercontent.com/georgia-tech-db/eva/master/evadb/udfs/chatgpt.py -O chatgpt.py


open_ai_key = os.environ.get('OPENAI_KEY')


pandas.set_option('display.max_colwidth', None)

# Drop Hey table if needed
cursor.query("DROP TABLE IF EXISTS Hey;").df()

# Then create Hey table
hey_query = """
    CREATE TABLE IF NOT EXISTS Hey (request TEXT(500), answer TEXT(3000));
"""
cursor.query(hey_query).df()

#########################################################################
# Input your request, set to "clear" to reset the table's state
# Once input, run the code and your answer will be the output below!
# A repeated input will use EvaDB's Hey table to reduce retrieval time

hey_request = """hey generate a function in javascript"""

#########################################################################

valid_request = False
if (hey_request.lower()[0:4] == "hey "):
  hey_request = hey_request[4:]
  valid_request = True
else:
  print("no hey? :(")
  if hey_request.lower() == "clear":
    clear_query = """
            DROP TABLE IF EXISTS Hey;
    """
    cursor.query(clear_query).df()
    hey_query = """
    CREATE TABLE IF NOT EXISTS Hey (request TEXT(500), answer TEXT(3000));
    """
    cursor.query(hey_query).df()


hey_test = f"""
    SELECT request FROM Hey
    WHERE request = "{hey_request}";
"""

answer = ""
if (valid_request):
  requested_query = cursor.query(hey_test).df()
  if requested_query.empty:
    chatgpt_udf = f"""
        SELECT ChatGPT("{hey_request}");
    """
    query = cursor.query(chatgpt_udf).df()
    answer = query.iloc[:,0].to_string()[1:].strip()
    answer = answer.replace("\\n", "\n")
    answer = answer.replace("\"", "@QUOTE@")
    answer = answer.replace(";", "@SEMICOLON@")

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

print(answer)
