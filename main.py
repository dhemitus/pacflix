#!/usr/bin/env python3

from user import User
from plan import Plan
from userplan import Userplan
from db import user_data
from db import plan_data
from db import user_plan

if __name__ == "__main__":

    user = User(user_data)

    #print(user.get_userbyname("bagus"))
    #print(user.get_userbyid(2))
    #user.add_user("Bagus")
    user.add_user("Toni")
    #print(user.get_userbyname("toni"))
    #print(user.refferal)
    #print(user.get_alluser())

    cahya = user.get_userbyname("cahya")

    toni = user.get_userbyname("toni")

    plan = Plan(plan_data)
    plan.add_plan("Exclusive Plan", "True", "True", 8, ["SD", "HD", "UHD", "UUHD"], 240_000)
    #print(plan.data);
    basic = plan.get_planbyname("premium plan")
    #print(plan.get_planbyname("Exclusive Plan"))

    userplan = Userplan(user_plan, user.data, plan.data)
    #userplan.get_userplan(bagus)
    #print(userplan.plan)
    #print(userplan.get_alluserplan())
    #print("\n\n--------------------------------\n\n")
    #print(userplan.add_userplan(toni, basic, 'ana-2134'))
    
    print("\n\n--------------------------------\n\n")
    print(userplan.upgrade_userplan(cahya, basic))
