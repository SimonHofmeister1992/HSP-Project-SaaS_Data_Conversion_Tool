import hashlib
class idTable:

    prefetchedIdSet=set()

    def appendPrefetchedIdSet(self, uniqueIdToken):
        m=hashlib.sha256()
        message=uniqueIdToken.encode('utf-8')
        m.update(message)
        if not m.hexdigest() in self.prefetchedIdSet:
            self.prefetchedIdSet.add(m.hexdigest())
        return

    def containsId(self, uniqueIdToken):
        m=hashlib.sha256()
        message=uniqueIdToken.encode('utf-8')
        m.update(message)
        if m.hexdigest() in self.prefetchedIdSet:
            return True
        else:
            return False
