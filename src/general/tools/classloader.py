import os
import re
import sys

class classloader():
    def getAllCategories(self):
        files = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser("../../")) for f in fn if re.match(r'[a-zA-Z0-9]+.*DataObject.py$', f)]
        d=set()
        for f in files:
            if not 'general' in f.split(os.path.sep):
                for item in f.split(os.path.sep):
                    if not '..' in item:
                        d.add(item.replace('DataObject.py', ''))
                        break
        return d


    def importAllPythonFiles(self):
        files = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser("../../")) for f in fn if re.match(r'[a-zA-Z0-9./]+.*.py$', f)]
        for pyfile in files:
            if "general" not in pyfile.split(os.path.sep):
                sys.path.append(os.path.dirname(os.path.realpath(pyfile)))
                for item in reversed(pyfile.split(os.path.sep)):
                    try:
                        mod = __import__(item.replace('.py',''))
                    except Exception as e:
                        print(str(e))
                        print("Module " + item + " couldn't be imported")
                    break
            

#    def loadClass(self, relativePathToClass):
 #       sys.path.append(os.path.dirname(os.path.realpath(relativePathToClass)))
  #      cls=''
   #     for item in reversed(relativePathToClass.split(os.path.sep)):
    #        mod = __import__(item.replace('.py',''))
     #       cls = getattr(mod, item.replace('.py', ''))
      #      return cls


#c = classloader()

#categories=c.getAllCategories()
#print(categories)

#d=c.getAllServices('calendar')
#print(d)
#e=c.loadClass(d['teamupCalendar'])
#print(type(e()))

#serviceClass=c.loadClass(d['teamupCalendar'].replace('DataObject', 'ApiInterface'))
#print(type(serviceClass()))
