class Plan:
    def __init__(self, data):
        self.data = data
        self.id = None
        self.name = None
        self.stream = None
        self.download = None
        self.devices = None
        self.quality = None
        self.content = None
        self.price = None

    def get_allplan(self):
        return self.data

    def get_planbyname(self, name):
        result = None
        for value in self.data:
            if value["Name"].lower() == name.lower():
                result = value
                self.id = value["Id"]
                self.name = value["Name"]
                self.stream = value["Can Stream"]
                self.download = value["Can Download"]
                self.devices = value["Devices"]
                self.quality = value["Quality"]
                self.content = value["Content"]
                self.price = value["Price"]
                break

        return result

    def get_planbyid(self, id):
        result = None
        for value in self.data:
            if value["Id"] == id:
                result = value
                self.id = value["Id"]
                self.name = value["Name"]
                self.stream = value["Can Stream"]
                self.download = value["Can Download"]
                self.devices = value["Devices"]
                self.quality = value["Quality"]
                self.content = value["Content"]
                self.price = value["Price"]
                break

        return result

    def add_plan(self, name, stream, download, quality, devices, content, price):
        tmp = None
        for value in self.data:
            if value["Name"].lower() == name.lower():
                tmp = value
                break

        if not tmp:
            tmp = {
                "Id": len(self.data) + 1,
                "Name": name,
                "Can Stream": stream,
                "Can Download": download,
                "Devices": devices,
                "Quality": quality,
                "Content": content,
                "Price": price
            }
            self.data.append(tmp)
            return self.data
        else:
            return "Nama plan sudah ada!"
