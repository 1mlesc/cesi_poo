class Team:
    def __init__(self, members=None):
        self.members = members if members is not None else []

    def add_member(self, member):
        self.members.append(member)

    def get_alive_members(self):
        return [m for m in self.members if m.is_alive()]

    def is_defeated(self):
        return all(not m.is_alive() for m in self.members)
