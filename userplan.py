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

    def _get_refferal(self, refferal):
        tmp = None
        for usr in self.alluser:
            if usr["Refferal"] == refferal:
                tmp = usr["Refferal"]
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
                return 'User Sudah terdaftar!'

        if not self._get_refferal(refferal):
            return "Refferal invalid!"

        if user["Refferal"] == refferal:
            return "Refferal ilegal!"

        tmp = {
            "Id": len(self.data) + 1,
            "User": user["Id"],
            "Plan": plan["Id"],
            "Months": 0,
            "Bill": plan["Price"] - (plan["Price"] * 0.04)
        }
        self.data.append(tmp)
        return self.data

    def upgrade_userplan(self, user, plan):
        tmp = None
        disc = 0
        for pln in self.data:
            if pln["User"] == user["Id"]:
                tmp = pln
                break

        if not tmp:
            return "User belum terdaftar!"

        print(tmp)
        if plan["Id"] <= tmp["Plan"]:
            return "Upgrade invalid!"

        if tmp["Months"] >= 13:
            disc = 0.05
        else:
            disc = 0

        tmp["Plan"] = plan["Id"]
        tmp["Bill"] = plan["Price"] - (plan["Price"] * disc)

        for i in range(len(self.data)):
            if self.data[i]["Id"] == tmp["Id"]:
                self.data[i] = tmp
        
        return self.data
