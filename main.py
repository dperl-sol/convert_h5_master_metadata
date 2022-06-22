#!/usr/bin/env python

import h5py
import argparse

def import_schema(input_h5):
    '''Take an .h5 file (from Eiger data) and convert the metadata structure to a dict'''

def export_schema(schema, output_json):
    '''Output a metadata schema (as python dict) as a json file'''

def translate(input_schema, output_schema, schema_mapping, metadata):
    '''Convert metadata from input_schema structure to output_schema structure using schema_mapping'''

def run(input_h5, input_schema, output_schema, schema_mapping):
    '''Take an .h5 master file (from Eiger data) and export a copy with the metadata in an output schema'''