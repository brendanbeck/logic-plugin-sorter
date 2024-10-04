class Plugin:
    def __init__(self, name, manufacturer, subtype, au_type):
        self.name = name
        self.manufacturer = manufacturer
        self.subtype = subtype
        self.au_type = au_type
        self.tagset = self._generate_tagset_name()

    def _generate_tagset_name(self):
        return (self.au_type.encode().hex() + "-"
                + self.subtype.encode().hex() + "-"
                + self.manufacturer.encode().hex())
