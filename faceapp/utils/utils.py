import time

class Utils:

    def getSystemTimeInMiliseconds():
        timestamp = int(time.time()*1000.0)
        return timestamp

    def getSystemTimeInMilisecondsString():
        timestamp = int(time.time()*1000.0)
        return str(timestamp)

    def handle_uploaded_file(f, name):
        with open(name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def removeWhiteSpace(name):
        return name.strip()
