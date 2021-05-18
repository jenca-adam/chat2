#!/usr/bin/python
import pickle,os
pickle.dump([],open('prispevky.pickle','wb'))
pickle.dump({},open('prezyvky.pickle','wb'))
pickle.dump([],open('povoleny.pickle','wb'))
os.remove("prisp.db")
