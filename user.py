class User:
    def __init__(self, data):
        self.data = data
        self.id = None
        self.name = None
        self.refferal = None

    def get_alluser(self):
        return self.data

    def get_userbyname(self, name):
        result = None
        for value in self.data:
            if value["Name"].lower() == name.lower():
                result = value
                self.id = value["Id"]
                self.name = value["Name"]
                self.refferal = value["Refferal"]
                break

        return result

    def get_userbyid(self, id):
        result = None
        for value in self.data:
            if value["Id"] == id:
                result = value
                self.id = value["Id"]
                self.name = value["Name"]
                self.refferal = value["Refferal"]
                break

        return result

    def add_user(self, name):
        tmp = None
        for value in self.data:
            if value["Name"].lower() == name.lower():
                tmp = value
                break

        if not tmp:
            tmp = {
                "Id": len(self.data) + 1,
                "Name": name,
                "Refferal": name.lower() + "-1234"
            }
            self.data.append(tmp)
            return self.data
        else:
            return "User sudah ada!"
