#!/bin/python

import os
import pprint

print "Test Local Python script environment variables:\n";

env_var = os.environ
pprint.pprint(dict(env_var),width=1)

