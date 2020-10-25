#!/usr/bin/env python
# -*- coding: utf-8 -*-

import textract

def get_text(file_path):
    try:
        return textract.process(file_path)
    except:
        return 'Failed to get full text'

def add_mappings(mappings):
    """Returns a dict with additional es mappings"""
    mappings['mappings']['file']['properties'].update({
        'fulltext': {
            'type': "keyword"
        }
    })
    return mappings

def add_meta(file_path):
    """Returns a dict with additional file meta data"""
    text = get_text(file_path)
    meta = {"fulltext": text}
    return meta