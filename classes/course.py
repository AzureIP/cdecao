class Course:



    def __init__(self, index, dbId, name, max_participants, min_participants):
        self.index: int = index
        self.dbId: int = dbId
        self.name: str = name
        self.instructor_ids: list[int] = []
        self.max_participants: int = max_participants
        self.min_participants = min_participants




