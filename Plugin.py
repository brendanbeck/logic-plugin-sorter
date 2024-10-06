class Plugin:
    def __str__(self):
        return self.name + " " + self.tagset

    def __init__(self, name: str, manufacturer: str, subtype: str, au_type: str):
        self.name = name
        self.manufacturer = manufacturer
        self.subtype = subtype
        self.au_type = au_type
        self.tagset = self._generate_tagset_name()
        self._category = None

    def _generate_tagset_name(self):
        return (self.au_type.encode().hex() + "-"
                + self.subtype.encode().hex() + "-"
                + self.manufacturer.encode().hex())

    def set_category(self, category: str):
        self._category = category

    def get_category(self):
        return self._category

    def get_tagset(self):
        return self.tagset

    def get_name(self):
        return self.name
