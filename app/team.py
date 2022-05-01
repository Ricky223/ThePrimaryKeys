class Team:
    teamName: str

    def __init__(self):
        teamName = ''

    def set_teamName(self, name):
        self.teamName = name

    def getTeamName(self):
        return self.teamName
