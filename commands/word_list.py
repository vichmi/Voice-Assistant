import mysql.connector as mc
from dotenv import load_dotenv
import os
import sys
sys.path.append('../')
from Assistant.db import db
from deep_translator import GoogleTranslator


def translate_word(word):
    return GoogleTranslator(source='en', target='bg').translate(word)

def add_word(*w):
    term = ' '.join(w)
    translated_word = translate_word(term)
    cursor = db.cursor()
    sql = "INSERT INTO words(term, definition) VALUES (%s, %s)"
    cursor.execute(sql, [term, translated_word])
    db.commit()

def get_words(order_by = None):
    cursor = db.cursor()
    query = 'SELECT * FROM WORDS'
    if order_by is not None:
        query += ' order by'
        check_ordering = ' '.join(order_by.split(' ')[2:])
        if check_ordering in ('words', 'words ascending', 'word ascending', 'alphabetically'): query += ' word asc'
        elif check_ordering in ('words descending', 'word descending'): query += ' word desc'
        elif check_ordering in ('id', 'id ascending'): query += ' id asc'
        elif check_ordering in ('id descending'): query += ' id desc'
    # print(query)
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)
