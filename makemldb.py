import sys, os
#sys.path.insert(0, '/lcrc/project/AWA-beam-dynamics/software/pyOPALTools/')
#sys.path.insert(0, '/lcrc/project/AWA-beam-dynamics/software/pyOPALTools/db/')
#sys.path.insert(0, '/lcrc/project/AWA-beam-dynamics/software/pyOPALTools/utilities/')
from db import mldb
''' 
We create a Pickle file from a number of OPAL 
simulations using the format from runOPAL.py

The content of the file is

 y = f (x)  

'''

#baseFN = 'rand_sample'
#root   = "/lcrc/project/AWA-beam-dynamics/surrogatemodels/random_sample/surrogate_models_rand_sample_bounds2"

baseFN = ['ex-1', 'ex-2', 'ex-3', 'ex-4']
#root   = "/lcrc/project/AWA-beam-dynamics/surrogatemodels/ga-model/results"
#root   = "./ex-4/results"

#baseFN = 'paper-pc'
#root   = "/lcrc/project/AWA-beam-dynamics/surrogatemodels/pc-models/paper-pc-model/data/"

#yNames = ['s','numParticles','rms_x','rms_y','rms_s','emit_x','emit_y','emit_s','energy','dE']
#dbw    = mldb.mldb()

#Build from stat files
#dbw.buildFromSDDS(baseFN, root, yNames)
#dbw.printOverview()

#Build from json files
#dbw.build(baseFN, root)
#dbw.printOverview()

#Make bounded db
for ex in baseFN:
    pickle = ex+'.pk'
    mldb.buildBounded(pickle, ex)

