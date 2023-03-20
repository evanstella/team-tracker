import datetime

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
            "checkin"  : "None" if (self.last_checkin == None) else self.last_checkin.strftime("%H:%M %d%^b%Y"),
            "notes"    : str(self.notes),
            "admin"    : self.admin
        }
