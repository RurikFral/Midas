class Logger():
    logPath = "log.txt"
    def log(self, message):
        f = open(self.logPath, "a")
        f.write(message+"/n")
        f.close()
        return