import configparser
from UI import *

class Settings:
    def __init__(self,fileName):
        self._fileName=fileName
    def start(self):
        with open(self._fileName,"r") as f:
            config_string="[SETTINGS]\n" + f.read()
        config = configparser.ConfigParser()
        config.read_string(config_string)
        for i in config["SETTINGS"]:
            config["SETTINGS"][i]=config["SETTINGS"][i].strip('"')

        repository=config["SETTINGS"]["repository"]

        ass=''
        st=''
        gr=''
        ud=UndoController()

        if repository=="inmemory":
            st = StudentRep(ud)
            ass=AssigmentRep(ud)
            gr=GradeRep(ud)
        elif repository=="text-file":
            st=RepoTextStudents(ud,config["SETTINGS"]["students"])
            ass=RepoTextAssigments(ud,config["SETTINGS"]["assignments"])
            gr=RepoTextGrade(ud,config["SETTINGS"]["grades"])
        elif repository=="binary-file":
            st=RepoBinStudents(ud,config["SETTINGS"]["students"])
            ass=RepoBinAssigments(ud,config["SETTINGS"]["assignments"])
            gr=RepoBinGrade(ud,config["SETTINGS"]["grades"])
        elif repository=="JSON-file":
            st = RepoJSONStudents(ud, config["SETTINGS"]["students"])
            ass = RepoJSONAssigments(ud, config["SETTINGS"]["assignments"])
            gr = RepoJSONGrade(ud, config["SETTINGS"]["grades"])

        s=Service(st,ass,gr,ud)
        ui=UI(s,ud,repository)
        ui.Start()
settings=Settings("settings.properties")
settings.start()





