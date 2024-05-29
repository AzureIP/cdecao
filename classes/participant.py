class Participant:



    def __init__(self, index, dbId, name, choices):
        self.index: int = index
        self.dbId: int = dbId
        self.name: str = name
        self.choices: list[int] = choices