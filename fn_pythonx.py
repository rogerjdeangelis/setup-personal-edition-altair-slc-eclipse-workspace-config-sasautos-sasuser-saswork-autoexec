import pandas as pd
import pyreadstat as ps
import json
import pyarrow.feather as feather;
import tempfile;
import pyperclip;
import os;
import sys;
import subprocess;
import time;
import numpy as np;
from pandasql import sqldf;
mysql = lambda q: sqldf(q, globals());
from pandasql import PandaSQL;
pdsql = PandaSQL(persist=True);
sqlite3conn = next(pdsql.conn.gen).connection.connection;
sqlite3conn.enable_load_extension(True);
sqlite3conn.load_extension('d:/dll/sqlean.dll');
mysql = lambda q: sqldf(q, globals());

