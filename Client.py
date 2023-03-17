class Client():
    def __init__(self, name, icon, admin=False):
        self.name         = name
        self.lat          = None
        self.lon          = None
        self.last_checkin = None 
        self.icon         = icon
        self.online       = False
        self.admin        = admin
        self.notes        = None

    def to_dict(self):
        return {
            "name"     : self.name,
            "lat"      : str(self.lat),
            "lon"      : str(self.lon),
            "icon"     : self.icon,
            "checkin"  : str(self.last_checkin),
            "notes"    : str(self.notes),
            "admin"    : self.admin
        }
