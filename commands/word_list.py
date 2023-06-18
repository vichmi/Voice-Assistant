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

def get_words(*order_by):
    cursor = db.cursor()
    query = 'SELECT * FROM WORDS'
    order_by = ' '.join(order_by)
    if order_by is not None:
        query += ' order by'
        check_ordering = ' '.join(order_by.split(' ')[2:])
        if check_ordering in ('terms', 'terms ascending', 'term ascending', 'alphabetically'): query += ' term asc'
        elif check_ordering in ('terms descending', 'term descending'): query += ' term desc'
        elif check_ordering in ('id', 'id ascending'): query += ' id asc'
        elif check_ordering in ('id descending'): query += ' id desc'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def search_word(word):
    cursor = db.cursor()
    query = f'SELECT * FROM WORDS WHERE term = "{word}";'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)