class Userplan:
    def __init__(self, data, alluser, allplan):
        self.data = data
        self.alluser = alluser
        self.allplan = allplan
        self.user = None
        self.plan = None

    def _get_plan(self, id):
        tmp = None
        for pln in self.allplan:
            if pln["Id"] == id:
                tmp = pln
                break
        return tmp

    def _get_user(self, id):
        tmp = None
        for usr in self.alluser:
            if usr["Id"] == id:
                tmp = usr
                break
        return tmp

    def get_alluserplan(self):
        result = []
        for dat in self.data:
            dat["User"] = self._get_user(dat["User"])
            dat["Plan"] = self._get_plan(dat["Plan"])
            result.append(dat)

        return result

    def get_userplan(self, user):
        for pln in self.data:
            if pln["User"] == user["Id"]:
                pln["Plan"] = self._get_plan(pln["Plan"])
                self.plan = pln
                self.plan["User"] = user
                break

        return self.plan

    def add_userplan(self, user, plan, refferal):
        tmp = None
        for pln in self.data:
            if pln["User"] == user["Id"]:
                print(f"User Sudah terdaftar!")
                break
        return tmp

    def upgrade_userplan(self, name, plan):
        pass

