#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def removeNull(path):
    r = os.system(f"sed -i -e 's/null/0/g' {path}")
    return r