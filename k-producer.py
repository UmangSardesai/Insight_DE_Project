import random
import sys
import time
import json
from datetime import datetime
from kafka.client import KafkaClient
from kafka.producer import KafkaProducer
import threading

def run_producer():
    while True:
        prod=KafkaProducer(bootstrap_servers=["52.34.235.156:9092","54.68.129.82:9092","52.36.60.60:9092"])
        random_number = random.randint(0, 190)
        random_number2 = random.randint(0, 4)
        rm3 = random.randint(0, 9)
        my_list = ['REFUND', 'GIFT CARD', 'PAYMENT', 'DEALS', 'ORDER']

        word_list = ["An", "ordered", "collection", "(also", "known", "as", "a", "sequence).", "The", "user", "of", "this", "interface", "has", "precise", "control", "over", "where", "in", "the", "list", "each", "element", "is", "inserted.", "The", "user", "can", "access", "elements", "by", "their", "integer", "index", "(position", "in", "the", "list),", "and", "search", "for", "elements", "in", "the", "list.", "Unlike", "sets,", "lists", "typically", "allow", "duplicate", "elements.", "More", "formally,", "lists", "typically", "allow", "pairs", "of", "elements", "e1", "and", "e2", "such", "that", "e1.equalse2,", "and", "they", "typically", "allow", "multiple", "null", "elements", "if", "they", "allow", "null", "elements", "at", "all.", "It", "is", "not", "inconceivable", "that", "someone", "might", "wish", "to", "implement", "a", "list", "that", "prohibits", "duplicates,", "by", "throwing", "runtime", "exceptions", "when", "the", "user", "attempts", "to", "insert", "them,", "but", "we", "expect", "this", "usage", "to", "be", "rare", "The", "List", "interface", "places", "additional", "stipulations,", "beyond", "those", "specified", "in", "the", "Collection", "interface,", "on", "the", "contracts", "of", "the", "iterator,", "add,", "remove,", "equals,", "and", "hashCode", "methods.", "Declarations", "for", "other", "inherited", "methods", "are", "also", "included", "here", "for", "convenience", "The", "List", "interface", "provides", "four", "methods", "for", "positional", "(indexed)", "access", "to", "list", "elements.", "Lists", "(like", "Java", "arrays)", "are", "zero", "based.", "Note", "that", "these", "operations", "may", "execute", "in", "time", "proportional", "to", "the", "index", "value", "for", "some", "implementations", "(the", "LinkedList", "class,", "for", "example).", "Thus,", "iterating", "over"]
        final_string=""
        for i in range (10):
            random_number = random.randint(1, 190)
            if i == rm3:
                #final_string=final_string + my_list[random_number2] + " "
                final_string=final_string + "REFUND" + " "
            else:
                final_string=final_string + word_list[random_number] + " "

        ts = time.time()
        my_json_string = json.dumps({'message': final_string, 'timestamp': ts})
        prod.send('fff2', my_json_string)
        #print my_json_string
        #time.sleep(1)

if __name__ == "__main__":
    for x in range (int(sys.argv[1])):
        t= threading.Thread(target=run_producer, name="Thread-"+str(x+1))
        t.start()