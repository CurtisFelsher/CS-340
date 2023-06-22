#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 04:34:15 2023

@author: curtisfelsher_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30648
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Connection Successful")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, query):
        # Checks if input query is present
        if query is not None:
            # Executes the method on the collection and searches the database for matching documents
            return self.database.animals.find(query)
        else:
            # If the query returns nothing, raise an exception
            raise Exception("Query returned empty")
            
# Create method to implement the U in CRUD
    def update(self, query, new_values):
        # Checks if input query and new_values is present
        if query is not None and new_values is not None:
            # Executes update_many operation on the animals collection
            result = self.database.animals.update_many(query, new_values)
            return result.modified_count
        else:
            # If nothing is returned, raise an exception
            raise Exception("Update operation failed. Empty query or new_values.")
            
# Create method to implement the D in CRUD
    def delete(self, query):
        # Checks if input query is present
        if query is not None:
            # Execute delete_many operation on the animals collection
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        else:
            # If nothing is returned, raise an exception
            raise Exception("Delete operation field. Empty query.")